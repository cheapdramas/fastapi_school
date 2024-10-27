from fastapi import APIRouter
from models.models_class import ClassModel
from db.alchemy.queries import AlchClassesQueries
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError

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
	


