import socket

from fastapi import FastAPI
from redis import Redis

app = FastAPI()
redis = Redis(host="redis", port=6379)


@app.get("/")
def root():
    visits = redis.incr("visits")
    return socket.gethostname(), visits
