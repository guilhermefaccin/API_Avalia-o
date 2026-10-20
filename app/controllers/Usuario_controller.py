
from entidades.models import Usuario
from sqlmodel import Session, select
from sqlalchemy.exc import OperationalError, IntegrityError
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def gerar_hash(senha: str) -> str:
    return password_hash.hash(senha)


def usuario_publico(usuario: Usuario):
    return usuario.model_dump(exclude={"senha"})


def inserir_usuario(usuario: Usuario, db: Session):
    try:
        if usuario.senha:
            usuario.senha = gerar_hash(usuario.senha)

        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        return usuario_publico(usuario)

    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def listar_usuarios(db: Session):
    usuarios = db.exec(select(Usuario)).all()

    return [usuario_publico(usuario) for usuario in usuarios]


def buscar_usuario(id_usuario: int, db: Session):
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        return None

    return usuario_publico(usuario)


def atualizar_usuario(
    id_usuario: int,
    dados: Usuario,
    db: Session
):
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id_usuario"}
    )

    # Gera hash somente quando uma nova senha for informada
    if alteracoes.get("senha"):
        alteracoes["senha"] = gerar_hash(alteracoes["senha"])

    try:
        for campo, valor in alteracoes.items():
            setattr(usuario, campo, valor)

        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        return usuario_publico(usuario)

    except (OperationalError, IntegrityError):
        db.rollback()
        raise


def deletar_usuario(id_usuario: int, db: Session):
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        return False

    try:
        db.delete(usuario)
        db.commit()
        return True

    except (OperationalError, IntegrityError):
        db.rollback()
        raise
