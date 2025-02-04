
import redis
from redis import ConnectionPool
import threading

pool = ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=10,
    socket_connect_timeout=3,
    socket_keepalive=True
)
r = redis.Redis(connection_pool=pool)
def worker(n):
    r = redis.Redis(connection_pool=pool)
    # Perform Redis operations with 'r'
    r.set('user:{n}:name', 'John Doe'+str(n))
    r.set('user:{n}:email', '{n}joe@h3hitema.zouloulou')

    user_name = r.get('user:{n}:name')
    user_email = r.get('user:{n}:email')
    print(user_name, user_email)

threads = [threading.Thread(target=worker(i)) for i in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()