import redis 


r = redis.Redis(host='localhost', port=6379, db=0)

r.set('user:4:name', 'John Djjokke')
