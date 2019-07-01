
function createproject(){
    echo "Creating" $1"..."
    cd
    #exicute python code
    #Set the path to python file
    python3 /home/<username>/.createProject.py $1
    #add your project path before '$1' which you have set in python script.
    cd /home/<username>/Desktop/Myprojects/$1
    git init
    #add your github project git link here
    git remote add origin https://github.com/<GithubUsermane>/<projectName>.git
    touch README.md
    git add .
    git commit -m "first commit"
    git push -u origin master
    exec bash

}

createproject $1
