# dependencies
## a dependencies tool
first download `dep.py`. then `import dep`. then do 
```py
dep.dependencies([dependencies])
```
this installs the dependencies with `pip`.
example:
```py
import dep
dep.dependencies(["bs4", "request", "flask"])
```
