#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """Fabric script that generates a .tgz archive
    from the contents of the web_static folder
    of your AirBnB Clone repo,
    using the function do_pack. """
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'web_static_{today}.tgz'

    folder_version = exists("versions")
    if folder_version is False:
        local('mkdir -p versions')
    try:
        local("tar -cvzf versions/{} web_static".format(file_name))
        return file_name
    except:
        return None
