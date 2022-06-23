#coding:utf-8

import rosbag
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

imgPath='./ros_img/' #存放图片的位置
bagPos = '/home/computer/r3live_ws/hku_campus_seq_00.bag'
imgTopic = '/camera/image_color/compressed'
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

class ImageCreator():
    def __init__(self):
        print("start processing...")
        self.bridge = CvBridge()
        with rosbag.Bag(bagPos, 'r') as bag:   #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == imgTopic:  #图像的topic；
                    try:
                        # cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        cv_image = self.bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
                    except CvBridgeError as e:
                        print e
                    timestr = "%.9f" %  msg.header.stamp.to_sec()
                    #%.6f表示小数点后带有9位，可根据精确度需要修改；
                    image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
                    cv2.imwrite(imgPath+image_name, cv_image)  #保存；
                    print("saving: {0}".format(image_name))
        print("done.")
                        


if __name__ == '__main__':

    #rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
