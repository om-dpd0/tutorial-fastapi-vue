from fastapi import FastAPI, File, UploadFile
import os
import multipart
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'hello world'}

@app.post('/upload-file/')
async def upload_file(file : UploadFile = File(...)):
    file_location = f"./uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    return {"info":f"file is saved at {file_location}"}