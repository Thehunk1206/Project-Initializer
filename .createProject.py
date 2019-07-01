import os 
import sys

from selenium import webdriver
import time
import urllib

#set the path for project folder
path = "/home/tauhid/Desktop/Myprojects/"
#enter your Github username here
USERNAME = ""
#Enter your Github password here 'WARNING:Do not share this piece of scirpt to any One with Password Entered'
PASSWORD = ""

#Asking User to enter the description of project which has to be in Github project description
Description = str(input("Enter the description of project: "))

#set the path of chrome driver
#EXAMPLE:-'/usr/lib/chromedriver_linux64/chromedriver'
browser = webdriver.Chrome(executable_path='path/to/chromedriver')
browser.get("https://github.com/login")


def create():
    if sys.argv[1] == None:
        print("Usage: createproject <'project name'>")
    else:
        folderName = str(sys.argv[1])
        print(folderName)
        os.makedirs(path + folderName)

    username = browser.find_element_by_name('login')
    username.send_keys(USERNAME)

    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)

    loginbutton = browser.find_element_by_name('commit')
    loginbutton.click()

    print("user logged in....")
    

    browser.get("https://github.com/new")
    reponame = browser.find_element_by_name('repository[name]')
    reponame.send_keys(folderName)
    repoDes = browser.find_element_by_name("repository[description]")
    repoDes.send_keys(Description)
    time.sleep(2)

    createRepo = browser.find_element_by_css_selector('button.first-in-line')
    createRepo.submit()

    time.sleep(3)
    browser.close()

    


if __name__ == "__main__":
    create()