#!/usr/bin/python3
"""Fab file for compressing to an archive"""

import os.path
from fabric.api import task, local
from datetime import datetime

@task
def do_pack():
    """Creates the folder (versions) if it doesn't exist"""
    local("mkdir -p versions")

    """Creates the archive filename using current timestamp"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(now)

    """Creates the .tgz archive using tar command"""
    local("tar -czvf versions/{} web_static".format(archive_filename))

    """Return the archive path if the archive is generated (successfullt)"""
    archive_path = "versions/{}".format(archive_filename)
    if not os.path.isfile(archive_path):
        return None
    else:
        return archive_path
