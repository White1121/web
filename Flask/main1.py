from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/blog/{id}")
def get_blog(id):
    return {"data":f"Blog 的 id 是：{id}"}