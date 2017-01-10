from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.start_preview()
camera.start_recording('/home/pi/videos/hugo.h264')
sleep(5)
camera.stop_recording()
#camera.stop_preview()

#omxplayer video.h264

#camera.capture('/home/pi/Desktop/image.jpg')



