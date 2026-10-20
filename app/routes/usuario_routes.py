
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError, OperationalError

from entidades.models import Usuario
from dependencies.dependencies import database

from controllers.Usuario_controller import (
    inserir_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    deletar_usuario,
)

usuario_router = APIRouter()


@usuario_router.post("/usuarios", status_code=201)
def cadastrar_usuario(
    usuario: Usuario,
    db: Session = Depends(database.get_db)
):
    try:
        return inserir_usuario(usuario, db)

    except IntegrityError as e:
        raise HTTPException(
            status_code=409,
            detail="CPF ou e-mail já cadastrado, ou registro incompatível."
        ) from e

    except OperationalError as e:
        raise HTTPException(
            status_code=500,
            detail="Falha na conexão com o banco de dados."
        ) from e


@usuario_router.get("/usuarios")
def listar_todos_usuarios(
    db: Session = Depends(database.get_db)
):
    try:
        return listar_usuarios(db)

    except OperationalError as e:
        raise HTTPException(
            status_code=500,
            detail="Falha ao consultar o banco de dados."
        ) from e


@usuario_router.get("/usuarios/{id_usuario}")
def consultar_usuario(
    id_usuario: int,
    db: Session = Depends(database.get_db)
):
    usuario = buscar_usuario(id_usuario, db)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return usuario


@usuario_router.put("/usuarios/{id_usuario}")
def editar_usuario(
    id_usuario: int,
    dados: Usuario,
    db: Session = Depends(database.get_db)
):
    try:
        usuario = atualizar_usuario(id_usuario, dados, db)

    except IntegrityError as e:
        raise HTTPException(
            status_code=409,
            detail="CPF ou e-mail já cadastrado, ou registro incompatível."
        ) from e

    except OperationalError as e:
        raise HTTPException(
            status_code=500,
            detail="Falha na conexão com o banco de dados."
        ) from e

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return usuario


@usuario_router.delete("/usuarios/{id_usuario}")
def excluir_usuario(
    id_usuario: int,
    db: Session = Depends(database.get_db)
):
    try:
        excluido = deletar_usuario(id_usuario, db)

    except IntegrityError as e:
        raise HTTPException(
            status_code=409,
            detail=(
                "Não é possível excluir este usuário "
                "porque existem registros relacionados."
            )
        ) from e

    except OperationalError as e:
        raise HTTPException(
            status_code=500,
            detail="Falha na conexão com o banco de dados."
        ) from e

    if not excluido:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return {"mensagem": "Usuário excluído com sucesso."}
