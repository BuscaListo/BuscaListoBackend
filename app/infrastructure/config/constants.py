import os
from dotenv import load_dotenv
load_dotenv()

NAME_SERVICEDB = os.getenv("NAME_SERVICEDB", "sqlite")
PORTDB = os.getenv("PORTDB", "sqlite")
NAMEDB = os.getenv("NAMEDB", "sqlite")
USERDB = os.getenv("USERDB", "sqlite")
PASSWORDDB = os.getenv("PASSWORDDB", "sqlite")
DB_TYPE = os.getenv("DB_TYPE", "sqlite")

PROJECT_NAME = os.getenv("PROJECT_NAME", "My FastAPI Project")
VERSION = os.getenv("VERSION", "1.0.0")
DESCRIPTION = os.getenv("DESCRIPTION", "Generic FastAPI Boilerplate API.")
ALLOW_ORIGINS = os.getenv("CORS_ALLOW_ORIGINS", "*").split(",")

HOST=os.getenv("HOST", "0.0.0.0"),
PORT=int(os.getenv("PORT", 8000)),
RELOAD = os.getenv("RELOAD", "1") == "1",

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "database_mysql")