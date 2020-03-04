import os, os.path

DIR = '/Users/xuhaoming/Desktop/machine-learning/my_keras/vacation-image-search-engine/dataset'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
# 805