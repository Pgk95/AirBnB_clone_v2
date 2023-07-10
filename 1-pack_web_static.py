#!/usr/bin/python3
"""
a Fabric script that creats an archive file from a "webstatic" folder
"""
from fabric.api import local
from time import strftime


def do_pack():
    """generate a .tgz archive"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        archname = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(archname))
        return archname
    except:
        return None
