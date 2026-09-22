from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from pydantic import EmailStr
from datetime import date

class estoqueequipamentos(SQLModel,table=True): 
    __tablename__ ="estoque"
    id_estoque : int | None = Field(default=None,primary_key=True)
    nome : str = Field(min_length=5,max_length=100)
    descricao : str | None = Field(max_length=100)
    emprestimos : list["Emprestimo"] = Relationship(back_populates="estoque")

###################################################################################################

class Status(str,Enum):
    disponivel= "DISPONIVEL"
    emprestado= "INDISPONIVEL"
    manutencao= "MANUTENCAO"

class EquipamentoBASE(SQLModel):
    id_equipamento : int | None = Field(default=None,primary_key=True) 
    numero_serie : str = Field(min_length=30,max_length=30)
    nome : str = Field(min_length=5,max_length=100)
    descricao : str | None = Field(max_length=300)
    status_equipamento : Status = Field(default=Status.disponivel)

class Equipamento(EquipamentoBASE,table=True):
    __tablename__= "equipamento"
    id_equipamento: int | None = Field(default=None,primary_key=True)
    emprestimos : list ["Emprestimo"]= Relationship(back_populates="equipamento")
##################################################################################################

class Usuario_Status(str,Enum):
    administrador= "ADMIN"
    gestor= "GESTOR"
    usuario= "USUARIO"

class UsuarioBASE(SQLModel):
    id_usuario : int | None = Field(default=None,primary_key=True)
    nome : str | None = Field(max_length=100)
    cpf : str | None = Field(min_length=11,max_length=11,unique=True)
    email : EmailStr | None = Field(max_length=80,unique=True)
    senha : str | None = Field(max_length=50)
    perfil : Usuario_Status | None = Field(default=Usuario_Status.gestor)

class Usuario(UsuarioBASE, table=True):
    __tablename__= "usuario"
    id_usuario: int | None = Field(default=None,primary_key=True)
    emprestimos: list["Emprestimo"]= Relationship(back_populates="usuario")

####################################################################################################

class Emprestimo_status(str,Enum):
    pendente= "PENDENTE"
    aprovado= "APROVADO"
    devolvido= "DEVOLVIDO"
    cancelado= "CANCELADO"
    recusado= "RECUSADO" 

class EmprestimoBASE(SQLModel):
    data_emprestimo : date
    data_devolucao : date
    status_em : Emprestimo_status = Field(default=Emprestimo_status.aprovado)
    observacao: str = Field(max_length=200)

class Emprestimo(EmprestimoBASE, table=True):
    __tablename__="emprestimo"
    id_emprestimo: int | None = Field(default=None,primary_key=True)

    #######
    id_usuario: int = Field(foreign_key="usuario.id_usuario")
    usuario: Usuario = Relationship(back_populates="emprestimos")
    #######
    id_equipamento: int = Field(foreign_key="equipamento.id_equipamento")
    equipamento: Equipamento = Relationship(back_populates="emprestimos")
    #######
    id_estoque: int = Field (foreign_key="estoque.id_estoque")
    estoque: estoqueequipamentos = Relationship(back_populates="emprestimos")