from fileinput import filename
from flask import Flask,request,safe_join,send_file
from http import HTTPStatus
import os
from werkzeug.utils import secure_filename

from app.kenzie.image import FILES_DIRECTORY, checking_file_size, get_file_path

app = Flask(__name__)

ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")

file_exist = os.access(FILES_DIRECTORY, os.F_OK)


if not file_exist:
    os.mkdir(FILES_DIRECTORY)
    for extension in ALLOWED_EXTENSIONS:
        os.mkdir(f"{FILES_DIRECTORY}/{extension}")





@app.get("/download/<file_name>")
def download_by_filename(file_name:str):
    return

@app.get("/download-zip")
def download_zipped_files():
    file_extension = request.args.get("file_extension")
    compression_ratio = request.args.get("compression_ratio")
    return    

@app.get("/files")
def retrieve_files():
    return

@app.get("/files/<extension>")
def retrieve_files_by_extension(extension:str):
    return

@app.post("/upload")
def upload_file():
   
    file = request.files["file"]
    content_length = request.headers["Content-Length"]
    print(content_length)
    
    checked_size = checking_file_size(content_length)

    *_,content_type = file.headers[1]
    *_,extension_file = content_type.split("/")

   
    print(get_file_path(file.filename))

    list_files_extension = list(os.listdir(f"./{FILES_DIRECTORY}/{extension_file}"))
    
    if file.filename in list_files_extension:
        print("copiou")

    else:        

        if extension_file in ALLOWED_EXTENSIONS:
            UPLOAD_FOLDER = os.path.join(os.getcwd(),f"{FILES_DIRECTORY}/{extension_file}")
            savepath = os.path.join(UPLOAD_FOLDER,secure_filename(file.filename))
            file.save(savepath)
        else:
            ...


    
    # abs_path = os.path.abspath("fFILES_DIRECTORY")
    # file_path = safe_join(abs_path,file)
    return  ""          