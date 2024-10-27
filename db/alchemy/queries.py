import db.alchemy.database as db
import db.alchemy.orms as orms
import sqlalchemy
from sqlalchemy.orm import selectinload,joinedload
from sqlalchemy import func,select
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError


async def serial_id_fix(
		session,
		tableORM:db.Base,
		kwargs:dict
)-> int:
		"""
		This function for avoiding case, when our transaction fails,but serial id still inreased,
		idk how to avoid this in sql way, so
		"""
		getting_max_id =await session.execute(select(func.max(tableORM.id)))
		max_id:int|None = getting_max_id.fetchone()[0]

		if max_id == None:
			kwargs['id'] = 1
		else:
			kwargs['id'] = max_id + 1

		return kwargs




class AlchSchoolsQueries:
	@staticmethod
	async def add_school(**kwargs):
			async with db.session_factory() as session:
				
				new_kwargs_with_serial_id=await serial_id_fix(session,orms.SchoolOrm,kwargs)
				
				schoolOrm = orms.SchoolOrm(**new_kwargs_with_serial_id)
				
				
				

				session.add(schoolOrm)
				await session.commit()
		
class AlchClassesQueries:
	@staticmethod
	async def add_class(**kwargs):
		async with db.session_factory() as session:
			
			new_kwargs_with_serial_id =await serial_id_fix(session,orms.ClassOrm,kwargs)
			classOrm = orms.ClassOrm(**new_kwargs_with_serial_id)
			
			
			session.add(classOrm)
			await session.commit()


	@staticmethod
	async def get_classes():
		async with db.session_factory() as session:

			query = select(orms.ClassOrm).options(joinedload(orms.ClassOrm.teacher),selectinload(orms.ClassOrm.students),joinedload(orms.ClassOrm.school))


			res = await session.execute(query)
			result = res.scalars().all()

			return result



class AlchTeachersQueries:
	@staticmethod
	async def add_teacher(**kwargs):
		async with db.session_factory() as session:
			new_kwargs_with_serial_id = await serial_id_fix(session,orms.TeachersOrm,kwargs)

			teacherOrm = orms.TeachersOrm(**new_kwargs_with_serial_id)

			session.add(teacherOrm)
			await session.commit()
	


	@staticmethod
	async def get_teacher_w_rel(teacher_id):
		"""
		[
			{
				id:1,
				name:valera,
				class:{
					id:1,
					name:1-A
					}
				students:[
					{id:1,name:anya,class_id:1,birthday:2009-08-10},
					{id:2,name:anya,class_id:1,birthday:2009-08-10}
				]
			},
			{
				id:2,
				name:pisyun,
				class:{
					id:2,
					name:2-A
					}
				students:[
					{id:3,name:dayn,class_id:2,birthday:2009-08-10},
					{id:4,name:zhopa,class_id:2,birthday:2009-08-10}
				]
			},

		]
		"""
		with db.sync_session_factory() as session:
			query = select(orms.TeachersOrm)

			res = session.execute(query)
			result = res.scalars.all()


class AlchAStudentsQueries:
	

	@staticmethod
	async def create_student(**kwargs):
		async with db.session_factory() as session:
			
			kwargs = await serial_id_fix(session,orms.StudentOrm,kwargs)

			studentOrm = orms.StudentOrm(**kwargs)

			session.add(studentOrm)
			await session.commit()








