web: flask db upgrade; flask translate compile; gunicorn microblog:app_module
worker: rq worker -u $REDIS_URL microblog-tasks