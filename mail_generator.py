#The goal of this project is to use and familiarize with pyautogui
#and simplify the process of generating a new email
#pyautogui cheatsheet https://pyautogui.readthedocs.io/en/latest/cheatsheet.html

import pyautogui as gui
import time
import sys
import random

mail_reg_url = 'https://service.mail.com/registration.html?edition=int&lang=en&#.1258-header-signup2-1'
name_list = open('name_list.txt','r').read().split('\n')
name_list = list(filter(None,name_list))
#F11 is shortcut for chrome to be fullscreen
#\n == enter
#lines = 4944
'''
Plan steps (Also works as a checklist)
1. Open Google Chrome                            Done
2. Input URL                                     Done
3. Input user info
4. Wait for user to complete captcha
5. Save user info as screenshot to a folder
6. Complete
'''

def open_chrome():
    '''
    Locate the chrome icon in the task bar and click it
    return True if complete
    '''
    try:
        screen_resolution = gui.size()
        search_region = (0,int(screen_resolution[1]*0.9),int(screen_resolution[0]*0.5),int(screen_resolution[1]*0.1)) # (left, top, width, height)
        chrome_location = gui.locateCenterOnScreen('images/chrome.png',region=search_region) #
        assert chrome_location != None #make sure chrome is found
        gui.click(chrome_location) #click on the chrome icon
        #test:
        #print(chrome_location)
        return True
    except:
        return False

def input_URL():
    '''
    Open a New tab
    Input URL
    Hit Enter Key
    return True if complete
    '''
    try:
        gui.hotkey('ctrl','t')
        #gui.press('f6')
        gui.typewrite(mail_reg_url)
        gui.press('enter')
        return True
    except:
        return False

def user_info():
    '''
    Put in full screenmode (f11)
    Pull random name from name list
    Select Birthday as Jan 1 1991
    email address as {first_name}_{last_name}@mail.com
    Use Same password, defined by user
    Security Question --> City Born
    Answer --> New York

    All variables should be adjustable by the user.
    '''

    #------------------Variables you may change-----------------
    month = 'jan'
    day = '1'
    year = '1991'
    security_answer = 'New York'
    password = ''  #password has to be at least 8 characters long with upper and lower case 
    #-----------------------------------------------------------
    screen_resolution = gui.size()
    try:
        gui.press('f11')
        time.sleep(1)
        first_name_number = random.randint(0,len(name_list)-1)
        last_name_number = random.randint(0,len(name_list)-1)
        first_name = name_list[first_name_number]
        last_name = name_list[last_name_number]
        gui.press('tab')
        gui.typewrite(first_name)
        gui.press('tab')
        gui.typewrite(last_name)
        gui.press(['tab','tab'])
        gui.typewrite(month) #birthday
        gui.press('tab')
        gui.typewrite(day)
        gui.press('tab')
        gui.typewrite(year)
        gui.press(['tab','tab'])
        gui.typewrite('{}_{}'.format(first_name,last_name)) #email address format 
        gui.press(['tab','tab'])
        gui.typewrite(password) #Password
        gui.press('tab')
        gui.typewrite(password) #Re-type password
        gui.press(['tab','tab'])
        gui.typewrite('w') #first question starts with 'w'
        gui.press('tab')
        gui.typewrite(security_answer) #security question answer

        ####Press the email verification button
        verify_location = gui.locateCenterOnScreen('images/verify.png',confidence = 0.7) 
        gui.click(verify_location) #click on the verify icon
        #print(verify_location)

        ####Press the captcha verification button
        captcha_location = gui.locateCenterOnScreen('images/captcha.png',confidence = 0.7) 
        gui.click(captcha_location) #click on the verify icon
        #print(captcha_location)

        ####Save screenshot
        banner_location = gui.locateOnScreen('images/mail_banner.png')
        left = banner_location[0]
        top = banner_location[1]+banner_location[3]
        width = banner_location[2]
        height = screen_resolution[1]-banner_location[3]*8
        gui.screenshot('screenshots/{}_{}.jpg'.format(first_name,last_name),region = (left,top,width,height)) #saved screeenshot format is firstName_lastName.jpg

        #Check if Captcha verification is complete. If not, let user finish manually
        completed_captcha = gui.locateOnScreen('images/captcha_complete.png',confidence = 0.7)
        if completed_captcha is None:
            gui.alert('Please manually complete captcha and press ok')
        else:
            print(completed_captcha)
            
        #Click Accept and Complete 
        accept_location = gui.locateCenterOnScreen('images/accept.png',confidence = 0.7)
        #gui.click(accept_location)
        #print(accept_location)
        time.sleep(3)
        gui.press('f11') #quit fullscreen mode
        return True

    except:
        return False
        


if __name__ == "__main__":
    if open_chrome():
        print("Opened Google Chrome")
    else:
        print("Failed to Open Google Chrome")
        sys.exit()
    
    if input_URL():
        print("Jumped to mail registration page")
    else:
        print("Failed to input URL")
        sys.exit()

    if user_info():
        print("Comepleted user info input")
    else:
        print("Failed to input user info")
        sys.exit()
