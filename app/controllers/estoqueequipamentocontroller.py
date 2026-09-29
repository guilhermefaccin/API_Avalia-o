from entidades.models import estoqueequipamentos
from sqlmodel import Session
from sqlalchemy.exc import OperationalError,IntegrityError

def insert_categoria(categoria:estoqueequipamentos,db:Session):
    categoria_insert = estoqueequipamentos.model_validate(categoria)
    try:
        db.add(categoria_insert)
        db.commit()
        db.refresh(categoria_insert)
        return categoria_insert
    except OperationalError as e:
        raise RuntimeError("Falha na conecção com o Bando de Dados") from e
    except IntegrityError as e:
        raise ValueError("Verifique o erro de Integridade")