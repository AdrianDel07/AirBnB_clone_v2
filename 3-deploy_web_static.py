#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py) \
that distributes an archive to your web servers, \
using the function do_deploy"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.75.68.113', '54.226.84.62']
env.user = 'ubuntu'

n = datetime.now()


def do_pack():
    """return the archive path if the archive has been correctly generated"""
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        n.year,
        n.month,
        n.day,
        n.hour,
        n.minute,
        n.second)
    local('mkdir -p versions')
    command = local("tar -cvzf " + file_name + " ./web_static")
    if command.succeeded:
        return file_name
    return None


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
    b = run('mkdir -p /data/web_static/releases/' + archv + '/')
    if b.failed:
        ret_value = False
    c = run('tar -xzt tmp' + '.tgz' +
            '-C /data/web_static/releases/' + archv + '/')
    if c.failed:
        ret_value = False
    d = run('rm /tmp/' + archv + '.tgz')
    if d.failed:
        ret_value = False
    e = run('mv /data/web_static/releases' + archv +
            '/web_static/* /data/web_static/releases/' + archv + '/web_static')
    if e.failed:
        ret_value = False
    f = run('rm -r -f /data/web_static/releases' + archv + '/web_static')
    if f.failed:
        ret_value = False
    g = run('rm -r -f /data/web_static/current')
    if g.failed:
        ret_value = False
    h = run('ln -sf /data/web_static/releases' + archv + '/' +
            '/data/web_static/current')
    if h.failed:
        ret_value = False
    return (ret_value)


def depploy():
    """Distribute to all servers"""
    archv_path = do_pack()
    if archv_path is None:
        return (False)
    return (do_deploy(archv_path))
