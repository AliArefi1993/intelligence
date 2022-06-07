from fastapi import FastAPI
import redis
import database
import time
app = FastAPI()

cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.get("/")
async def root():
    count = get_hit_count()
    return {"message": "Hello World", "count": count, "test": database.test}
