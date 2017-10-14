[![Code Climate](https://codeclimate.com/github/francium/microURL/badges/gpa.svg)](https://codeclimate.com/github/francium/microURL)

# micro url

URL shortener written in Python + Flask

Requirements: Python 3, Pip and mariadb (mysql should be supported as well)

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed.
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/).

```
$ sudo pip install virtualenv
```

3. Create a virtual environment venv and specify the Python version to use.

```
$ virtualenv venv -p python3
$ source venv/bin/activate
```

4. Install requirements.

```
$ pip install -r requirements.txt
```

## Database Configuration

MariaDB or MySQL is required for the rest of the steps.

Create `.config.json`

```
{
    "user": "mysql_user",
    "password": "mysql_user's_password",
    "host": "mysql_server_ip",
    "db_name": "mysql_database"
}
```

Create table

```
$ python3 database.py create
```

## Running

Debug

```
$ make debug    # Run with flask debugger
```

Run as application

```
$ make run      # Run application
```
