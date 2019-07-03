#!/bin/bash
# use 'chmod u+x createproject' to make command executable
function createproject() {
    # TODO: Check for Python, Selenium, Webdriver, Git
    # TODO: Stop process and prompt Installation and Instructions
    echo "Project-Initializer"
    if [ -z $1 ] #githubProjectName
    then
        read -p "Enter project name: " $1  #githubProjectName
    fi
    echo "Creating project $1..." #githubProjectName
    python3 'createproject.py' $1 #githubProjectName
}

createproject $1 #githubProjectName
