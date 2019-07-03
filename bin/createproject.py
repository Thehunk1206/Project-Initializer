import os
from selenium import webdriver
import subprocess
import time
import urllib
from getpass import getpass
from sys import argv, platform


def createDirectory():
    global projectPath
    # option to manually set path

    # This sets path for project folder
    # Application will save projects to ~/project-initializer/projects by default
    projectPath = os.path.join(os.path.expanduser(
        "~"), 'project-initializer', 'projects')
    if not os.path.exists(projectPath):
        print("Making directory at", projectPath)
        os.makedirs(projectPath, exist_ok=True)
    else:
        print("Directory ", projectPath,  " already exists")


def WebdriverDo():
    # Asking User to enter the description of project which has to be in Github project description
    Description = str(input("Enter the description of project: "))

    # Getting Github username and password
    usernameGithub = str(input("Enter Your Github Username: "))
    passwordGithub = getpass(prompt="Enter Your Github Password: ")

    # Give your chromedriver's executable path as an argument to parameter "executable_path"
    ## EXAMPLE: browser = webdriver.Chrome(executable_path='/usr/lib/chromedriver_linux64/chromedriver')
    browser = webdriver.Chrome(
        executable_path='/usr/lib/chromedriver_linux64/chromedriver')
    # Also, you could use firefox's geckodriver. We used chromedriver above.
    browser.get("https://github.com/login")

    username = browser.find_element_by_name('login')
    # GithubUsername from sysarg are passed here
    username.send_keys(usernameGithub)

    password = browser.find_element_by_name('password')
    # GithubPassword from sysarg are passed here
    password.send_keys(passwordGithub)

    loginbutton = browser.find_element_by_name('commit')
    loginbutton.click()

    print(usernameGithub, " logged in successfully!")

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
    makeLocal(usernameGithub)


def makeLocal(usernameGithub):
    global projectPath
    if folderName == None:
        print("Usage: createproject <project-name>")
    else:
        print(folderName)
        projectSaveDirectory = os.path.join(projectPath, folderName)
        os.makedirs(projectSaveDirectory)
        print("Project will be saved at ", projectSaveDirectory)
        print("Making", folderName, " locally available")
    gitCommands = ("git init",
                   "git remote add origin https://github.com/"+usernameGithub+"/"+folderName,
                   "touch README.md",
                   "git add .",
                   "git commit -m 'first commit'",
                   "git push -u origin master",
                   "exec bash")
    for i in range(7):
        os.system(gitCommands[i])
    pass


if __name__ == "__main__":
    # python interpreter is running this file as the main program, thus _name_=="__main__"
    projectPath, folderName = "", str(argv[1])
    createDirectory()
    WebdriverDo()
