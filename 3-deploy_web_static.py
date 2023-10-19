#!/usr/bin/python3
""" script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""
from fabric.api import env, run, local, put

from os import path
from datetime import datetime
import sys

env.hosts = ["52.204.99.18", "34.232.78.67"]
env.user = "ubuntu"


def do_pack():
    """ script that generates a .tgz archive from the contents.
        Return: path to archive or None
    """
    try:
        current_date = datetime.now()
        file_name = "versions/web_static_{}{}{}{}{}{}.tgz"\
                    .format(current_date.year,
                            current_date.month,
                            current_date.day,
                            current_date.hour,
                            current_date.minute,
                            current_date.second)

        local(f"mkdir -p versions")
        local(f"tar -czvf {file_name} web_static")
        return file_name
    except Exception as e:
        return


def do_deploy(archive_path) -> bool:
    """ Fabric script (based on the file 1-pack_web_static.py)
        that distributes an archive to your web servers,
        using the function do_deploy.
        Args:
             archive_path: path to an archive file
        Return: True or False
    """
    # check if archive path exists

    if archive_path is None or not path.exists(archive_path):
        return False

    try:
        tmp_archive = "/tmp/{}".format(archive_path.split("/")[1])
        releases = "/data/web_static/releases/"
        archive_name = archive_path.split("/")[1].split(".")[0]
        current = "/data/web_static/current"
        full_path = "{}{}/".format(releases, archive_name)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_archive)

        """ create directory
           /data/web_static/releases/<archive filename without extension>
        """
        run("sudo mkdir -p {}".format(full_path))

        """ Uncompress the archive to the folder
            /data/web_static/releases/<archive filename without extension>
            on the web server.
        """
        run("sudo tar -xzf {} -C {}".format(tmp_archive,
                                            full_path))

        # Delete the archive from the web server
        run("sudo rm -rf {}".format(tmp_archive))

        run("sudo mv {}web_static/* {}".format(full_path, full_path))
        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")
        """ Create a new the symbolic link /data/web_static/current
            on the web server, linked to the new version of your code
            (/data/web_static/releases/<archive filename without extension>
        """
        run("sudo ln -s {} {}".format(full_path, current))

        print("New version deployed!")

        return True
    except Exception as e:
        return False


def deploy() -> bool:
    """ Script (based on the file 2-do_deploy_web_static.py)
        that creates and distributes an archive
        to your web servers, using the function deploy.
        Return: False if it fails else return value of do_deploy
    """
    archive_file = do_pack()

    if archive_file is None:
        return False

    return do_deploy(archive_file)
