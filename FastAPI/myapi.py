from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1:{
        "name":"John",
        "age": 20,
        "class_": "A"
    }
}

subjects = {
    1:{
        "name":"Math",
        "teacher": "Mr. Smith"
    },
    2:{
        "name":"Science",
        "teacher": "Ms. Johnson"
    }
}


class Student(BaseModel):
    name:str
    age:int
    class_:str

class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    class_:Optional[str] = None

#GET method

@app.get("/")
def index():
    return {"name":"First DATA"}


#query params
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(..., description="TheID of the student you  want to view",gt=0,lt=3)):
    return students[student_id]


@app.get("/get-subject/{subject_id}")
def get_subject(subject_id:int = Path(..., description="TheID of the subject you  want to view",gt=0,lt=3)):
    return subjects[subject_id]

#optional params
@app.get("/get-student-by-name")
def get_student_by_name(*,name: Optional[str] = None,test:int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}

#combining query and path params
@app.get("/get-subject-by-name/{subject_id}")
def get_subject_by_name(*,subject_id:int,name: Optional[str] = None,test:int):
    for subject_id in subjects:
        if subjects[subject_id]["name"] == name:
            return subjects[subject_id]
    return {"Data":"Not Found"}


#Request body and the POST method
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return{"Error","Student exists"}
    students[student_id] = student
    return students[student_id] 


#PUT method
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error","Student does not exist"}
    
    if student.age != None:
        students[student_id].age = student.age

    if student.class_ != None:
        students[student_id].class_ = student.class_
    return students[student_id]


#DELETE method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"Error","Student does not exist"}
    
    del students[student_id]
    return {"Message":"Student deleted successfully"}