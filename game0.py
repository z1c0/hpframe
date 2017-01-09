import sys
import pygame
from picamera import PiCamera
from time import sleep

camera = PiCamera()

countDown = int(sys.argv[1])
print countDown

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
pygame.display.set_caption("bla")

pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

camera.start_preview()
sleep(5)
camera.stop_preview()

# render text
myfont = pygame.font.SysFont("monospace", 35)
for i in range(countDown, -1, -1):
  label = myfont.render(str(i), 1, (0, 0, 200), (255, 255, 255))
  screen.blit(label, (200, 100))
  pygame.display.flip()
  sleep(1)

pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(80, 230, 60, 60))
pygame.display.flip()
sleep(1)

pygame.quit()
quit()
