
from entidades.models import (
    Emprestimo,
    Usuario,
    Equipamento,
    estoqueequipamentos,
)
from sqlmodel import Session, select
from sqlalchemy.exc import OperationalError, IntegrityError


def inserir_emprestimo(emprestimo: Emprestimo, db: Session):
    try:
        # Verifica se o usuário existe
        if db.get(Usuario, emprestimo.id_usuario) is None:
            raise ValueError("Usuário não encontrado.")

        # Verifica se o equipamento existe
        if db.get(Equipamento, emprestimo.id_equipamento) is None:
            raise ValueError("Equipamento não encontrado.")

        # Verifica se o estoque existe
        if db.get(estoqueequipamentos, emprestimo.id_estoque) is None:
            raise ValueError("Estoque não encontrado.")

        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)
        return emprestimo

    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def listar_emprestimos(db: Session):
    return db.exec(select(Emprestimo)).all()


def buscar_emprestimo(id_emprestimo: int, db: Session):
    return db.get(Emprestimo, id_emprestimo)


def atualizar_emprestimo(
    id_emprestimo: int,
    dados: Emprestimo,
    db: Session,
):
    emprestimo = buscar_emprestimo(id_emprestimo, db)

    if emprestimo is None:
        return None

    # Valida os relacionamentos, se forem alterados
    if db.get(Usuario, dados.id_usuario) is None:
        raise ValueError("Usuário não encontrado.")

    if db.get(Equipamento, dados.id_equipamento) is None:
        raise ValueError("Equipamento não encontrado.")

    if db.get(estoqueequipamentos, dados.id_estoque) is None:
        raise ValueError("Estoque não encontrado.")

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id_emprestimo"},
    )

    try:
        for campo, valor in alteracoes.items():
            setattr(emprestimo, campo, valor)

        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)
        return emprestimo

    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def deletar_emprestimo(id_emprestimo: int, db: Session):
    emprestimo = buscar_emprestimo(id_emprestimo, db)

    if emprestimo is None:
        return False

    try:
        db.delete(emprestimo)
        db.commit()
        return True

    except (OperationalError, IntegrityError):
        db.rollback()
        raise
