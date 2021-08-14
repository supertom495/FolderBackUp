from distutils.dir_util import copy_tree
from datetime import datetime
import time
import yaml


stamp = str(int(time.time()))

with open('./config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

fromDirectory = config['from']
toDirectory = config['to'] + '\\' + stamp

copy_tree(fromDirectory, toDirectory)

print("finished: " + stamp)

