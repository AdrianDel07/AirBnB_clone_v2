#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py) \
that distributes an archive to your web servers, \
using the function do_deploy"""

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['34.75.68.113', '54.226.84.62']


def do_deploy(archive_path):
    """Deploys archive"""
    if not path.exists(archive_path):
        return False
    ret_value = True
    a = put(archive_path, '/tmp/')
    if a.failed:
        ret_value = False
    arch = archive_path.replace(".tgz", "").replace("versions/", "")
    b = run('mkdir -p /data/web_static/releases/' + arch + '/')
    if b.failed:
        ret_value = False
    c = run('tar -xzf /tmp/' + arch + '.tgz' +
            ' -C /data/web_static/releases/' + arch + '/')
    if c.failed:
        ret_value = False
    d = run('rm /tmp/' + arch + '.tgz')
    if d.failed:
        ret_value = False
    e = run('mv /data/web_static/releases/' + arch +
            '/web_static/* /data/web_static/releases/' + arch + '/')
    if e.failed:
        ret_value = False
    f = run('rm -rf /data/web_static/releases/' + arch + '/web_static')
    if f.failed:
        ret_value = False
    g = run('rm -rf /data/web_static/current')
    if g.failed:
        ret_value = False
    h = run('ln -sf /data/web_static/releases/' + arch +
            '/' + ' /data/web_static/current')
    if h.failed:
        ret_value = False
    if ret_value:
        print("All tasks succeeded!")
    return ret_value
