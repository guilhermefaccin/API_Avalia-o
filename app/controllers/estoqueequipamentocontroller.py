
from entidades.models import estoqueequipamentos
from sqlmodel import Session, select
from sqlalchemy.exc import OperationalError, IntegrityError


def insert_categoria(categoria: estoqueequipamentos, db: Session):
    try:
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def listar_categorias(db: Session):
    return db.exec(select(estoqueequipamentos)).all()


def buscar_categoria(id_estoque: int, db: Session):
    return db.get(estoqueequipamentos, id_estoque)


def atualizar_categoria(
    id_estoque: int,
    dados: estoqueequipamentos,
    db: Session
):
    categoria = buscar_categoria(id_estoque, db)

    if categoria is None:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id_estoque"}
    )

    for campo, valor in alteracoes.items():
        setattr(categoria, campo, valor)

    try:
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def deletar_categoria(id_estoque: int, db: Session):
    categoria = buscar_categoria(id_estoque, db)

    if categoria is None:
        return False

    try:
        db.delete(categoria)
        db.commit()
        return True
    except (OperationalError, IntegrityError):
        db.rollback()
        raise
