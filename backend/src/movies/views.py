from django.shortcuts import render
import redis

def index(request):
    db = get_redis_db()
    count = get_latest_count(db) + 1
    save(db, "count", count)

    return render(request, 'count.html', {"count": count})

def get_redis_db():
    return redis.Redis(host='fullstackapp_redis_1', port=6379, decode_responses=True)

def get_latest_count(db):
    return parseInt(db.get("count"), 0)

def save(db, key, value):
    db.set(key, value)

def parseInt(valueStr, defaultValue):
    try:
        return int(valueStr)
    except:
        return defaultValue