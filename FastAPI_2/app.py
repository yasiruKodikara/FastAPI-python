from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

# import the ML model
with open('model.pkl','rb') as f:
    model = pickle.load(f)


app = FastAPI()

#pydantic model to validate incomming data
class UserInput(BaseModel):
    age:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight:Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height:Annotated[int, Field(..., gt=0, description='Height of the user')]
    income_lpa:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    smoker:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    city:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    occupation:Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]