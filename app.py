import uvicorn
from fastapi import FastAPI, File, Request, UploadFile
from starlette.responses import FileResponse,Response
import test

app = FastAPI()
@app.get("/",tags=['測試服務狀態'])
def Hello():
    return{"status":200}

@app.get("/moduel",tags=['測試模組結合'])
def TestModeuel(Somethong:str):
    return test.modeuel1(Somethong)

@app.post("/name/",tags=['給文字參數回檔案下載'], response_description='xlsx')
async def ReturnExcel(Name:str):
    print(Name)
    return FileResponse(Name+'.xlsx', filename=Name+'.xlsx')

@app.post("/files/",tags=["圖片上傳"])
async def UploadImage(file: UploadFile = File(...)):
    contents=await file.read()
    with open("./testimg.jpg","wb") as f:
        f.write(contents)
    return {"filename":file.filename}

if __name__ == '__main__':
    uvicorn.run(app="app:app", host="0.0.0.0", port=8000, reload=True, debug=True)
