import os

for dirpath, dirnames, filenames in os.walk('/home/kiran.dumpa/WorkSpace'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
