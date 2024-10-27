from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from datetime import date

import db.alchemy.database as db



class SchoolOrm(db.Base):
	__tablename__ ='schools'

	
	full_name:Mapped[str]
	short_name:Mapped[str]
	email:Mapped[str]
	director:Mapped[str]
	town:Mapped[str]

	id:Mapped[int] = mapped_column(primary_key=True,default='schools')


class ClassOrm(db.Base):
	__tablename__='classes'

	
	name:Mapped[str]
	school_id: Mapped[int] = mapped_column(ForeignKey('schools.id'))


	id:Mapped[int]=mapped_column(primary_key=True)

	teacher:Mapped["TeachersOrm"] = relationship()

	students: Mapped[list["StudentOrm"]] = relationship()
	school:Mapped["SchoolOrm"] = relationship()

class TeachersOrm(db.Base):
	__tablename__ = 'teachers'

	
	first_name:Mapped[str] 
	second_name:Mapped[str]
	lesson:Mapped[str]
	class_id: Mapped[int] = mapped_column(ForeignKey('classes.id'))
	
	id:Mapped[int] = mapped_column(primary_key=True)

	teacher_class:Mapped["ClassOrm"] = relationship()
	
	
	
class StudentOrm(db.Base):
	__tablename__ ='students'

	first_name:Mapped[str]
	second_name: Mapped[str]
	birthday:Mapped[date]
	class_id: Mapped[int] = mapped_column(ForeignKey('classes.id'))

	id:Mapped[int] = mapped_column(primary_key=True)


	student_class :Mapped["ClassOrm"]=relationship()