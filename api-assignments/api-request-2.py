from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email:EmailStr
    password : str = Field(min_length=8)


class UserOut(BaseModel):
    username: str
    email : EmailStr


users_db: list[UserOut] = []

@app.post("/register",response_model=UserOut)
def register(user: UserIn):
    if any(u.email == user.email for u in users_db):
        raise HTTPException(status_code=400,detail="Emails already registered")
    

    new_user = UserOut(username = user.username, email = user.email)
    users_db.append(new_user)
    return new_user

@app.get("/users",response_model=list[UserOut])

def list_users():
    return users_db
