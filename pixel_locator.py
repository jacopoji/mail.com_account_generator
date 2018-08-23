import pyautogui as gui
import cv2
import numpy as np
'''
This is a simple program to find the location of your mouse and prints it
'''
font = cv2.FONT_HERSHEY_SIMPLEX

def pixel_locator():
    '''
    Constanly shows the coordinate of the mouse until user presses "q" to stop the program
    '''
    prev_x,prev_y = None,None #initialize a dummy variable
    text_origin = (0,50)
    text_scale = 1
    text_color = (0,0,0) #BLACK
    text_thickness = 2
    while True:
        x,y = gui.position() #get mouse coordinates
        if x != prev_x or y != prev_y:
            background = np.ones((100,350,3), np.uint8) * 255 #redefine image background
            cv2.putText(background,'x={}    y={}'.format(x,y),text_origin, font, text_scale,text_color,text_thickness,cv2.LINE_AA)
        cv2.imshow('canvas',background) #display window

        prev_x, prev_y = x,y #save variable

        if (cv2.waitKey(1) & 0xFF) == ord('q'): #keyboard interrupt
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pixel_locator()