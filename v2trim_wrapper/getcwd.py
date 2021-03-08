import os
import os.path
from inspect import getsourcefile
execution_folder = os.path.abspath(getsourcefile(lambda: 0))
one_folder_down = "/".join(execution_folder.split("/")[:-2])
v2trim_folder_generator = os.walk(one_folder_down)
print(one_folder_down)
