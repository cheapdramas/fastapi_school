from pydantic import BaseModel,EmailStr,Field
from random import randint
from typing import Annotated,Optional



class TeachersModel(BaseModel):
	
	first_name: Annotated[str,Field(max_length=20)]
	second_name:Annotated[str,Field(max_length=30)]
	lesson:Annotated[str,Field(max_length=30)]
	class_id: Annotated[int,Field(gt=0)] = None
  


    



    

