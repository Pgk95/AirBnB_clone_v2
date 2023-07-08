#!/usr/bin/python3
"""Fab file for compressing to an archive"""


from fabric2 import task
from fabric.operations import local
from datetime import datetime


@task
def do_pack(c):
    """Creates the folder (versions) if it doesn't exist"""
    c.run("mkdir -p versions")

    """Creates the archive filename using current timestamp"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(now)

    """Creates the .tgz archive using tar command"""
    local("tar -czvf versions/{} web_static".format(archive_filename))

    """Return the archive path if the archive is generated (successfullt)"""
    archive_path = "versions/{}".format(archive_filename)
    if c.run("test -f {}".format(archive_path), warn=True).failed:
        return None
    else:
        return archive_path
