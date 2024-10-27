import psycopg
from conf.env_parser import env_variables
import asyncio


async def async_connect():
    connection= await psycopg.AsyncConnection.connect(
        port=env_variables['PORT'],
        password=env_variables['PASSWORD'],
        user=env_variables['USER'],
        dbname=env_variables['DBNAME']
    )
    
    return connection

def connect():
    connection= psycopg.connect(
        port=env_variables['PORT'],
        password=env_variables['PASSWORD'],
        user=env_variables['USER'],
        dbname=env_variables['DBNAME']
    )
    return connection
