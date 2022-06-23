# rosbag2img
transfer image topic from rosbag to image, each image is named by the corresponding timestamp. 

### usage:
edit file path and ros topic in rosbag2img.py:
```
imgPath='./ros_img/' #存放图片的位置
bagPos = '/home/computer/r3live_ws/hku_campus_seq_00.bag'
imgTopic = '/camera/image_color/compressed'
```
run command:
```
python2 rosbag2img.py
```

