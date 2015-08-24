# coding: utf-8
from bottle import static_file
from bottle import get, request, response


@get('/')
def index():
    return static_file('index.html', root='./dist')


@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./dist')
