from fastapi import Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
import database, schemas, models, JWTtoken
from hashing import Hash
#All Post Details
def register_user(request: schemas.Login,db: Session = Depends(database.get_db)):
    User = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not User:
        db_User = models.Users(username= request.username, password= Hash.bcrypt(request.password), first_name= request.first_name, last_name= request.last_name, email_id= request.email_id)
        db.add(db_User)
        db.commit()
        db.refresh(db_User)
        msg = 'User created successfully'
    else :
        msg = "Error"
        raise HTTPException(status_code = status.HTTP_302_FOUND, detail = f"{request.username} already present in database")
    return msg

def login_user(request: schemas.Login,db: Session = Depends(database.get_db)):
    User = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")
    if not Hash.verify(request.password, User.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    access_token = JWTtoken.create_access_token(data={"sub": User.username})
    return {"access_token": access_token, "token_type": "bearer"}


def change_password(id: int, request: schemas.ChangePassword, db: Session):
    user = db.query(models.Users).filter(models.Users.id == id)
    if not user.first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found") 
    db.query(models.Users).filter(models.Users.id == id).update({models.Users.password: Hash.bcrypt(request.password)})
    db.commit()
    return "Password Changed"

def verify_emailid(mailid: str, verifycode: str, db: Session):
    User = db.query(models.Users).filter(models.Users.email_id == mailid).first()
    if not User:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f" {mailid} User not found")
    if not verifycode == User.email_verify_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Verification Code is Worng")
    db.query(models.Users).filter(models.Users.id == User.id).update({models.Users.email_verify: "1"})
    db.commit()
    return "Email Verifyed"  