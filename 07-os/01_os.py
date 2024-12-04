import os
import shutil
from datetime import datetime
print(os.listdir())

if not os.path.exists("example_dir"):
    os.makedirs("example_dir")

print(os.path.abspath("./01_os.py"))
print(os.path.basename("./01_os.py")) # filename without the directories to it
print(os.path.abspath(os.path.dirname("./01_os.py")))
print(os.path.join("Users", "kevin", "Documents"))

with open("test", "w") as test:
    test.write("This is a test" * 100)

print(os.path.getsize("test"))

if os.path.getsize("test") > 100000:
    shutil.move("test", f"test.{datetime.now()}")

os.rmdir("example_dir")

print(os.cpu_count())
print(os.environ["PATH"])