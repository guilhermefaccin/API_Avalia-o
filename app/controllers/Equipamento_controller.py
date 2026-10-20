
from entidades.models import Equipamento
from sqlmodel import Session, select
from sqlalchemy.exc import OperationalError, IntegrityError


def inserir_equipamento(equipamento: Equipamento, db: Session):
    try:
        db.add(equipamento)
        db.commit()
        db.refresh(equipamento)
        return equipamento
    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def listar_equipamentos(db: Session):
    return db.exec(select(Equipamento)).all()


def buscar_equipamento(id_equipamento: int, db: Session):
    return db.get(Equipamento, id_equipamento)


def atualizar_equipamento(
    id_equipamento: int,
    dados: Equipamento,
    db: Session
):
    equipamento = buscar_equipamento(id_equipamento, db)

    if equipamento is None:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id_equipamento"}
    )

    for campo, valor in alteracoes.items():
        setattr(equipamento, campo, valor)

    try:
        db.add(equipamento)
        db.commit()
        db.refresh(equipamento)
        return equipamento
    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def deletar_equipamento(id_equipamento: int, db: Session):
    equipamento = buscar_equipamento(id_equipamento, db)

    if equipamento is None:
        return False

    try:
        db.delete(equipamento)
        db.commit()
        return True
    except (OperationalError, IntegrityError):
        db.rollback()
        raise
