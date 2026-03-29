# 使用輕量級的 Nginx 伺服器作為基底映像檔
FROM nginx:alpine

# 將你本地端 DockerHW 資料夾內的網頁檔案，複製到容器內 Nginx 預設的網頁路徑
COPY . /usr/share/nginx/html

# 宣告容器在執行時會監聽 80 port
EXPOSE 80