import os

os.system("pwd" if os.name !="nt" else "cd")
os.system("echo 'This is a shell-created file.' > shellfile.txt" )

os.system("cat shellfile.txt" if os.name !="nt" else "type shellfile.txt")
print(os.name)

import subprocess # provides more advanced tooling for shell scripting.