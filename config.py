import os
import redis

class ApplicationConfig:
    SECRET_KEY = 'helloworld'

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url('redis://127.0.0.1:6379')
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True