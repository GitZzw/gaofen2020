# 北斗高分2020视觉

>   scripts 包含获取d435相机内参的脚本、tcp_ip信息传输+ros_topic融合  
    yolo_realsense_tcp.py：调用d435的pyrealsense2包获取实时图像并进行yolo检测的逻辑
    
>   src下test_node_time.cpp:接收飞机姿态msg，接收yolo识别结果msg，对齐时间戳，小孔成像估计深度和实际位置并发布，欧拉角四元数互相转化

>   camkelists:添加各种依赖，将.cpp编译为.out，将.py编译为可执行文件的方法

