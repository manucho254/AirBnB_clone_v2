#!/usr/bin/python3
""" script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ script that generates a .tgz archive from the contents.
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
    except Exception as e:
        return
