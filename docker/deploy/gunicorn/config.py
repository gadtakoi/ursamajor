import multiprocessing

workers = multiprocessing.cpu_count()
bind = '0.0.0.0:10000'
accesslog = '/var/log/gunicorn-access.log'
errorlog = '/var/log/gunicorn-error.log'
syslog = True
max_requests = 2048
max_requests_jitter = 64
timeout = 120
