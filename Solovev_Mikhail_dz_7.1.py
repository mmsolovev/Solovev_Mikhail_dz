import os


pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            current_dir = os.path.join(root, folder)
            if os.path.exists(current_dir):
                print(current_dir, 'существует')
            else:
                os.makedirs(current_dir)
