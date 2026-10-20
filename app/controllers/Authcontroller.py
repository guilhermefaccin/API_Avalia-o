from entidades.models import Usuario, Usuario_Status
from sqlmodel import Session, select
from core.security import verifica_senha, criar_token
from sqlalchemy.exc import OperationalError,IntegrityError

def fazer_login(db:Session,username:str, password:str):
    try:
        usuario = db.exec(select(Usuario).where(Usuario.usuario_email==username)).first()
        print(f"{usuario}")
        senha_ok = usuario is not None and verifica_senha(password,usuario.senha)
        if not senha_ok:
            raise ValueError("Credenciais inválidas.")
    except IntegrityError as e:
        raise ValueError("Credenciais inválidas.") from e
    

    token = criar_token(str(usuario.id_usuario),Usuario_Status=list(usuario.perfil))
    # Retorna token
    return {
        "acess_token":token,
        "token_type":"bearer"}