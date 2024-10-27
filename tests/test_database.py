import pytest
from db.alchemy import database as db_alchemy
import db.pg as pg
from db.alchemy import orms
from sqlalchemy import text,select
from sqlalchemy.orm import joinedload,selectinload
from db.pg.connect import connect,async_connect



class TestAlchTeacher:
	def test_teacher_relationship(*args):
		with db_alchemy.sync_session_factory() as session:
			query = select(orms.TeachersOrm).options(joinedload(orms.TeachersOrm.teacher_class))  #ONE TO ONE relationship

			res = session.execute(query)
			result = res.scalars().all()

			print(result[0].teacher_class)

	def test_class_students_teachers(*args):
		with db_alchemy.sync_session_factory() as session:

			query = select(orms.ClassOrm).options(joinedload(orms.ClassOrm.teacher)).options(selectinload(orms.ClassOrm.students))


			res = session.execute(query)
			result = res.scalars().all()

			print(result[0])

	async def async_test_class_students_teachers():
		async with db_alchemy.async_sessionmaker() as session:

			query = select(orms.ClassOrm).options(joinedload(orms.ClassOrm.teacher)).options(selectinload(orms.ClassOrm.students))


			res = await session.execute(query)
			result = res.scalars().all()

			print(result[0])

