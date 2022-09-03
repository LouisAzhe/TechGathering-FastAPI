# 技術小聚-實習生版
## 主題 : FastAPI(使用API串接現有服務)

※今日分享之相關網站參考-->FastAPI相關介紹.txt  
※相關環境設定請參考requirements.txt，Python版本3.9

※FastAPI使用注意事項  
1.安裝FastAPI和Uvicorn 使用前先安裝這兩個套件  
2.python version >= 3.6 FastAPI支援python3.6以上版本  
3.uvicorn main:app --reload 打開服務器(在Terminal)  
4.http://127.0.0.1:8000/docs 可以查看API文件 8000為預設  
▼下面這段可直接寫在程式裡面取代上面的3跟4▼  
if __name__ == '__main__':  
&emsp;&emsp;uvicorn.run(app="app:app", host="0.0.0.0", port=8000, reload=True, debug=True)  
