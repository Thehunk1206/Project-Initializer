#!/bin/sh
# use 'chmod u+x createproject' to make command executable
function createproject() {
    # TODO: Check for Python, Selenium, Webdriver, Git
    # TODO: Stop process and prompt Installation and Instructions
    echo "Project: "$1
    read -p "Enter Your Github Username: "  $2`#usernameGithub`
    echo
    read -s -p "Enter Your Github Password: " $3`#usernamePassword`
    echo
    if [ -z $1] #githubProjectName
    then
        read -p "Enter project name: " $1`#githubProjectName`
    fi
    echo "Creating project $1`#githubProjectName` ..."
    python3 'createproject.py' $1`#githubProjectName` $2`#usernameGithub` $3`#usernamePassword`
}

createproject $1`#githubProjectName`
