from fastapi import APIRouter,Depends,status,HTTPException,Response
from..import database,models,schemas,oauth2
from sqlalchemy.orm import Session
from .. hashing import Hash
from .. repository import student_user
# from oauth2 import get_current_user
get_db=database.get_db
router=APIRouter()



@router.get('/')
def get_all(db: Session=Depends(get_db),current_user:schemas.show_user=Depends(oauth2.get_current_user)):
    return student_user.get_all_user(db)
    # users=db.query(models.User).all()
    # return users

 

@router.post('/User',status_code=status.HTTP_201_CREATED)
def create(request:schemas.User_student,db:Session=Depends(get_db),current_user:schemas.show_user=Depends(oauth2.get_current_user)):
    return student_user.create_user(request,db)
    # new_student_user=models.User(name=request.name,
    #                              email=request.email,
    #                              password=Hash.bcrypt(request.password),
    #                              age=request.age,
    #                              department=request.department)
    # db.add(new_student_user)
    # db.commit()
    # db.refresh(new_student_user)
    # return new_student_user



@router.get('/user{id}',response_model=schemas.show_user,status_code=200)
def show_student_user(id:int,db: Session=Depends(database.get_db),current_user:schemas.show_user=Depends(oauth2.get_current_user)):
    return student_user.show(id,db)
    # get_user=db.query(models.User).filter(models.User.id==id).first()
    # if not get_user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'User with the id {id} is not available')
    #     # Response.status_code=status.HTTP_404_NOT_FOUND
    #     # return{'detail':f'User with the id {id} is not available'}
    # return get_user