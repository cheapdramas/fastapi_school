from db.pg.connect import async_connect
from psycopg.rows import dict_row

class TeacherQueries:

	@staticmethod
	async def get_teacher_school(teacher_id:int) -> int|None:
		async with await async_connect() as connect:
			query = """
				SELECT *  FROM schools WHERE 
					id = (SELECT school_id FROM classes WHERE 
								id= (SELECT class_id FROM teachers WHERE id=%s)
					) 
			"""
			cursor = connect.cursor(row_factory=dict_row)
			
			await  cursor.execute(query=query,params=(teacher_id,))
			school_info  :	dict|None= await cursor.fetchone()

			return school_info			

	@staticmethod
	async def get_teacher_class(teacher_id:int) -> dict|None:
		async with await async_connect() as connect:

			
			query = """SELECT * FROM classes WHERE id=(SELECT class_id FROM teachers WHERE id=%s)"""
			cursor = connect.cursor(row_factory=dict_row)

			

			await cursor.execute(query,(teacher_id,))

			class_info :dict|None = await cursor.fetchone()			
			
			return class_info
	
	@staticmethod
	async def get_all_students_for_teacher(teacher_id:int)->list|None:
		async with await async_connect() as connect:

			query = """
				SELECT * FROM students WHERE class_id = (SELECT class_id FROM teachers WHERE id = %s)
			"""
			cursor = connect.cursor(row_factory=dict_row)
			await cursor.execute(query,(teacher_id,))

			result = await cursor.fetchall()

			return result
		
	
		



class SchoolsQueries:

	@staticmethod
	async def get_all_teachers_from_school(school_id:int) -> list|None:
		async with await async_connect() as connect:

			query = """
			SELECT * FROM teachers WHERE class_id IN (SELECT id FROM classes WHERE school_id = %s)
			"""

			cursor = connect.cursor(row_factory=dict_row)

			await cursor.execute(query,(school_id,))

			teachers = await cursor.fetchall()
			if teachers ==[]:
				return None
			
			return teachers
			
		
	

	
