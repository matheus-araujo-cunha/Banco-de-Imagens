# Desenvolva sua lógica de manipulação das imagens aqui
from io import UnsupportedOperation
import os
from flask import safe_join


FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")

def checking_file_size(content_length):
    float_content = ""
    lenght_content = len(float_content)
    
    for index,number in enumerate(reversed(content_length),start=1):
        if index % 3 == 0 and not index == lenght_content:
            float_content += number+"."
        else:
            float_content += number    
    
    float_content = float(float_content[lenght_content::-1])

    
    converted_to_megabyte = float_content / int(MAX_CONTENT_LENGTH)


    
    if converted_to_megabyte > int(MAX_CONTENT_LENGTH):
        raise ValueError({
            "error":"File size is invalid",
            "expected":"File size less than 1MB"
        })
        

def get_file_path(filename:str):
    abs_path = os.path.abspath(FILES_DIRECTORY)
    filepath = safe_join(abs_path,filename)
    return filepath

def validate_name_file(filename,extension_file):
    list_files_extension = list(os.listdir(f"{FILES_DIRECTORY}/{extension_file}"))
    
    if filename in list_files_extension:
        raise FileExistsError({
            "error":"File name already exists"
        }) 

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
    all_files = os.walk(FILES_DIRECTORY)

    response = []

    for _,_,files in all_files:
        for file in files:
            response.append(file)    

    return response
