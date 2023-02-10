import os
import subprocess
from datasets.data_utils import MBIBDataLoader



print("------------Processing-datasets------------")
datasets_path = './datasets'
data_dirs = [ name for name in os.listdir(datasets_path) if os.path.isdir(os.path.join(datasets_path, name))]
for d in data_dirs:
    if "pycache" in d or 'mbib' in d:
        continue
    subprocess.call("python " + os.path.join(datasets_path,d,'process.py'),shell=True)
print("------------datasets-processed------------")
print("------------creating-mbib------------")
dl = MBIBDataLoader()
dl.create_all_categories()