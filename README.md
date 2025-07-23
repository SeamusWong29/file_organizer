# File Sorter
A Python script that organizes files in a folder by extension or creation date.

## Features
- Sort files by extension or date
- Custom config via JSON
- Logs operations with timestamps

## Installation
```bash
git clone https://github.com/yourname/file-sorter.git
cd file-sorter    # Enter the downloaded project folder
pip install -r requirements.txt  # pip is Python's package installer, install every package listed inside it
python main.py --path ~/Downloads --mode ext

tells the system to run a python script
the name of your script
--path ~/Downloads You're passing the folder you want to organize (Downloads)
--mode ext You're telling your script to organize files by extension (e.g., .jpg, .pdf, .txt)






# git init
# git status

# stage and commit the file (change)
# git add main.py
# git commit -m "feat: initial version of file sorter script"

#Use this conventional commit format:
feat: new feature
fix: bug fix
refactor: code improvement
docs: documentation

# git diff
# git branch

# An experimental branch where I can freely code, basically the same idea when working with others on git.  
git checkout -b refactor-logging  # any name

git add main.py
git commit -m "refactor: extract logging to a separate function"

git checkout main

git merge refactor-logging

