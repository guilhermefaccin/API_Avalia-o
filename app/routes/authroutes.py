from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from dependencies.dependencies import database
from entidades.models import Usuariologin
from controllers.Equipamento_controller import Authcontroller

auth_router = APIRouter

@auth_router.post("/auth/login")
def usuario_login(credenciais:Usuariologin,db:Session = Depends(database.get_db)):
    try:
        token= Authcontroller.fazer_login(db,credenciais.email,credenciais.senha)
        return token
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))