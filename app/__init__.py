from flask import Flask,request,send_from_directory
from http import HTTPStatus

from app.kenzie import starting_project, list_by_extension,checking_file_size, format_name_file, changing_path_and_zip_files, get_file_path,validate_extension_file, validate_file_exist, validate_name_file, list_all_files
from app.kenzie.image import FILES_DIRECTORY

app = Flask(__name__)
ROOT_PATH = starting_project()


@app.get("/download/<file_name>")
def download_by_filename(file_name:str):
    extension = file_name[file_name.find(".") +1:]

    try:
        validate_file_exist(file_name,extension)
        return send_from_directory(
            directory=f"../{FILES_DIRECTORY}/{extension}",
            path=file_name,
            as_attachment=True
        )
    except FileNotFoundError as FileNotFound:
        return FileNotFound.args[0],HTTPStatus.NOT_FOUND


@app.get("/download-zip")
def download_dir_as_zip():
    file_extension = request.args.get("file_extension")
    compression_ratio = request.args.get("compression_ratio")


    try:
        validate_extension_file(file_extension)
        list_by_extension(file_extension)
        changing_path_and_zip_files(ROOT_PATH,file_extension,compression_ratio)
    except FileNotFoundError as FileNotFound:
        return FileNotFound.args[0],HTTPStatus.NOT_FOUND
    except PermissionError as Permission:
        return Permission.args[0],HTTPStatus.NOT_FOUND        

    return send_from_directory(
        directory=f"/tmp",
        path=f"{file_extension}.zip",
        as_attachment=True
    )   

@app.get("/files")
def retrieve_files():
    list_files = list_all_files()
    return list_files

@app.get("/files/<extension>")
def retrieve_files_by_extension(extension:str):
    try:
        validate_extension_file(extension)
        response = list_by_extension(extension)
        return {extension:response},HTTPStatus.OK
    except PermissionError as Permission:
        return Permission.args[0],HTTPStatus.NOT_FOUND    

@app.post("/upload")
def upload():
   
    file = request.files["file"]
    content_length = request.headers["Content-Length"]
  
    extension_file = format_name_file(file)
    try:
        checking_file_size(content_length)
        validate_extension_file(extension_file)
        validate_name_file(file.filename,extension_file)
        filepath = get_file_path(file.filename, extension_file)
      
        file.save(filepath)  

        return {"message": "Upload image with success!"},HTTPStatus.CREATED      

    except ValueError as Value:
        return Value.args[0],HTTPStatus.REQUEST_ENTITY_TOO_LARGE
    except FileExistsError as FileExist:
        return FileExist.args[0],HTTPStatus.CONFLICT
    except PermissionError as Permission:
        return Permission.args[0],HTTPStatus.UNSUPPORTED_MEDIA_TYPE
   
