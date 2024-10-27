import sqlalchemy
from conf.env_parser import env_variables
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import asyncpg
import psycopg

DSN=f"postgresql+asyncpg://{env_variables['USER']}:{env_variables['PASSWORD']}@{env_variables['HOST']}:{env_variables['PORT']}/schools"

DSN_SYNC = f"postgresql+psycopg://{env_variables['USER']}:{env_variables['PASSWORD']}@{env_variables['HOST']}:{env_variables['PORT']}/schools"

engine=create_async_engine(url=DSN,echo=False)
sync_engine = sqlalchemy.create_engine(url=DSN_SYNC,echo=False)



session_factory = async_sessionmaker(engine)

sync_session_factory = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    
    def __repr__(self):
        columns = [f'{col}={getattr(self,col)}' for col in self.__table__.columns.keys()]

        return f"<{self.__class__.__name__} {','.join(columns)}>"


