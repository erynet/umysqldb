import sys
import pymysql
from pymysql import *
from pymysql import DATETIME
from pymysql import __all__

from .util import setdocstring

__all__ += ['DATETIME']

# for pyMySQL>=0.75 compatibility
paramstyle = "format"

@setdocstring(pymysql.Binary)
def Binary(x, encoding="utf8"):
    return bytearray(x, encoding)
    
@setdocstring(pymysql.Connect)
def Connect(*args, **kwargs):
    from .connections import Connection
    return Connection(*args, **kwargs)


def thread_safe():
    return True  # match MySQLdb.thread_safe()


def install_as_MySQLdb():
    """
    After this function is called, any application that imports MySQLdb or
    _mysql will unwittingly actually use umysqldb.
    """
    sys.modules["MySQLdb"] = sys.modules["_mysql"] = sys.modules["umysqldb"]
    sys.modules["MySQLdb.constants"] = sys.modules["pymysql.constants"]


connect = Connection = Connect
