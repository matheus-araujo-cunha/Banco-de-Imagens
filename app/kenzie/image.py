import os
from flask import safe_join


FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")

def checking_file_size(content_length):
    
    if int(content_length) > int(MAX_CONTENT_LENGTH):
        raise ValueError({
            "error":"File size is invalid",
            "expected":"File size less than 1MB"
        })
        

def get_file_path(filename:str):
    abs_path = os.path.abspath(FILES_DIRECTORY)
    filepath = safe_join(abs_path,filename)
    return filepath

def validate_name_file(filename):
    list_files = walk_files()
   
    for _,_,file in list_files:
        if filename in file:
            raise FileExistsError({
                "error":"File name already exists"
            }) 

def walk_files():
    return os.walk(FILES_DIRECTORY)

def validate_extension_file(extension_file):

    if extension_file not in ALLOWED_EXTENSIONS:
        raise PermissionError({
            "error": "File extension not allowed",
            "expected_extensions":ALLOWED_EXTENSIONS,
            "received": extension_file
        })


def list_by_extension(extension_file):
    list_files_extension = list(os.listdir(f"{FILES_DIRECTORY}/{extension_file}"))

    return list_files_extension

def list_all_files():
    all_files = walk_files()

    return [all_files for _,_,file in all_files for all_files in file]
