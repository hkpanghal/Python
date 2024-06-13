from fastapi import FastAPI,UploadFile # type: ignore
import uvicorn # type: ignore

app = FastAPI()

@app.get("/")
def home():
    return {"data":"welcome to the homepage "}

@app.get("/contact")
def contact():
    return {"data":"welcome to the contact page "}

@app.post("/upload")
def upload(file:list[UploadFile]):
    return {"status":"got the files"}


uvicorn.run(app)