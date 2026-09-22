from sqlmodel import Session
from entidades.models import Equipamento
from sqlalchemy.exc import OperationalError, IntegrityError

def cadastrar_equipamento(categoria:Equipamento,db: Session):   
    try:
        categoria_casdastro = Equipamento.model_validate(categoria)
        db.add(categoria_casdastro)
        db.commit()
        db.refresh(categoria_casdastro)
        return categoria_casdastro
    except OperationalError as e:
        raise RuntimeError("Falha na conecção com o Bando de Dados") from e
    except IntegrityError as e:
        raise ValueError("Verifique o erro de Integridade")