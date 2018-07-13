#-*- coding: UTF-8 -*-
'''
根据设备名称获取相机设备号

使用前需要先安装v4l-utils

Installing v4l-utils (debian) gives one the handy v4l2-ctl command:
$ v4l2-ctl --list-devices

KS-WDR: KS-WDR (usb-0000:00:14.0-2):
	/dev/video0

H264 USB Camera: USB Camera (usb-0000:00:14.0-4.1):
	/dev/video1
	/dev/video2

所以我们可以根据设备名称去检索摄像头对应的序号
'''
from subprocess import PIPE,Popen

def find_cam(cam):
    cmd = ["/usr/bin/v4l2-ctl", "--list-devices"]
    out, err = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
    out = out.strip()
    # 降byte类型转换为string
    # out = str(out)
    for dev_name, dev_idx in [i.split(b"\n\t") for i in out.split(b"\n\n")]:
        if cam in dev_name:
            return dev_idx.decode('utf8')
    return None
    
if __name__ == "__main__":
    # 这里修改设备名称
    cam= b"KS-WDR"
    # 寻找设备编号
    dev_idx = find_cam(cam)
    if dev_idx is None:
        print("设备没有找到")
    else:
        print("设备编号： {}".format(dev_idx))

