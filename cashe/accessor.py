import redis 


def get_redis_connection() ->  redis.Redis:
    redis_ = redis.Redis(
        host = 'localhost',
        port = 6379,
        db = 0
    )
    return redis_

