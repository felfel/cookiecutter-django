from psycogreen.gevent import patch_psycopg     # use this if you use gevent workers


def post_fork(server, worker):
    """
    This is necessary to patch
    See: https://github.com/jneight/django-db-geventpool#patch-psycopg2
    """
    patch_psycopg()
    worker.log.info("django-db-geventpool: make psycopg2 green")


workers = 3
worker_class = "gevent"
worker_connections = 500
bind = "0.0.0.0:5000"
timeout = 600
max_requests = 1000
max_requests_jitter = 4


access_log_format = '%(h)s %(l)s %({Forwarded}i)s %(l)s %(r)s %(s)s %(b)s %(f)s %(a)s'
