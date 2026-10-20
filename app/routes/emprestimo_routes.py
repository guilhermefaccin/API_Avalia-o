
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from entidades.models import Emprestimo
from dependencies.dependencies import database
from controllers.Emprestimo_controller import (
    inserir_emprestimo,
    listar_emprestimos,
    buscar_emprestimo,
    atualizar_emprestimo,
    deletar_emprestimo,
)

emprestimo_router = APIRouter()


@emprestimo_router.post("/emprestimos", status_code=201)
def cadastrar_emprestimo(
    emprestimo: Emprestimo,
    db: Session = Depends(database.get_db),
):
    try:
        return inserir_emprestimo(emprestimo, db)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        ) from e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao cadastrar empréstimo.",
        ) from e


@emprestimo_router.get("/emprestimos")
def listar_todos_emprestimos(
    db: Session = Depends(database.get_db),
):
    return listar_emprestimos(db)


@emprestimo_router.get("/emprestimos/{id_emprestimo}")
def consultar_emprestimo(
    id_emprestimo: int,
    db: Session = Depends(database.get_db),
):
    emprestimo = buscar_emprestimo(id_emprestimo, db)

    if emprestimo is None:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado.",
        )

    return emprestimo


@emprestimo_router.put("/emprestimos/{id_emprestimo}")
def editar_emprestimo(
    id_emprestimo: int,
    dados: Emprestimo,
    db: Session = Depends(database.get_db),
):
    try:
        emprestimo = atualizar_emprestimo(
            id_emprestimo, dados, db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        ) from e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao atualizar empréstimo.",
        ) from e

    if emprestimo is None:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado.",
        )

    return emprestimo


@emprestimo_router.delete("/emprestimos/{id_emprestimo}")
def excluir_emprestimo(
    id_emprestimo: int,
    db: Session = Depends(database.get_db),
):
    try:
        excluido = deletar_emprestimo(id_emprestimo, db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao excluir empréstimo.",
        ) from e

    if not excluido:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado.",
        )

    return {"mensagem": "Empréstimo excluído com sucesso."}
