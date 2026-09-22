from sqlmodel import Session
from entidades.models import Emprestimo
from sqlalchemy.exc import OperationalError, IntegrityError

def cadastro_emprestimo(emprestimo:Emprestimo,db: Session):
    try:
        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)
        return emprestimo
    except OperationalError as e:
        print("ERRO REAL:", e)
        raise RuntimeError("Falha na conecção com o Bando de Dados") from e
    except IntegrityError as e:
        raise ValueError("Verifique o erro de Integridade")