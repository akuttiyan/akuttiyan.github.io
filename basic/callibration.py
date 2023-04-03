import pygame
import sys
import argparse
import cv2
import numpy as np
from os import path
from datetime import datetime


class App:
    def __init__(self):
        self.args = self.get_args()
        self.cap = cv2.VideoCapture()
        self.out = cv2.VideoWriter()
        self.done = None
        self.EXTENSION = "avi"
        self.BASE_DIR = "./eye-tracker-captures"  # MAKE SURE TO CREATE A FOLDER CALLED eye-tracker-captures IN YOUR DIRECTORY
        self.FILENAME_FORMAT = "calibration-{:%Y%m%d_%H%M%S}.{:s}"

    def get_args(self):
        parser = argparse.ArgumentParser(description="Eye tracker calibration tool.")
        parser.add_argument("frametime", metavar="N", type=int, help="")
        parser.add_argument("dots", metavar="N", type=int, help="")

        args = parser.parse_args()
        return args

    def gen_coords(self, w, h, num_of_dots):
        coords = []
        x_coords = [100 + i * (int((w - 200) / (num_of_dots - 1))) for i in range(num_of_dots)]
        y_coords = [100 + i * (int((h - 200) / (num_of_dots - 1))) for i in range(num_of_dots)]
        for y_coord in y_coords:
            for x_coord in x_coords:
                coords.append((x_coord, y_coord))
        return coords

    def open_cap(self):
        pixels_w = 640
        pixels_h = 480

        self.cap = cv2.VideoCapture(1)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, pixels_w)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, pixels_h)

        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        date = datetime.now()

        file_name = self.FILENAME_FORMAT.format(date, self.EXTENSION)
        file_path = path.normpath(path.join(self.BASE_DIR, file_name))

        self.out = cv2.VideoWriter(file_path, fourcc, 5.0, (pixels_w, pixels_h))

    def close_cap(self):

        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def main(self):
        self.done = False
        args = self.get_args()

        w = 1000
        h = 800
        circle_radius = 20

        pygame.init()
        screen = pygame.display.set_mode((w, h))

        frametime = args.frametime

        coordinates = self.gen_coords(w, h, args.dots)
        ind = 0
        clock = pygame.time.Clock()
        old_coord = coordinates[0]
        self.open_cap()
        while self.done != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            ret, img = self.cap.read()
            self.out.write(img)
            if ind // frametime < len(coordinates):
                coord = coordinates[ind // frametime]
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (255, 100, 0), (coord[0], coord[1]), circle_radius)
                ind += 1
                if old_coord != coord:
                    self.close_cap()
                    self.open_cap()
                old_coord = coord
            elif ind // frametime == len(coordinates):
                self.close_cap()
                ind += 1
            else:
                screen.fill((0, 0, 0))
            pygame.display.flip()
            clock.tick(60)
        self.close_cap()


if __name__ == "__main__":
    App().main()