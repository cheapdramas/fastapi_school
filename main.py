from fastapi import FastAPI
import uvicorn
import sys
from contextlib import asynccontextmanager
from routes import main_router
import asyncio
import db.pg.create_drop as db_queries


import pytest
import pathlib



app = FastAPI()
app.include_router(main_router)




if __name__ == '__main__':
    if '--recreate-tables' in sys.argv:
            db_queries.drop_tables()
            db_queries.create_tables()

    elif '--test' in sys.argv:
        


        pytest.main(['-s','-v','tests','--disable-warnings'])
        

    else:
        
    
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


        uvicorn.run('main:app')

