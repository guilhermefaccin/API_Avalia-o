from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from dependencies.dependencies import database
from entidades.models import Emprestimo
from controllers.Emprestimo_controller import cadastro_emprestimo

emprestimo_router = APIRouter()

@emprestimo_router.post("/emprestimo")
def cadastroemprestimo(emprestimo : Emprestimo, db:Session = Depends(database.get_db)):
    try:
        cadastro_emprestimo(emprestimo,db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))


