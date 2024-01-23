import os
import sys
import re

config_path = './swap_rename.config'
config = {}

if os.path.exists(config_path):
    with open(config_path) as file:
        for line in file:
            # simple comments to aid the users
            if line.startswith('#'):
                continue
            match = re.search(r'(\w+)\s*=\s*(.+)', line)
            if match:
                config[match.group(1)] = match.group(2)
# Such that it can be more easily setup, the script will create the config file if it doesn't exist and do nothing else
else:
    with open(config_path, 'w') as file:
        file.write('''# What the script will in short is this: You have a file named file1 and another named final_name. When ran, it will make final_name be named file2 and file1 be named final_name. This is useful when you want to swap the names of two files.
file1=
file2=
final_name=''')

# handling for incorrect configs is simply do nothing
config_keys = config.keys()
required_keys = ['file1', 'file2', 'final_name']
for key in required_keys:
    if key not in config_keys:
        sys.exit()

file1_exists = os.path.exists(config['file1'])
file2_exists = os.path.exists(config['file2'])
final_file_exists = os.path.exists(config['final_name'])

if final_file_exists:
    if file1_exists:
        os.rename(config['final_name'], config['file2'])
        os.rename(config['file1'], config['final_name'])
    elif file2_exists:
        os.rename(config['final_name'], config['file1'])
        os.rename(config['file2'], config['final_name'])
else:
    if file1_exists:
        os.rename(config['file1'], config['final_name'])