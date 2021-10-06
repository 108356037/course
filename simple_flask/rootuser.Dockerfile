# local 端的 file structure 如下
# ----------------------------------------------------
#└── simple_flask
#    ├── nonrootuser.Dockerfile
#    ├── rootuser.Dockerfile
#    ├── myapp
#    │   ├── app.py
#    │   └── templates
#    │       └── index.html
#    └── requirements.txt

# Base image 是 python:3.7
FROM python:3.7

# requirements.txt 裡有我們需要的套件資訊， 
# 把他複製到container裡，路徑為 /app/requirements.txt
COPY ./requirements.txt /app/requirements.txt

# pip是python的套件管理工具
RUN pip install -r /app/requirements.txt

# 切換到container裡的 /app 路徑作為工作目錄 
WORKDIR /app

# 把本地端myapp資料夾複製到container的當前目錄 (/app)
ADD ./myapp .

# 5000是我們服務所在的port
EXPOSE 5000

# CMD代表command，當你啟動這個container時，會預設執行這個指令
CMD ["python3","/app/app.py"]
