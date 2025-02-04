import redis 


r = redis.Redis(host='my-redis', port=6379, db=0)

r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')