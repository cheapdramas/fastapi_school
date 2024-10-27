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




@router.get('/all_teachers_school')
async def get_all_teachers_school_route(school_id:int):
    all_teachers =await SchoolsQueries.get_all_teachers_from_school(school_id=school_id)
    return all_teachers
