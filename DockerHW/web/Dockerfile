# 使用 Python 官方輕量級映像檔
FROM python:3.9-slim

# 在容器內建立並設定工作目錄
WORKDIR /app

# 將當前目錄的所有檔案 (包含 app.py 和 requirements.txt) 複製進容器
COPY . /app

# 安裝 Flask (讀取 requirements.txt)
RUN pip install -r requirements.txt

# 宣告容器在執行時會監聽 5000 port (對應你 app.py 的設定)
EXPOSE 5000

# 啟動 Flask 伺服器
CMD ["python", "app.py"]