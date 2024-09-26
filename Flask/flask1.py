from flask import Flask, request

app = Flask(__name__)     # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

# @app.route("/", methods=['POST']) # default methods=['GET']，可以透過網址列傳送所有的參數內容，POST不行
@app.route("/")           # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home(name):               # 發出請求後會執行 home() 的函式
    print(request.args)            # 使用 request.args
    return f"<h1>hello {name}</h1>"   # 執行函式後會回傳特定的網頁內容

@app.route("/<msg>")           # 加入 <msg> 讀取網址
def ok(msg):                   # 加入參數
    return f"<h1>{msg}</h1>"   # 使用變數

@app.route("/<path:msg>")     # 加入 path: 轉換成「路徑」的類型
def ok1(msg):
    return f"<h1>{msg}</h1>"

@app.route("/yes")
def yes():
    return "<h1>yes</h1>"

app.run()
# 指定埠號 port
# app.run(host="0.0.0.0", port=5555) # 設定 host 為 0.0.0.0 就能採用本機實際分配到的 IP 作為網址