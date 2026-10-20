
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from entidades.models import estoqueequipamentos
from dependencies.dependencies import database
from controllers.estoqueequipamentocontroller import (
    insert_categoria,
    listar_categorias,
    buscar_categoria,
    atualizar_categoria,
    deletar_categoria
)

estoqueequipamento_router = APIRouter()


@estoqueequipamento_router.post("/estoque", status_code=201)
def cadastrar_estoque(
    categoria: estoqueequipamentos,
    db: Session = Depends(database.get_db)
):
    try:
        return insert_categoria(categoria, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao cadastrar estoque."
        ) from e


@estoqueequipamento_router.get("/estoque")
def listar_estoques(
    db: Session = Depends(database.get_db)
):
    return listar_categorias(db)


@estoqueequipamento_router.get("/estoque/{id_estoque}")
def consultar_estoque(
    id_estoque: int,
    db: Session = Depends(database.get_db)
):
    categoria = buscar_categoria(id_estoque, db)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado."
        )

    return categoria


@estoqueequipamento_router.put("/estoque/{id_estoque}")
def editar_estoque(
    id_estoque: int,
    dados: estoqueequipamentos,
    db: Session = Depends(database.get_db)
):
    try:
        categoria = atualizar_categoria(id_estoque, dados, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao atualizar estoque."
        ) from e

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado."
        )

    return categoria


@estoqueequipamento_router.delete("/estoque/{id_estoque}")
def excluir_estoque(
    id_estoque: int,
    db: Session = Depends(database.get_db)
):
    try:
        excluido = deletar_categoria(id_estoque, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao excluir estoque."
        ) from e

    if not excluido:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado."
        )

    return {"mensagem": "Estoque excluído com sucesso."}
