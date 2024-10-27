from fastapi import APIRouter,HTTPException,status
from models.models_student import StudentModel
from db.alchemy.queries import AlchAStudentsQueries


router = APIRouter(tags=['Students routes'],prefix='/students')


@router.post('/create_student')
async def create_student(student_info:StudentModel):
	try:
		await AlchAStudentsQueries.create_student(**student_info.dict())

		return 'Success!'
	except Exception as ex:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(ex))




