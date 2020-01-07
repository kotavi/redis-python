from redis import Redis

my_redis = Redis(host='127.0.0.1', port=6379, db=0)
my_redis.set("cat", "Kaptain")
my_redis.get("cat")