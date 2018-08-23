#The goal of this project is to use and familiarize with pyautogui
#and simplify the process of generating a new email
#pyautogui cheatsheet https://pyautogui.readthedocs.io/en/latest/cheatsheet.html

import pyautogui
import time
import sys

mail_reg_url = 'https://service.mail.com/registration.html?edition=int&lang=en&#.1258-header-signup2-1'


#F6 is shortcut for chrome to input url
#\n == enter

'''
Plan steps
1. Open Google Chrome
2. Input URL
3. Input user info
4. Wait for user to complete captcha
5. Save user info as screenshot to a folder
6. Complete
'''

