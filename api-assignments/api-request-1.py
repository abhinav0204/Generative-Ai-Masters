from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a:int
    b:int

@app.post("/multiply")

def multiply(numbers: Numbers):
    result = numbers.a * numbers.b
    return {"result",result}