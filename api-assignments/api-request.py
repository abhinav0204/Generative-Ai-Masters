from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/abhinav/suman/xyz")
def add(a:int,b:int):
    return a+b

print(add(3,4))


class SubstractModel(BaseModel):
    a:int
    b:int

def substract(a:int,b:int):
    return a-b




@app.post("/substraction")
def substractNumbers(model:SubstractModel):
    return substract(model.a,model.b)

