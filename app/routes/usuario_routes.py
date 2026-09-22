from fastapi import APIRouter , Depends , HTTPException, status
from sqlmodel import Session
from dependencies.dependencies import database
from controllers.Usuario_controller import usuario_cadastro
from entidades.models import Usuario

usuario_router = APIRouter()

@usuario_router.post("/usuario")
def usuario_cadastrorouter(usuario : Usuario, db:Session = Depends(database.get_db)):
    try:
        usuario_cadastro(usuario,db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))