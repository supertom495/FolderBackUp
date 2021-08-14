from distutils.dir_util import copy_tree
from datetime import datetime
import time
import yaml

with open('./config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

while(True):
    stamp = str(int(time.time()))

    fromDirectory = config['from']
    toDirectory = config['to'] + '\\' + stamp

    copy_tree(fromDirectory, toDirectory)

    print("finished: " + stamp)

    time.sleep(config['sleep'])

