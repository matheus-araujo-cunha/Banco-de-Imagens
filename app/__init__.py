from flask import Flask,request,safe_join,send_file
from http import HTTPStatus
import os


app = Flask(__name__)

MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")
FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")


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
    return            