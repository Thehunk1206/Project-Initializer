import os
import sys
from selenium import webdriver
import subprocess
import time
import urllib

# kept in global scope for easy access
if len(sys.argv) != 4:
    print('Input error.')
else:
    # This sets path for project folder
    projectPath = os.path.join(os.path.expanduser("~"), 'project-initializer')
    if not os.path.exists(projectPath):
        os.mkdir(projectPath)
    else:
        print("Directory ", projectPath,  " already exists")

    try:
        # Github login information goes here
        # Username
        USERNAME = str(sys.argv[2])
        # Password 'WARNING:Do not share this piece of scirpt to any one with Password Entered'
        PASSWORD = str(sys.argv[3])
    else:
        # lol
        print("Username \& Password input error.")
    # Asking User to enter the description of project which has to be in Github project description
    Description = str(input("Enter the description of project: "))

    # Setting the path of chrome driver
    ## EXAMPLE: '/usr/lib/chromedriver_linux64/chromedriver'
    # Default is lib/chromedriver of project path
    browser = webdriver.Chrome(executable_path=os.path.join(
        projectPath, 'lib', 'chromedriver'))
    browser.get("https://github.com/login")


def create():
    global Description, USERNAME, PASSWORD

    if sys.argv[1] == None:
        print("Usage: createproject <project name>")
    else:
        folderName = str(sys.argv[1])
        print(folderName)
        os.makedirs(projectPath + folderName)

    username = browser.find_element_by_name('login')
    username.send_keys(USERNAME)

    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)

    loginbutton = browser.find_element_by_name('commit')
    loginbutton.click()

    print(USERNAME, " logged in successfully!")

    browser.get("https://github.com/new")
    reponame = browser.find_element_by_name("repository[name]")
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
