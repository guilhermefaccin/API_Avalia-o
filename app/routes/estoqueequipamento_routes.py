from fastapi import APIRouter, Depends
from entidades.models import estoqueequipamentos
from sqlmodel import Session
from dependencies.dependencies import database
from controllers.estoqueequipamentocontroller import insert_categoria

estoqueequipamento_router = APIRouter()

@estoqueequipamento_router.post("/estoque")
def insert(categoria : estoqueequipamentos,db: Session = Depends(database.get_db)):
    return insert_categoria(categoria,db)

