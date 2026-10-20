
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from entidades.models import Equipamento
from dependencies.dependencies import database
from controllers.Equipamento_controller import (
    inserir_equipamento,
    listar_equipamentos,
    buscar_equipamento,
    atualizar_equipamento,
    deletar_equipamento
)

equipamento_rauter = APIRouter()


@equipamento_rauter.post("/equipamentos", status_code=201)
def cadastrar_equipamento(
    equipamento: Equipamento,
    db: Session = Depends(database.get_db)
):
    try:
        return inserir_equipamento(equipamento, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao cadastrar equipamento."
        ) from e


@equipamento_rauter.get("/equipamentos")
def listar_todos_equipamentos(
    db: Session = Depends(database.get_db)
):
    return listar_equipamentos(db)


@equipamento_rauter.get("/equipamentos/{id_equipamento}")
def consultar_equipamento(
    id_equipamento: int,
    db: Session = Depends(database.get_db)
):
    equipamento = buscar_equipamento(id_equipamento, db)

    if equipamento is None:
        raise HTTPException(
            status_code=404,
            detail="Equipamento não encontrado."
        )

    return equipamento


@equipamento_rauter.put("/equipamentos/{id_equipamento}")
def editar_equipamento(
    id_equipamento: int,
    dados: Equipamento,
    db: Session = Depends(database.get_db)
):
    try:
        equipamento = atualizar_equipamento(
            id_equipamento, dados, db
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao atualizar equipamento."
        ) from e

    if equipamento is None:
        raise HTTPException(
            status_code=404,
            detail="Equipamento não encontrado."
        )

    return equipamento


@equipamento_rauter.delete("/equipamentos/{id_equipamento}")
def excluir_equipamento(
    id_equipamento: int,
    db: Session = Depends(database.get_db)
):
    try:
        excluido = deletar_equipamento(id_equipamento, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao excluir equipamento."
        ) from e

    if not excluido:
        raise HTTPException(
            status_code=404,
            detail="Equipamento não encontrado."
        )

    return {"mensagem": "Equipamento excluído com sucesso."}
