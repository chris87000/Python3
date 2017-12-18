
import sys
import os
#import pprint
from pathlib import Path
import inspect

print(os.environ)
print(Path.cwd())
print(sys.path)


lines = inspect.getsourcelines(Path)
print("".join(lines[0]))