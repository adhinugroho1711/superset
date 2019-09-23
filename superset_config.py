import os
from werkzeug.contrib.cache import RedisCache
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
REDIS_SERVER_IP = os.getenv('localhost', '')
REDIS_PASSWORD = os.getenv('password', '')
POSTGRES_SERVER_IP = os.getenv('192.168.64.7', '')
POSTGRES_USER = 'postgresadmin'
POSTGRES_PASSWORD = os.getenv('admin123', '')
SUPERSET_CACHE_REDIS_URL = "".join(['redis://:', REDIS_PASSWORD, '@', REDIS_SERVER_IP, ':6379/1'])
SUPERSET_BROKER_URL = "".join(['redis://:', REDIS_PASSWORD, '@', REDIS_SERVER_IP, ':6379/0'])
SUPERSET_CELERY_RESULT_BACKEND = "".join(['redis://:', REDIS_PASSWORD, '@', REDIS_SERVER_IP, ':6379/0'])
SUPERSET_SQLALCHEMY_DATABASE_URI = "".join(['postgresql+psycopg2://', POSTGRES_USER, ':', POSTGRES_PASSWORD, '@', POSTGRES_SERVER_IP, ':31937/supersetdb'])
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': SUPERSET_CACHE_REDIS_URL
}
SQLALCHEMY_DATABASE_URI = SUPERSET_SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'
class CeleryConfig(object):
    BROKER_URL = SUPERSET_BROKER_URL
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = SUPERSET_CELERY_RESULT_BACKEND
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host=REDIS_SERVER_IP,
    port=6379,
    key_prefix='superset_results',
    password=REDIS_PASSWORD
)
