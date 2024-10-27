from pydantic import BaseModel,EmailStr,Field
from random import randint
from models.models_dependencies import SchoolModelDependencies
from typing import Annotated,Optional


    


class SchoolModel(BaseModel):
    full_name:str
    short_name:str
    email:EmailStr
    director:str
    town:str = 'М.Гайсин'
    


    



    

