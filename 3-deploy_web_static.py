#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py) that \
creates and distributes an archive to your web servers, \
using the function deploy:"""

from fabric.api import *
from os import path

env.hosts = ['34.75.68.113', '54.226.84.62']

def do_deploy(archive_path):
    """Distributes an archive to your web servers,"""
    if not path.exists(archive_path):
        return (False)
    else:
        ret_value = True
    a = put(archive_path, '/tmp/')
    if a.failed:
        ret_value = False
    _file = archive_path.replace(".tgz").replace("/versions/", "")
    b = run('mkdir -p /data/web_static/releases/' + _file + '/')
    if b.failed:
        ret_value = False
    c = run('tar -xzt tmp' + '.tgz' +
            '-C /data/web_static/releases/' + _file + '/')
    if c.failed:
        ret_value = False
    d = run('rm /tmp/' + _file + '.tgz')
    if d.failed:
        ret_value = False
    e = run('mv /data/web_static/releases' +_file +
            '/web_static/* /data/web_static/releases/' + _file + '/web_static')
    if e.failed:
        ret_value = False
    f = run('rm -r -f /data/web_static/releases' + _file + '/web_static')
    if f.failed:
        ret_value = False
    g = run('rm -r -f /data/web_static/current')
    if g.failed:
        ret_value = False
    h = run('ln -sf /data/web_static/releases' + _file + '/' +
            '/data/web_static/current')
    if h.failed:
        ret_value = False
    return (ret_value)
