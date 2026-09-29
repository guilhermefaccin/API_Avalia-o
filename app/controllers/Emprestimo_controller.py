
from sqlmodel import Session, select, or_
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

        # Busca o equipamento no banco
        equipamento = db.get(
            Equipamento,
            emprestimo.id_equipamento
        )

        # Verifica se o equipamento existe
        if equipamento is None:
            raise ValueError("Equipamento não encontrado.")

        # Verifica se o equipamento está disponível
        if equipamento.status_equipamento != Status.disponivel:
            raise ValueError(
                "Este equipamento não está disponível."
            )

        # Verifica se já existe empréstimo aprovado ou pendente
        emprestimo_existente = db.exec(
            select(Emprestimo)
            .where(
                Emprestimo.id_equipamento == emprestimo.id_equipamento
            )
            .where(
                or_(
                    Emprestimo.status_em == Emprestimo_status.aprovado,
                    Emprestimo.status_em == Emprestimo_status.pendente
                )
            )
        ).first()

        if emprestimo_existente:
            raise ValueError(
                "Este equipamento já está emprestado."
            )

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

        raise ValueError(
            f"Erro de integridade: {e.orig}"
        ) from e


def atualizar_emprestimo(
    id_emprestimo: int,
    novos_dados: Emprestimo,
    db: Session
):
    try:
        # Busca o empréstimo existente
        emprestimo_atual = db.get(
            Emprestimo,
            id_emprestimo
        )

        # Verifica se encontrou
        if emprestimo_atual is None:
            raise ValueError(
                "Empréstimo não encontrado."
            )

        # Atualiza os campos
        emprestimo_atual.data_emprestimo = (
            novos_dados.data_emprestimo
        )

        emprestimo_atual.data_devolucao = (
            novos_dados.data_devolucao
        )

        emprestimo_atual.status_em = (
            novos_dados.status_em
        )

        emprestimo_atual.observacao = (
            novos_dados.observacao
        )

        emprestimo_atual.id_usuario = (
            novos_dados.id_usuario
        )

        emprestimo_atual.id_equipamento = (
            novos_dados.id_equipamento
        )

        emprestimo_atual.id_estoque = (
            novos_dados.id_estoque
        )

        # Salva as alterações
        db.add(emprestimo_atual)
        db.commit()
        db.refresh(emprestimo_atual)

        return emprestimo_atual

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

        raise ValueError(
            f"Erro de integridade: {e.orig}"
        ) from e
