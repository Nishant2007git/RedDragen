import os

import eel 

eel.init("www")

os.system('start chrome --app="http://localhost:8000/index.html"')

eel.start("index.html",  mode='none', host='localhost', block=True)