from fastapi import APIRouter
from models import models_school 
from db.alchemy.queries import AlchSchoolsQueries  
from db.pg.queries import SchoolsQueries 
from fastapi import HTTPException,status


router = APIRouter(tags=['School routes'],prefix="/schools")


@router.post('/create_school')
async def create_school(school_info:models_school.SchoolModel):
    try:
        await AlchSchoolsQueries.add_school(**school_info.dict())

    except Exception as ex:
        print(ex)
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=str(ex))
    
    return 'no troubles ))'

@router.get('/schools_short_info')
async def schools_short_info():
    return await AlchSchoolsQueries.all_schools_short_info()


@router.get('/school_info')
async def get_school_info_route(school_id:int):
    school_info = await AlchSchoolsQueries.get_school_info(school_id)

    return school_info
