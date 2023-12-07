from fastapi import FastAPI

app = FastAPI()
import redis

r = redis.Redis(host='localhost', port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World2 mordeczko Szoko bons twój wons"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"hits": r.get('hits')}
