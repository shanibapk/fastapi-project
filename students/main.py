from fastapi import FastAPI
from.import models
from . database import engine
from . routers import student,authentication,password_reset



app=FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(student.router)
app.include_router(password_reset.router)
 

