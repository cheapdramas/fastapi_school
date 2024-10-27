from pydantic import BaseModel,Field
from typing import Annotated
from datetime import date
from pydantic.functional_validators import AfterValidator
from models.models_dependencies import StudentsModelDependencies
from models.models_dependencies import check_name

age_type = Annotated[date,AfterValidator(StudentsModelDependencies.check_age)]

name_type = Annotated[str,AfterValidator(check_name)]




class StudentModel(BaseModel):
	
	first_name: Annotated[name_type,Field(max_length=20)] = 'Анатолій'
	second_name:Annotated[name_type,Field(max_length=30)] ='Римар'
	birthday:age_type = date(2009,11,9)
	class_id:Annotated[int,Field(gt=0)]
	