import os
def dependencies(deps = []):
  for i in deps:
    os.system("pip install "+i)
    