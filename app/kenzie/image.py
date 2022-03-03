# Desenvolva sua lógica de manipulação das imagens aqui
import os
from flask import safe_join

FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")

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
    
    return converted_to_megabyte < int(MAX_CONTENT_LENGTH)
        

def get_file_path(filename:str):
    abs_path = os.path.abspath(FILES_DIRECTORY)
    filepath = safe_join(abs_path,filename)
    return filepath