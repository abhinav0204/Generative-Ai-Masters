from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Literal

app = FastAPI()

class CalculationRequest(BaseModel):
    a:float
    b:float
    operation : Literal["add","subtract","multiply","divide"]

class CalculationResult(BaseModel):
    result: float

@app.post("/calculator", response_model=CalculationResult)

def calculator(request : CalculationRequest):
    a,b,op = request.a, request.b , request.operation.lower()

    if op == "add":
        return {"result":a+b}

    elif op == "subtract":
        return {"result":a-b}
    
    elif op == "multiply":
        return {"result":a*b}
    
    elif op == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return {"result":a/b}