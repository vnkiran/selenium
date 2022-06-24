import os
import webbrowser

#link = 'https://www.google.com/'
links = ['https://www.youtube.com/','https://www.google.com/','https://mail.google.com/mail/u/0/?ogbl#inbox']
#webbrowser.open(link)

for i in links:
    webbrowser.open_new_tab(i)
    #webbrowser.open(i)

#os.startfile('cmd')
#os.startfile("C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
#selenium automation for daily tasks
#if ur applications are hide go to views and select hidden option
#application full path-  C:\Users\ADMIN\AppData\Local\Programs\Microsoft VS Code\Code.exe
#users>admin>appdata>roaming>microsoft>windows>startmenu>programs>startup (paste ur developed .py file)