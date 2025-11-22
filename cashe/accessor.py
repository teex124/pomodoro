import redis

from settings import Settings 


def get_redis_connection() ->  redis.Redis:
    settings = Settings()
    redis_ = redis.Redis(
        host = settings.REDIS_HOST,
        port = settings.REDIS_PORT,
        db = settings.REDIS_DB
    )
    return redis_

