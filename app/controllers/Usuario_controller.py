from sqlmodel import Session
from entidades.models import Usuario
from sqlalchemy.exc import OperationalError, IntegrityError

def usuario_cadastro(categoria:Usuario,db: Session):   
    try:
        usuario_cadastro = Usuario.model_validate(categoria)
        db.add(usuario_cadastro)
        db.commit()
        db.refresh(usuario_cadastro)
        return usuario_cadastro
    except OperationalError as e:
        print (f"->> {e}")
        raise RuntimeError("Falha na conecção com o Bando de Dados") from e
    except IntegrityError as e:
        raise ValueError("Verifique o erro de Integridade")