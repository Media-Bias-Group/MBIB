import os
import subprocess

datasets_path = './datasets'
data_dirs = [ name for name in os.listdir(datasets_path) if os.path.isdir(os.path.join(datasets_path, name))]
for d in data_dirs:
    if "pycache" in d:
        continue
    subprocess.call("python " + os.path.join(datasets_path,d,'process.py'),shell=True)