import os
from flask import safe_join

FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")


def starting_project():
    root_path = os.getcwd()
    file_exist = os.access(FILES_DIRECTORY, os.F_OK)

    if not file_exist:
       os.mkdir(FILES_DIRECTORY)
       for extension in ALLOWED_EXTENSIONS:
           os.mkdir(f"{FILES_DIRECTORY}/{extension}")

    return root_path

def checking_file_size(content_length):
    
    if int(content_length) > int(MAX_CONTENT_LENGTH):
        raise ValueError({
            "error":"File size is invalid",
            "expected":"File size less than 1MB"
        })
        

def get_file_path(filename:str, extension_file=""):
    if extension_file:
        abs_path = os.path.abspath(f"{FILES_DIRECTORY}/{extension_file}")    
    else:
        abs_path = os.path.abspath(FILES_DIRECTORY)    
    filepath = safe_join(abs_path,filename)
    return filepath

def validate_name_file(filename, extension_file):
    list_files_extension = listdir(extension_file) 
   

    if filename in list(list_files_extension):
        raise FileExistsError({
            "error":"File name already exists"
            })            
    return list_files_extension 

def validate_file_exist(filename,extension_file):
    list_files_extension = listdir(extension_file) 
    
    
    if not filename in list_files_extension:
        raise FileNotFoundError({
            "error":"File Not found"
        })
    return list_files_extension   
            
def walk_files():
    return os.walk(FILES_DIRECTORY)

def listdir(extension_file):
    return os.listdir(f"{FILES_DIRECTORY}/{extension_file}")    

def validate_extension_file(extension_file):

    if extension_file not in ALLOWED_EXTENSIONS:
        raise PermissionError({
            "error": "File extension not allowed",
            "expected_extensions":ALLOWED_EXTENSIONS,
            "received": extension_file
        })


def list_by_extension(extension_file,ROOT_PATH=""):
    if ROOT_PATH:
        os.chdir(ROOT_PATH)
    list_files_extension = list(os.listdir(f"{FILES_DIRECTORY}/{extension_file}"))
    

    if not list_files_extension:
        raise FileNotFoundError({
            "error":f"There are no files in {extension_file} directory"
            })

    return list_files_extension

def list_all_files():
    all_files = walk_files()
    extensions = list(walk_files())[0][1]
    response = {key:[] for key in extensions}

    for _,_,files in list(all_files):
        files_list = []        
        for file in files:
            files_list.append(file)
            response[file[file.index(".")+1:]] = files_list
    return response        

    

def changing_path_and_zip_files(ROOT_PATH,file_extension,compression_ratio=-9):
    os.chdir(f"{ROOT_PATH}/{FILES_DIRECTORY}")
    os.system(f"zip {compression_ratio} -r {file_extension}.zip {file_extension}")
    os.system(f"mv {file_extension}.zip /tmp")
    os.chdir("/tmp")

    

def format_name_file(file):
      content_file = file.filename.split(".")
      extension_file = content_file[1]
      return extension_file