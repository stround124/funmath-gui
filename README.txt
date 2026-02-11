Pre-creating
Install Python extensions in VSCode: Python, Python Debugger, Python Environments

VENV creation (in VSCode) - One time
1. Git clone to folder
2. Open the folder
3. Ctrl + Shift + P > Python: Create Environment
4. Select venv
5. Choose python executable (/usr/bin/python3 in Linux)
6. Ctrl + Shift + P > Python: Create Terminal
7. pip install briefcase

Project creation
8. briefcase new
9. Enter project details
10. deactivate
11. Ctrl + Shift + P > Debug: Add configuration
12. Python > Module
13. Enter briefcase
14. Edit to look like this:
{
    "name": "Briefcase: Dev",
    "type": "debugpy",
    "request": "launch",
    "module": "briefcase",
    "args": [
        "dev",
    ],
    "justMyCode": false
}
