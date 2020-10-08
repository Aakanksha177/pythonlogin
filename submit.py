import subprocess
import sys

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

install()

import requests
url = "http://12ved.pythonanywhere.com/static/test_app.py"
r = requests.get(url)

with open("test_app.py",'wb') as f:
    f.write(r.content)

import test_app

with open("test_app.py",'w') as f:
    f.write("[]")
