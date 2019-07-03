# DONT RUN
function createproject($githubProjectName) {
    # TODO: Check for Python, Selenium, Webdriver, Git
    # TODO: Stop process and prompt Installation and Instructions
    $usernameGithub = Read-Host "Enter Your Github Username: "
    Write-Host
    $usernamePassword = Read-Host "Enter Your Github Password: " -AsSecureString
    Write-Host
    if ([string]::IsNullOrWhitespace($githubProjectName)){
        $githubProjectName =  Read-Host "Enter project name: "
    }
    Write-Host "Creating project $githubProjectName ..."
    python3 'createproject.py' $githubProjectName $usernameGithub $usernamePassword
}

createproject $githubProjectName
