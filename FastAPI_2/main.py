from fastapi import FastAPI, Path,Query, HTTPException
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

#path params
@app.get("/view/{patient_id}")
def view_patient_by_id(patient_id:str = Path(..., description='ID of the patient in the DB',example='P001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='patient not found')

#query params
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basisof height, weight or BMI'), order:str = Query('asc',description='sort in asc or desc order') ):
    
    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail=f'Invalid field')

    data = load_data()
    

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data