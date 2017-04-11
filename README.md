[![Code Climate](https://codeclimate.com/github/francium/microURL/badges/gpa.svg)](https://codeclimate.com/github/francium/microURL)

Requirements
===

System
---
- python3
- python3-dev
- libmysqlclient-dev
- mariadb (mysql should be supported as well)

Pip
---
- see requirements.txt

Setup
===
Note these are \*nix instructions, usage on Windows may be different. Using a
\*nix system is *highly* recommended to avoid any undue frustration.

Install requirements
---

Install system requirements

    $ apt-get install python3 python3-dev libmysqlclient-dev mariadb

Setup mariadb

    $ echo "you're on your own here for now."

Install pip requirements

    $ pip insall -r requirements.txt

Create `.config.json`
---

    {
        "user": "mysql_user",
        "password": "mysql_user's_password",
        "host": "mysql_server_ip",
        "db_name": "mysql_database"
    }

Create table
---

    $ python3 database.py create

Start
---
Debug

    $ make debug    # Run with flask debugger

Run as application

    $ make run      # Run application
