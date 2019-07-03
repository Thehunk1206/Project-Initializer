#!/bin/sh
# use 'chmod u+x createproject' to make command executable
function createproject() {
    read -p "Enter Your Github Username: "  $usernameGithub
    echo
    read -s -p "Enter Your Github Password: " $usernamePassword
    echo
    if [ -z $githubProjectName]
    then
        read -p "Enter project name: " $githubProjectName
    fi
    echo "Creating project $githubProjectName ..."
    python3 'createproject.py' $githubProjectName $usernameGithub $usernamePassword
}

createproject $githubProjectName
