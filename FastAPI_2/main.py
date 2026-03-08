from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message":"Patients management system API"}

@app.get("about")
def about():
    return {"message":"fully functaional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def view_patient_by_id(patient_id:str):
    data = load_data()
    for i in data:
        if i.keys == patient_id:
            return i