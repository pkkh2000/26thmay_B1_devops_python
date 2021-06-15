import time
import subprocess
import os
import platform
import getmac


user_input='''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-
Press 9 to exit the loop:-  
'''
while True :
    print(user_input)
    # to accept input from user 
    user_choice=input("Input Valid Choice  ")
    # printing user input 
    #print("user has entered ",user_choice)
    if user_choice == '1':
    # mytime=time.ctime()
        print("Current time is: ",time.ctime())
        
    elif  user_choice  ==  '2' :
        
        print("Total RAM size is ",((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))/(1024.**3)))  
        

    elif  user_choice  ==  '3' :
        print("Current Name is: ",platform.system())
    

    elif  user_choice  ==  '4' :
        print("Your Mac Address Is: ",getmac.get_mac_address()) 

    elif  user_choice  ==  '5' :
        ans=input("Enter The Name of Directory:- ")
        path="/home/harrypotter/Desktop/"+ans
        os.mkdir(path)

    elif  user_choice  ==  '6' :
        print("The OS will restart after 3 Second:")
        time.sleep(3)
        os.system("shutdown -r now")

    elif  user_choice  ==  '7' :
        print("Availble Wifi are: ")
        print(subprocess.getoutput("nmcli dev wifi"))
        
    elif  user_choice  ==  '8' :
        print(os.system("python3 basic.py"))

    elif  user_choice  ==  '9' :
        exit() 
 

    else :
        print("INVALID INPUT")