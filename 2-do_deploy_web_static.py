#!/usr/bin/python3
""" script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""
from fabric.api import local

from os import path

env.hosts = ["52.204.99.18", "34.232.78.67"]


def do_deploy(archive_path) -> bool:
    """ Fabric script (based on the file 1-pack_web_static.py)
        that distributes an archive to your web servers,
        using the function do_deploy.

        Args:
             archive_path: path to an archive file
        Return: True or False
    """
    # check if archive path exists
    if not path.exists(archive_path):
        return False

    try:
        tmp_archive = "/tmp/{}".format(archive_path)
        releases = "/data/web_static/releases/"
        archive_name = tmp_archive.split()[0]
        current = "/data/web_static/current"

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_archive)
        """ create directory
           /data/web_static/releases/<archive filename without extension>
        """
        run("sudo mkdir -p {}{}".format(releases, archive_name))
        """ Uncompress the archive to the folder
            /data/web_static/releases/<archive filename without extension>
            on the web server.
        """
        run("sudo tar -xvf {} -C {}".format(tmp_archive, releases))
        # Delete the archive from the web server
        run("sudo rm -rf {}".format(tmp_archive))
        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")
        """ Create a new the symbolic link /data/web_static/current
            on the web server, linked to the new version of your code
            (/data/web_static/releases/<archive filename without extension>
        """
        run("sudo ln -s {} {}".format(releases, current))

        return True
    except Exception as e:
        return False
