from fastapi import APIRouter
from models.models_class import ClassModel
from db.alchemy.queries import AlchClassesQueries
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError
from typing import Annotated
from pydantic import Field









router = APIRouter(tags=['Classes routes'],prefix='/classes')

@router.post('/create_class')
async def create_class(classInfo:ClassModel):
	try:
		await AlchClassesQueries.add_class(**classInfo.dict())
	
	except Exception as ex:
		raise HTTPException(status.HTTP_409_CONFLICT,detail=str(ex))

	return 'successfull'

@router.get('/classes')
async def get_classes_route():

		return await AlchClassesQueries.get_classes()

@router.get('/class_info')
async def get_class_info_route(class_id:Annotated[int,Field(gt=0)]):
	class_info = await AlchClassesQueries.get_class_info(class_id=class_id)

	return class_info





