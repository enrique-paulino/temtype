import os, subprocess

a = subprocess.Popen("pythonw wsgi.py")
os._exit(0)
