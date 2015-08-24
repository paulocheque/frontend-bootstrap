from bottle import request, response, install
import time

def safe_bottle(callback):
    def wrapper(*args, **kwargs):
        start = time.time()
        body = callback(*args, **kwargs)
        response.headers['Server'] = ')'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Language'] = 'pt-br'
        end = time.time()
        response.headers['X-Exec-Time'] = str(end - start)
        return body
    return wrapper

install(safe_bottle)
