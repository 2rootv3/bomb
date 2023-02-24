import pyautogui
import time
import os
banner2='2009'
banner='''
dP   dP   dP          dP                                                
88   88   88          88                                                
88  .8P  .8P .d8888b. 88 .d8888b. .d8888b. 88d8b.d8b. .d8888b.          
88  d8'  d8' 88ooood8 88 88'  `"" 88'  `88 88'`88'`88 88ooood8          
88.d8P8.d8P  88.  ... 88 88.  ... 88.  .88 88  88  88 88.  ...          
8888' Y88'   `88888P' dP `88888P' `88888P' dP  dP  dP `88888P'          
                                                                        
                                                                        
8888ba.88ba              dP                          oo .8888b          
88  `8b  `8b             88                             88   "          
88   88   88 88d888b.    88        dP    dP .d8888b. dP 88aaa  .d8888b. 
88   88   88 88'  `88    88        88    88 88'  `"" 88 88     88ooood8 
88   88   88 88       dP 88        88.  .88 88.  ... 88 88     88.  ... 
dP   dP   dP dP       88 88888888P `88888P' `88888P' dP dP     `88888P'   
                                            +-+-+-+-+-+-+ +-+-+-+-+-+-+ 
                                            |H|a|c|k|e|r| |s|h|o|h|a|n| 
                                            +-+-+-+-+-+-+ +-+-+-+-+-+-+                                                                   
'''
os.system('clear')
print(banner)
print("Enter unlock password:")
password=int(input('=>'))
for x in banner2:
    if password != 2009:
        print("Invalid password!")
        exit()
print('Enter you message')
message=input('=>')
for i in range(0,10000000):
    time.sleep(0)
    pyautogui.typewrite(message)
    time.sleep(0.1)
    pyautogui.press('enter')