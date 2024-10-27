from pydantic import BaseModel,EmailStr,Field
import enum
from random import randint
from models.models_dependencies import SchoolModelDependencies
from typing import Annotated,Optional
from models.models_teachers import TeachersModel
from models.models_student import StudentModel
from pydantic.functional_validators import AfterValidator
from fastapi import HTTPException,status
from models.models_dependencies import ClassesModelDependencies

nameType=Annotated[str,AfterValidator(ClassesModelDependencies.checkName)]


class ClassModel(BaseModel):
	name:nameType = '1-А'
	school_id:Annotated[int,Field(gt=0)] = 1 







    



    

