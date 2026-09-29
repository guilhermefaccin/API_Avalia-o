
from sqlmodel import Session, select
from sqlalchemy.exc import OperationalError, IntegrityError

from entidades.models import (
    Emprestimo,
    Emprestimo_status,
    Status,
    Equipamento
)


def cadastro_emprestimo(emprestimo: Emprestimo, db: Session):
    try:
        print("ID DO EQUIPAMENTO:", emprestimo.id_equipamento)

        # Busca o equipamento existente no banco pelo ID
        equipamento = db.get(
            Equipamento,
            emprestimo.id_equipamento
        )

        # Verifica se o equipamento foi encontrado
        if equipamento is None:
            raise ValueError("Equipamento não encontrado.")

        # Verifica o status do equipamento encontrado
        if equipamento.status_equipamento != Status.disponivel:
            raise ValueError("Este equipamento não está disponível.")

        # Verifica se já existe empréstimo aprovado para esse equipamento
        emprestimo_existente = db.exec(
            select(Emprestimo).where(
                Emprestimo.id_equipamento == emprestimo.id_equipamento,
                Emprestimo.status_em == Emprestimo_status.aprovado
            )
        ).first()

        if emprestimo_existente:
            raise ValueError("Este equipamento já está emprestado.")

        # Salva o empréstimo
        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)

        return emprestimo

    except ValueError:
        db.rollback()
        raise

    except OperationalError as e:
        db.rollback()
        print("ERRO REAL:", e)
        raise RuntimeError(
            "Falha na conexão com o Banco de Dados"
        ) from e

    except IntegrityError as e:
        db.rollback()
        print("ERRO DE INTEGRIDADE:", e)
        print("ERRO ORIGINAL:", e.orig)
        raise ValueError(f"Erro de integridade: {e.orig}")
