from entidades.models import estoqueequipamentos
from sqlmodel import Session

def insert_categoria(categoria:estoqueequipamentos,db:Session):
    categoria_insert = estoqueequipamentos.model_validate(categoria)
    db.add(categoria_insert)
    db.commit()
    db.refresh(categoria_insert)
    return categoria_insert