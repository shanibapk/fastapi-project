
from sqlalchemy.orm import Session
from .. import models,schemas
from .. hashing import Hash
from fastapi import HTTPException,status



def get_all_user(db:Session):
    users=db.query(models.User).all()
    return users

# def create_user(request:schemas.User_student,db:Session):
#     new_student_user=models.User(name=request.name,
#                                  email=request.email,
#                                  password=Hash.bcrypt(request.password),
#                                  confirm_password=Hash.bcrypt(request.confirm_password),
#                                  age=request.age,
#                                  department=request.department)
#     db.add(new_student_user)
#     db.commit()
#     db.refresh(new_student_user)
#     return new_student_user


def create_user(request: schemas.User_student, db: Session):
    # Check if the password and confirm_password match
    if request.password != request.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and confirm_password do not match",
        )

    # Hash both the password and confirm_password
    hashed_password = Hash.bcrypt(request.password)

    new_student_user = models.User(
        name=request.name,
        email=request.email,
        password=hashed_password,
        confirm_password=hashed_password,  # Using the same hash for both passwords
        age=request.age,
        department=request.department,
    )

    db.add(new_student_user)
    db.commit()
    db.refresh(new_student_user)
    return new_student_user



def show(id:int,db:Session):
    get_result=db.query(models.User).filter(models.User.id==id).first()
    if not get_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
        # Response.status_code=status.HTTP_404_NOT_FOUND
        # return{'detail':f'User with the id {id} is not available'}
    return get_result