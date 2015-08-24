 # coding: utf-8
from fabric.api import *
from fabric.colors import *
from fabric.utils import abort
from fabric.contrib.console import confirm

from fab_scripts.fabfile_heroku import *


@task
def npm():
    local('brew install npm')
    local('sudo npm install -g bower')
    local('sudo npm install -g vulcanize')
    local('sudo npm install -g yo')
    local('sudo npm install -g generator-polymer')
    local('sudo npm install -g gulp')

@task
def bootstrap():
    local('npm install')
    local('bower install')

@task
def bower():
    local('bower prune')
    local('bower install')
    local('bower update')

@task
def build():
    local('gulp')

@task
def server():
    local('gulp')
    start_server()

@task
def dev_server():
    local('gulp clean')
    local('gulp serve')

@task
def prod_server():
    local('gulp clean')
    local('gulp serve:dist')

@task
def pre_deploy():
    bower()
    local('gulp')
    with quiet():
        local('git add dist/')
        local('git commit -m "[deploy]"')

@task
def heroku_deploy():
    pre_deploy()
    deploy()
