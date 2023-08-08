# Algoritm for data acquisition
# Developed by Ismael Mendoza
# 24/09/2022

fileName = "tesis.csv"

import serial
from serial import SerialException
import sys
import os

dirP = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

sys.path.append(dirP + '/z1_ref_other/0_lib')
Complete_trial = 0


import pygame
import sys
import time
import pyautogui
import math


from CONFIG import *
from concurrent.futures import ThreadPoolExecutor

VAR = 1
FIN = 0
# *********************
# Build the interface
# ####################

arduino_port = "COM15"
baud = 9600


screen = pyautogui.size()

screen_width = screen[0]
screen_height = screen[1]
screen_width_o = screen[0]
screen_height_o = screen[1]
scaling_factor = 1

# Normalize everything to the size of the bar as determined below
screen_width = int(screen_width / scaling_factor)
screen_height = int(screen_height / scaling_factor)
screen = pygame.display.set_mode((screen_width, screen_height))  # Setting up the screen size
pygame.display.set_caption('Motor Imagery Experiment')
screen_height = min(screen_width, screen_height)
screen_width = min(screen_height, screen_width)

spaceToBeLeft = 2.5 * int(screen_width * 0.1)  # space to be left at the edges of the rectangle to fit the
# images at the sides (2*original bar width)
Bigger_rectangle_width = screen_width - 2 * spaceToBeLeft
bar_width = 0.5 * Bigger_rectangle_width

# Load flexion and extension images, scale them, and place them at the side of the rectangle
flexion_image = pygame.image.load('flexion.png')
image_scaling_flexion = spaceToBeLeft / flexion_image.get_rect().size[0]
flexion_image = pygame.transform.scale(flexion_image, (
    int(spaceToBeLeft), int(flexion_image.get_rect().size[1] * image_scaling_flexion)))
(flexion_image_x, flexion_image_y) = (0, screen_height / 2 - flexion_image.get_rect().size[1] / 2)
extension_image = pygame.image.load('extension.png')
image_scaling_extension = spaceToBeLeft / extension_image.get_rect().size[0]
extension_image = pygame.transform.scale(extension_image, (
    int(spaceToBeLeft), int(extension_image.get_rect().size[1] * image_scaling_extension)))
(extension_image_x, extension_image_y) = (
    screen_width - spaceToBeLeft, screen_height / 2 - extension_image.get_rect().size[1] / 2)

bar_height = int(flexion_image.get_rect().size[
                     1] * 0.2086701)  # make the height of the bar consistent with the size of wrist in the images

# setting the dimensions of the rectangle in which the bar moves right/left
Bigger_rectangle_height = bar_height
Bigger_rectangle_X = screen_width_o / 2 - Bigger_rectangle_width / 2
Bigger_rectangle_Y = screen_height / 2 - bar_height / 2 + bar_height * 2
Bigthickness = 3  # thickness of the edge lines for the rectangle and other shapes

# color setting
black = (0, 0, 0)
bigRecEdgeColor = (185, 188, 181)  # FES:(130,92,63) #
bigRecColor = (46, 52, 54)  # FES:(198,160,131) #
barColor = bigRecEdgeColor
white = (225, 225, 225)
yellow = (255, 255, 0)
rightRed = (203, 0, 0)
leftBlue = (52, 101, 163)
upGreen = (0, 128, 0)

# Initial position of the bar in the middle of the rectangle:
initial_x = screen_width - bar_width
initial_y = Bigger_rectangle_Y
centerOfScreen = (screen_width_o / 2, screen_height / 2)
initial_x_2 = centerOfScreen[0]
thickness = 0

# correct for cue arrows by increasing the width of the bar so it is aligned with the arrow as it reaches the end of the task
arrowMidShift = (bar_height / 2)
bar_width = bar_width + arrowMidShift
initial_x = initial_x - arrowMidShift / 2

# new rectangle dimensions
Bigger_rectangle_new_X = (Bigger_rectangle_X + (Bigger_rectangle_width / 2)) - (Bigger_rectangle_height / 2)
Bigger_rectangle_new_Y = (Bigger_rectangle_Y + Bigger_rectangle_height) - (Bigger_rectangle_width / 2
                                                                           + Bigger_rectangle_height / 2)
Bigger_rectangle_height_new = Bigger_rectangle_width / 2 + Bigger_rectangle_height / 2

# new 'down' rectangle dimensions (not used here)
Down_rectangle_X = Bigger_rectangle_new_X
Down_rectangle_Y = Bigger_rectangle_new_Y + (Bigger_rectangle_height_new - Bigger_rectangle_height)

# new bar
bar_height_new = Bigger_rectangle_height
bar_width_new = bar_height
initial_y_new = Bigger_rectangle_new_Y + (Bigger_rectangle_height_new / 2)
initial_x_new = Bigger_rectangle_new_X

######## Arrow dimensions goes here
rightArrowStartingX = Bigger_rectangle_X + Bigger_rectangle_width
rightArrowStartingY = Bigger_rectangle_Y
leftArrowStartingX = Bigger_rectangle_X
lefttArrowStartingY = Bigger_rectangle_Y
ArrowTipWidth = bar_width / 3.5
ArrowRectangleHeight = Bigger_rectangle_height
ArrowRectangleWidth = 0.5 * ArrowTipWidth

point1RightArrow = (rightArrowStartingX + ArrowRectangleWidth + ArrowTipWidth, Bigger_rectangle_Y + bar_height / 2)
point2RightArrow = (rightArrowStartingX + ArrowRectangleWidth, Bigger_rectangle_Y + bar_height / 2 +
                    ArrowTipWidth / math.sqrt(3))
point3RightArrow = (rightArrowStartingX + ArrowRectangleWidth, Bigger_rectangle_Y + bar_height / 2 -
                    ArrowTipWidth / math.sqrt(3))

point1LeftArrow = (leftArrowStartingX - ArrowRectangleWidth - ArrowTipWidth, Bigger_rectangle_Y + bar_height / 2)
point2LeftArrow = (leftArrowStartingX - ArrowRectangleWidth, Bigger_rectangle_Y + bar_height / 2 +
                   ArrowTipWidth / math.sqrt(3))
point3LeftArrow = (leftArrowStartingX - ArrowRectangleWidth, Bigger_rectangle_Y + bar_height / 2 -
                   ArrowTipWidth / math.sqrt(3))

upArrowStartingX = Bigger_rectangle_new_X
upArrowStartingY = Bigger_rectangle_new_Y - ArrowRectangleWidth
upArrowRectangleHeight = ArrowRectangleWidth
upArrowRectangleWidth = ArrowRectangleHeight

point1UpArrow = (centerOfScreen[0], upArrowStartingY - ArrowTipWidth)
point2UpArrow = (centerOfScreen[0] - ArrowTipWidth / math.sqrt(3), upArrowStartingY)
point3UpArrow = (centerOfScreen[0] + ArrowTipWidth / math.sqrt(3),
                 upArrowStartingY)

# adjustment to bar_width for drawing the bars
bar_width = Bigger_rectangle_height

# changes in horizontal rectangle to create two rectangles
Bigger_rectangle_width_adj = Bigger_rectangle_width / 2 + bar_width / 2
Bigger_rectangle_X_adj = Bigger_rectangle_X + (Bigger_rectangle_width / 2 - bar_width / 2)

##################################
######## RUN STARTS HERE #########
##################################

def visualinterface():

# Left hand and right HandArrows and up arrow
    pygame.draw.rect(screen, rightRed,
                     (rightArrowStartingX, rightArrowStartingY, ArrowRectangleWidth, ArrowRectangleHeight),
                     0)  # Moving bar specs
    pygame.draw.rect(screen, upGreen,
                     (upArrowStartingX, upArrowStartingY, upArrowRectangleWidth, upArrowRectangleHeight),
                     0)  # Moving bar specs
    pygame.draw.rect(screen, leftBlue,
                     (leftArrowStartingX, lefttArrowStartingY, -1 * ArrowRectangleWidth, ArrowRectangleHeight),
                     0)  # Moving bar specs
    pygame.draw.polygon(screen, upGreen, (point1UpArrow, point2UpArrow, point3UpArrow))
    pygame.draw.polygon(screen, rightRed, (point1RightArrow, point2RightArrow, point3RightArrow))
    pygame.draw.polygon(screen, leftBlue, (point1LeftArrow, point2LeftArrow, point3LeftArrow))

    # draw the big rectangle in which the bar moves right and left
    pygame.draw.rect(screen, bigRecColor,
                     (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                      Bigger_rectangle_height),
                     0)  # filled left rectangle
    pygame.draw.rect(screen, bigRecEdgeColor,
                     (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                      Bigger_rectangle_height),
                     Bigthickness)  # edges of left rectangle
    pygame.draw.rect(screen, bigRecColor,
                     (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                      Bigger_rectangle_height),
                     0)  # filled right rectangle
    pygame.draw.rect(screen, bigRecEdgeColor,
                     (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                      Bigger_rectangle_height),
                     Bigthickness)  # edges of right rectangle
    pygame.draw.rect(screen, bigRecColor,
                     (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                      Bigger_rectangle_height_new), 0)  # third direction bar
    pygame.draw.rect(screen, bigRecEdgeColor,
                     (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                      Bigger_rectangle_height_new),
                     Bigthickness)  # edges of the rectangle (third)
    pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width), thickness)  # draw the bar
    pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width), thickness)  # draw the bar
    pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width))  # up bar

    pygame.display.update()

    time.sleep(
        ExperimentConfigureTime)  # display the interface for a certain period that is set in the i0_configFile.py file

    screen.fill(black)

    prevTime = time.time()  # record time at beginning of the trial

    arrowColor = white

    for trial in trials:  # trial = +1 (extension)/-1(flexion)

        currentClass = trial
        if (currentClass == 1):
            arrowColor = rightRed

        if (currentClass == -1):
            arrowColor = leftBlue

        if (currentClass == 2):
            arrowColor = upGreen

        print('Class of current trial: ', currentClass)

        # ***************************
        # ** NEW TRIAL BEGINS HERE **
        # ***************************

        SendID(',1000')
        if FIN == 1:
            sys.exit()
        # Draw the big rectangle and the bar
        #############################################################################
        pygame.draw.rect(screen, rightRed,
                         (rightArrowStartingX, rightArrowStartingY, ArrowRectangleWidth, ArrowRectangleHeight),
                         0)  # Moving bar specs
        pygame.draw.rect(screen, leftBlue,
                         (leftArrowStartingX, lefttArrowStartingY, -1 * ArrowRectangleWidth, ArrowRectangleHeight),
                         0)  # Moving bar specs
        pygame.draw.rect(screen, upGreen,
                         (upArrowStartingX, upArrowStartingY, upArrowRectangleWidth, upArrowRectangleHeight),
                         0)  # Moving bar specs
        pygame.draw.polygon(screen, upGreen, (point1UpArrow, point2UpArrow, point3UpArrow))
        pygame.draw.polygon(screen, rightRed, (point1RightArrow, point2RightArrow, point3RightArrow))
        pygame.draw.polygon(screen, leftBlue, (point1LeftArrow, point2LeftArrow, point3LeftArrow))

        pygame.draw.rect(screen, bigRecColor,
                         (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                          Bigger_rectangle_height),
                         0)  # filled left rectangle
        pygame.draw.rect(screen, bigRecEdgeColor,
                         (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                          Bigger_rectangle_height),
                         Bigthickness)  # edges of left rectangle
        pygame.draw.rect(screen, bigRecColor,
                         (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                          Bigger_rectangle_height),
                         0)  # filled right rectangle
        pygame.draw.rect(screen, bigRecEdgeColor,
                         (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                          Bigger_rectangle_height),
                         Bigthickness)  # edges of right rectangle
        pygame.draw.rect(screen, bigRecColor,
                         (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                          Bigger_rectangle_height_new), 0)  # third direction bar
        pygame.draw.rect(screen, bigRecEdgeColor,
                         (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                          Bigger_rectangle_height_new),
                         Bigthickness)  # edges of the rectangle (third)

        pygame.draw.rect(screen, barColor, (initial_x_new, Down_rectangle_Y, bar_width, bar_width))
        pygame.draw.rect(screen, barColor, (initial_x_new, Down_rectangle_Y, bar_width, bar_width))
        pygame.draw.rect(screen, barColor, (initial_x_new, Down_rectangle_Y, bar_width, bar_width))

        pygame.display.update()

        # <<<<<< FIXATION CUE >>>>>>

# <<<<<< TASK CUE >>>>>>

# Drawing arrow polygon to point towards required task (right for extension and left for flexion and up for both hands)
        point1 = 0
        point2 = 0
        point3 = 0
        if currentClass == 1 or currentClass == -1:
            pygame.draw.rect(screen, arrowColor, (
                centerOfScreen[0] - currentClass * arrowMidShift, Bigger_rectangle_Y + bar_height / 2 - bar_height / 6,
                currentClass * bar_height / 2,
                2 * bar_height / 6), thickness)  # Arrow Specs
            point1 = (centerOfScreen[0] + currentClass * bar_height / 2, Bigger_rectangle_Y + bar_height / 2)
            point2 = (centerOfScreen[0], Bigger_rectangle_Y + bar_height / 2 - 0.35 * bar_height)
            point3 = (centerOfScreen[0], Bigger_rectangle_Y + bar_height / 2 + 0.35 * bar_height)
        else:
            pygame.draw.rect(screen, arrowColor, (
                centerOfScreen[0] - bar_height / 6, Bigger_rectangle_Y + bar_height / 2, 2 * bar_height / 6,
                Bigger_rectangle_height / 2), thickness)  # Arrow Specs
            point1 = (centerOfScreen[0], Bigger_rectangle_Y)
            point2 = (centerOfScreen[0] - 0.35 * bar_height, Bigger_rectangle_Y + bar_height / 2)
            point3 = (centerOfScreen[0] + 0.35 * bar_height, Bigger_rectangle_Y + bar_height / 2)

        pygame.draw.polygon(screen, arrowColor, (point1, point2, point3))
        pygame.display.update()

        # COMENTAMOS ESTO
        if (currentClass == -1):
            SendID(',600')
        #        SendID(',769')  # send Event CUE: 769 to LOOP to indicate flexion cue
        if (currentClass == 1):
            SendID(',700')
        #        SendID(',770') # send Event CUE: 770 to LOOP to indicate extension cue
        if (currentClass == 2):
            SendID(',800')
        #        SendID(',771')

        time.sleep(cueTime)  # wait for the period determined in a0_configFile.py

        screen.fill(black)  # clear display

        prevTime = time.time()
        task_cue = 0

        # <<<<<< TASK BEGINS >>>>>>


        if currentClass == -1 and task_cue == 0:
            SendID(',601')
            if FIN == 1:
                sys.exit()

        elif currentClass == 1 and task_cue == 0:
            SendID(',701')
            if FIN == 1:
                sys.exit()

        elif currentClass == 2 and task_cue == 0:
            SendID(',801')
            if FIN == 1:
                sys.exit()


        fflag = 1

        while True:

            x_bar = initial_x_new
            y_bar = Bigger_rectangle_Y
            delta_width = bar_width
            delta_width_1 = bar_width
            delta_height_2 = bar_width

            # find how much the bar must move to the left based on how much time has passed
            if currentClass == -1:
                step_size = (0.5 * Bigger_rectangle_width - 0.5 * bar_width) * (time.time() - prevTime) / taskTime
                x_bar = initial_x_new + currentClass * step_size  # init_x+step_size*currentClass
                # move the bar according to selected class (flexion/extension)
                delta_width = bar_width + step_size

            elif currentClass == 1:
                step_size = (0.5 * Bigger_rectangle_width - 0.5 * bar_width) * (time.time() - prevTime) / taskTime
                # move the bar according to selected class (flexion/extension)
                delta_width_1 = bar_width + step_size
            else:
                step_size = (0.5 * Bigger_rectangle_width - bar_width * 0.5) * (time.time() - prevTime) / taskTime
                y_bar = Bigger_rectangle_Y - step_size
                delta_height_2 = bar_width + step_size

            # re-draw the interface
            if fflag:
                pygame.draw.rect(screen, rightRed,
                                 (rightArrowStartingX, rightArrowStartingY, ArrowRectangleWidth, ArrowRectangleHeight),
                                 0)  # Moving bar specs
                pygame.draw.rect(screen, leftBlue,
                                 (leftArrowStartingX, lefttArrowStartingY, -1 * ArrowRectangleWidth, ArrowRectangleHeight),
                                 0)  # Moving bar specs
                pygame.draw.rect(screen, upGreen,
                                 (upArrowStartingX, upArrowStartingY, upArrowRectangleWidth, upArrowRectangleHeight),
                                 0)  # Moving bar specs

                pygame.draw.polygon(screen, upGreen, (point1UpArrow, point2UpArrow, point3UpArrow))
                pygame.draw.polygon(screen, rightRed, (point1RightArrow, point2RightArrow, point3RightArrow))
                pygame.draw.polygon(screen, leftBlue, (point1LeftArrow, point2LeftArrow, point3LeftArrow))
                fflag = 0

            pygame.draw.rect(screen, bigRecColor,
                             (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                              Bigger_rectangle_height),
                             0)  # filled left rectangle
            pygame.draw.rect(screen, bigRecEdgeColor,
                             (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                              Bigger_rectangle_height),
                             Bigthickness)  # edges of left rectangle
            pygame.draw.rect(screen, bigRecColor,
                             (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                              Bigger_rectangle_height),
                             0)  # filled right rectangle
            pygame.draw.rect(screen, bigRecEdgeColor,
                             (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                              Bigger_rectangle_height),
                             Bigthickness)  # edges of right rectangle
            pygame.draw.rect(screen, bigRecColor,
                             (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                              Bigger_rectangle_height_new), 0)  # third direction bar
            pygame.draw.rect(screen, bigRecEdgeColor,
                             (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                              Bigger_rectangle_height_new),
                             Bigthickness)  # edges of the rectangle (third)
            pygame.draw.rect(screen, barColor, (initial_x_new, Bigger_rectangle_Y, delta_width_1, bar_width),
                             thickness)  # draw the bar right
            pygame.draw.rect(screen, barColor, (x_bar, Bigger_rectangle_Y, delta_width, bar_width),
                             thickness)  # draw the bar left
            pygame.draw.rect(screen, barColor, (initial_x_new, y_bar, bar_width, delta_height_2))  # draw up bar

            # Drawing arrow polygon to point towards required task (right for extension and left for flexion)
            if currentClass == 1 or currentClass == -1:
                pygame.draw.rect(screen, arrowColor, (
                    centerOfScreen[0] - currentClass * arrowMidShift, Bigger_rectangle_Y + bar_height / 2 - bar_height / 6,
                    currentClass * bar_height / 2,
                    2 * bar_height / 6), thickness)  # Arrow Specs
            else:
                pygame.draw.rect(screen, arrowColor, (
                    centerOfScreen[0] - bar_height / 6, Bigger_rectangle_Y + bar_height / 2, 2 * bar_height / 6,
                    Bigger_rectangle_height / 2), thickness)  # Arrow Specs

            pygame.draw.polygon(screen, arrowColor, (point1, point2, point3))

            pygame.display.update()

            # Stopping criteria based on taskTime that is set in a0_configFile.py
            if (time.time() - prevTime >= taskTime):


                if currentClass == -1:
                    SendID(',602')
                #send Event CUE: 7692 to LOOP to indicate end of flexion task and start of result view time
                elif currentClass == 1:
                    SendID(',702')
                #send Event CUE: 7702 to LOOP to indicate end of extension task and start of result view time
                elif currentClass == 2:
                    SendID(',802')
                # <<<<<< RESULT CUE >>>>>>

                # Arrange the elements of the display to generate the result cue correctly
                #############################################################################
                pygame.draw.rect(screen, rightRed,
                                 (rightArrowStartingX, rightArrowStartingY, ArrowRectangleWidth, ArrowRectangleHeight),
                                 0)  # Moving bar specs
                pygame.draw.rect(screen, leftBlue,
                                 (leftArrowStartingX, lefttArrowStartingY, -1 * ArrowRectangleWidth, ArrowRectangleHeight),
                                 0)  # Moving bar specs
                pygame.draw.rect(screen, upGreen,
                                 (upArrowStartingX, upArrowStartingY, upArrowRectangleWidth, upArrowRectangleHeight),
                                 0)  # Moving bar specs

                pygame.draw.polygon(screen, upGreen, (point1UpArrow, point2UpArrow, point3UpArrow))
                pygame.draw.polygon(screen, rightRed, (point1RightArrow, point2RightArrow, point3RightArrow))
                pygame.draw.polygon(screen, leftBlue, (point1LeftArrow, point2LeftArrow, point3LeftArrow))

                pygame.draw.rect(screen, bigRecColor,
                                 (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                                  Bigger_rectangle_height),
                                 0)  # filled left rectangle
                pygame.draw.rect(screen, bigRecEdgeColor,
                                 (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                                  Bigger_rectangle_height),
                                 Bigthickness)  # edges of left rectangle
                pygame.draw.rect(screen, bigRecColor,
                                 (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                                  Bigger_rectangle_height),
                                 0)  # filled right rectangle
                pygame.draw.rect(screen, bigRecEdgeColor,
                                 (Bigger_rectangle_X_adj, Bigger_rectangle_Y, Bigger_rectangle_width_adj,
                                  Bigger_rectangle_height),
                                 Bigthickness)  # edges of right rectangle
                pygame.draw.rect(screen, bigRecColor,
                                 (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                                  Bigger_rectangle_height_new), 0)  # third direction bar
                pygame.draw.rect(screen, bigRecEdgeColor,
                                 (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                                  Bigger_rectangle_height_new),
                                 Bigthickness)  # edges of the rectangle (third)
                pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width),
                                 thickness)  # draw the bar
                pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width),
                                 thickness)  # draw the bar
                pygame.draw.rect(screen, barColor, (initial_x_new, initial_y, bar_width, bar_width))  # up bar

                if currentClass == 2:
                    pygame.draw.rect(screen, arrowColor,
                                     (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                                      Bigger_rectangle_height_new),
                                     0)  # fill bar with the class color
                    pygame.draw.rect(screen, bigRecEdgeColor,
                                     (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                                      Bigger_rectangle_height_new),
                                     Bigthickness)  # mark the edge of the bar with original color

                    pygame.draw.rect(screen, bigRecEdgeColor,
                                     (Bigger_rectangle_new_X, Bigger_rectangle_new_Y, Bigger_rectangle_height,
                                      Bigger_rectangle_height_new),
                                     Bigthickness)  # Bigger edge mark

                    pygame.draw.circle(screen, arrowColor,
                                       (int(centerOfScreen[0]), int(Bigger_rectangle_Y + bar_height / 2)),
                                       int(bar_height * 0.8),
                                       0)  # draw a colored filled circle to show result
                    pygame.draw.circle(screen, bigRecEdgeColor,
                                       (int(centerOfScreen[0]), int(Bigger_rectangle_Y + bar_height / 2)),
                                       int(bar_height * 0.8), Bigthickness)  # highlight the edge of the circle

                    # Drawing arrow polygon
                    pygame.draw.rect(screen, white, (
                        centerOfScreen[0] - bar_height / 6, Bigger_rectangle_Y + bar_height / 2, 2 * bar_height / 6,
                        Bigger_rectangle_height / 2), thickness)  # Arrow Specs  # Arrow Specs
                    pygame.draw.polygon(screen, white, (point1, point2, point3))

                else:
                    pygame.draw.rect(screen, arrowColor,
                                     (centerOfScreen[0], Bigger_rectangle_Y, currentClass * Bigger_rectangle_width / 2,
                                      bar_height),
                                     0)  # fill bar with the class color
                    pygame.draw.rect(screen, bigRecEdgeColor,
                                     (centerOfScreen[0], Bigger_rectangle_Y, currentClass * Bigger_rectangle_width / 2,
                                      bar_height),
                                     Bigthickness)  # mark the edge of the bar with original color

                    pygame.draw.rect(screen, bigRecEdgeColor,
                                     (Bigger_rectangle_X, Bigger_rectangle_Y, Bigger_rectangle_width,
                                      Bigger_rectangle_height),
                                     Bigthickness)  # Bigger edge mark

                    pygame.draw.circle(screen, arrowColor,
                                       (int(centerOfScreen[0]), int(Bigger_rectangle_Y + bar_height / 2)),
                                       int(bar_height * 0.8),
                                       0)  # draw a colored filled circle to show result
                    pygame.draw.circle(screen, bigRecEdgeColor,
                                       (int(centerOfScreen[0]), int(Bigger_rectangle_Y + bar_height / 2)),
                                       int(bar_height * 0.8), Bigthickness)  # highlight the edge of the circle

                    # Drawing arrow polygon
                    pygame.draw.rect(screen, white, (
                        centerOfScreen[0] - currentClass * arrowMidShift,
                        Bigger_rectangle_Y + bar_height / 2 - bar_height / 6,
                        currentClass * bar_height / 2, 2 * bar_height / 6), thickness)  # Arrow Specs
                    pygame.draw.polygon(screen, white, (point1, point2, point3))

                pygame.display.update()

                time.sleep(resultTime)

                # sendTiD(1000)  # send Event CUE: 1000 to LOOP to indicate end of result view time
                SendID(',1001')
                break

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()


        task_cue = 0
        screen.fill(black)
        pygame.display.update()

        # <<<<<< REST >>>>>>
        time.sleep(restTime + random.random())

    end()
    time.sleep(3)
    logFile = sys.argv[1]
    print(logFile)
    f = open(logFile, "a+")

    f.write("ExperimentConfigureTime %f\r\n" % ExperimentConfigureTime)
    f.write("fixationCrossTime %f\r\n" % fixationCrossTime)
    f.write("cueTime %f\r\n" % cueTime)
    f.write("timeout %f\r\n" % timeout)
    f.write("taskTime %f\r\n" % taskTime)
    f.write("resultTime %f\r\n" % resultTime)
    f.write("restTime %f\r\n" % restTime)
    f.write("detectionThresholdLH %f\r\n" % detectionThresholdLH)
    f.write("detectionThresholdRH %f\r\n" % detectionThresholdRH)
    f.write("detectionThresholdBH %f\r\n" % detectionThresholdBH)
    f.write("nTrials %f\r\n" % n_LH)
    f.close()


def SendID(Trigg):
    global TEMP

    TEMP = str(Trigg)

def end():
    global VAR
    VAR = 3

def SerialComunication():

    global TEMP
    global FIN

    try:
        ser = serial.Serial(arduino_port, baud)
        FIN = 0
    except SerialException:
        print("¡¡ERROR COMMUNICATION SERIAL!!")
        FIN = 1
        sys.exit()
    # ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    print("Created file")

    # display the data to the terminal
    getData = str(ser.readline())
    data = getData[2:][:-6] + TEMP
    TEMP = ',0'
    print(data)

    # add the data to the file
    file = open(fileName, "a")  # append the data to the file
    file.write(data + "\\n")  # write data with a newline

    file.close()

    print_labels = False
    line = 0  # start at 0 because our header is 0 (not real data)
    while VAR < 2:
        # incoming = ser.read(9999)
        # if len(incoming) > 0:
        if print_labels:
            if line == 0:
                print("Printing Column Headers")
            else:
                print("Line " + str(line) + ": writing...")
        getData = str(ser.readline())
        data = getData[2:][:-6] + TEMP
        TEMP = ',0'
        print(data)

        file = open(fileName, "a")
        file.write(data + "\n")  # write data with a newline
        line = line + 1

    print("Data collection complete!")
    file.close()

if __name__ == '__main__':

    executor = ThreadPoolExecutor(max_workers=3)

    executor.submit(SerialComunication)
    executor.submit(visualinterface)