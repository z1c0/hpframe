import os
import subprocess
from picamera import PiCamera
from time import sleep

fileName = '/home/pi/videos/good.h264'

camera = PiCamera()
camera.resolution = (800, 1200)
camera.brightness = 40
camera.hflip = True
camera.start_preview()
camera.start_recording(fileName)
camera.wait_recording(10)
camera.stop_recording()
camera.stop_preview()

# conver to mp4
fileNameMp4 = fileName + '.mp4';
process = subprocess.Popen(['MP4Box', '-add', fileName, fileNameMp4])
process.wait()
os.remove(fileName)

#MP4Box -fps 30 -add myvid.h264 myvid.mp4

#omxplayer video.h264
#camera.capture('/home/pi/Desktop/image.jpg')



