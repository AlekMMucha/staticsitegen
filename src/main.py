import os
import shutil
def main():
    ###check if the public is empty, if not then make it empty
    path_to_public_dir = "../public"
    path_to_static_dir = "../static"
    ###checking to see if path is intact, if it is removeing it and adding to clear it.
    if os.path.exists(path_to_public_dir):
        shutil.rmtree(path_to_public_dir)
    os.mkdir(path_to_public_dir)
    ###checking to see if static dir is there
    if not os.path.exists(path_to_static_dir):
        raise Exception("No static directory to copy from")
    copy_layer_recursive(path_to_public_dir,path_to_static_dir)
###recursive function to copy all of static dir to public dir with logger decorator

def logger(func):
    def wrapper(current_path_public,current_path_static):
        print(f"Currently copying from :\n{current_path_static} to:\n{current_path_public}")
        func(current_path_public,current_path_static)
    return wrapper

@logger
def copy_layer_recursive(current_path_public,current_path_static):
    directory_list = os.listdir(current_path_static)
    for item in directory_list:
        if not os.path.isdir(os.path.join(current_path_static,item)):
            shutil.copy(os.path.join(current_path_static,item),current_path_public)
        else:
            os.mkdir(os.path.join(current_path_public,item))
            copy_layer_recursive(os.path.join(current_path_public,item),os.path.join(current_path_static,item))

main()