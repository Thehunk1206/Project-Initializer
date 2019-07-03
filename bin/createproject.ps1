# DONT RUN
function createproject($githubProjectName) {
    # TODO: Check for Python, Selenium, Webdriver, Git
    # TODO: Stop process and prompt Installation and Instructions
    Write-Host "Project-Initializer"
    if ([string]::IsNullOrWhitespace($githubProjectName)){
        $githubProjectName =  Read-Host "Enter project name"
    }
    Write-Host "Creating project $githubProjectName ..."
    python3 'createproject.py' $githubProjectName
}
createproject $githubProjectName