import os
os.system("pip install --upgrade pip")
def dependencies(deps = []):
  for i in deps:
    os.system("pip install "+i)
    os.system("clear")