import os

home = os.environ['HOME']
directory_path = f'{home}/.m2/repository'

def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path:str = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        elif (full_path.endswith('.jar') or full_path.endswith('.pom')):
            substring_length = len(directory_path) + 1
            relative_path = full_path[substring_length:]
            print(relative_path)

# Specify the directory path you want to start from
list_files_recursive(directory_path)