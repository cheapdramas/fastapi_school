from fastapi import APIRouter
from models import models_teachers

from db.alchemy.queries import AlchTeachersQueries
from fastapi import HTTPException,status
from fastapi.encoders import jsonable_encoder
from db.pg.queries import TeacherQueries


router = APIRouter(tags=['Teacher routes'],prefix='/teachers')



@router.post('/create_teacher')
async def create_teacher_route(teacher_info:models_teachers.TeachersModel):
		try:
			await AlchTeachersQueries.add_teacher(**teacher_info.dict())
		except Exception as exc:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(exc))
		

@router.get('/alch_teacher')
async def get_teacher_route():
	pass


# @router.get('/teacher_school')
# async def get_teacher_school_route(id:int) -> dict|None:
# 	"""Returns school,where teacher is"""


# 	teacher_school_info:dict|None =await TeacherQueries.get_teacher_school(id) 

# 	if teacher_school_info != None:
# 		return {'school_info':teacher_school_info}

# 	return teacher_school_info #None
	

# @router.get('/teacher_class')
# async def get_class_teacher(teacher_id:int):
# 	"""Returns class, where teacher is."""
# 	class_info:dict|None =await TeacherQueries.get_teacher_class(teacher_id=teacher_id)

# 	if class_info!=None:
# 		return {'class_info':class_info}
	
# 	return class_info #None

# @router.get('/all_teacher_students')
# async def get_all_students_for_teacher(teacher_id:int):
# 		# all_students = await TeacherQueries.get_all_students_for_teacher(teacher_id)
# 		all_students = await AlchTeachersQueries.get_all_students_for_teacher(teacher_id=teacher_id)
		
# 		return all_students
# 		# if all_students != None:
# 		# 	return {'all_students': all_students}
# 		# return all_students
