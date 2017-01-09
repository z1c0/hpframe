import sys
from time import sleep
import config
import pygame
from picamera import PiCamera

camera = PiCamera()



def RecordVideo(name, initialDelay, duration):
  fullName = config.VIDEO_DIR + name
  print fullName
  # countDown
  for i in range(initialDelay, -1, -1):
    label = myfont.render(str(i), 1, (0, 0, 200), (255, 255, 255))
    screen.blit(label, (200, 100))
    pygame.display.flip()
    sleep(1)

  # now record video
  camera.start_preview()
  camera.start_recording(fullName)
  sleep(duration)
  camera.stop_recording()
  camera.stop_preview()




countDown = int(sys.argv[1])
duration = int(sys.argv[2])
#print countDown

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
pygame.display.set_caption("")
myfont = pygame.font.SysFont("monospace", 35)

#pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
#pygame.display.flip()
#pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(80, 230, 60, 60))
#pygame.display.flip()
#sleep(1)

RecordVideo("first", 5, 5)
RecordVideo("first", 3, 15)


pygame.quit()
quit()
