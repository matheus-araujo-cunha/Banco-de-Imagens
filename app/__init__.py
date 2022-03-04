from fileinput import filename
from flask import Flask, jsonify,request,safe_join,send_file
from http import HTTPStatus
import os
from werkzeug.utils import secure_filename

#from app.kenzie.image import FILES_DIRECTORY
from app.kenzie import list_by_extension,checking_file_size, get_file_path,validate_extension_file, validate_name_file, list_all_files
from app.kenzie.image import ALLOWED_EXTENSIONS, FILES_DIRECTORY
app = Flask(__name__)


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
    list_files = list_all_files()
    return jsonify(list_files)

@app.get("/files/<extension>")
def retrieve_files_by_extension(extension:str):
    try:
        validate_extension_file(extension)
        response = list_by_extension(extension)
        return jsonify(response),HTTPStatus.OK
    except PermissionError as pe:
        return pe.args[0],HTTPStatus.NOT_FOUND    

@app.post("/upload")
def upload_file():
   
    file = request.files["file"]
    content_length = request.headers["Content-Length"]
    *_,content_type = file.headers[1]
    *_,extension_file = content_type.split("/")

    try:
        checking_file_size(content_length)
        validate_extension_file(extension_file)
        validate_name_file(file.filename,extension_file)

    
        abs_path = os.path.abspath(f"{FILES_DIRECTORY}/{extension_file}")
        filepath = safe_join(abs_path, file.filename)
        file.save(filepath)  

        return {"message": "Upload image with success!"},HTTPStatus.CREATED      

    except ValueError as ve:
        return ve.args[0],HTTPStatus.REQUEST_ENTITY_TOO_LARGE
    except FileExistsError as fee:
        return fee.args[0],HTTPStatus.CONFLICT
    except PermissionError as pe:
        return pe.args[0],HTTPStatus.UNSUPPORTED_MEDIA_TYPE

   


    
    
    

        

 
        
 

    
    # abs_path = os.path.abspath("fFILES_DIRECTORY")
    # file_path = safe_join(abs_path,file)
    return  ""          