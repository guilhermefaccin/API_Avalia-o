from fastapi import FastAPI, Depends
from dependencies.dependencies import database
# import random
# import datetime
# from routes import aluno_rotes
# from routes import cardapio_routes
# from entidades.agenda import agenda
from config.Config import settings
from sqlmodel import Session
from routes.estoqueequipamento_routes import estoqueequipamento_router
from routes.Equipamento_routes import equipamento_rauter
from routes.usuario_routes import usuario_router
from routes.emprestimo_routes import emprestimo_router

app = FastAPI(
    title="Minha PI",
    description="Primeira API desenvolvida por Guilherme",
    version="1.0.0"
)

# @app.get("/config")
# def config():
#     return settings

app.include_router(estoqueequipamento_router)
app.include_router(equipamento_rauter)
app.include_router(usuario_router)
app.include_router(emprestimo_router)




# app = FastAPI(
#     title= "Primeira API de Guilherme",
#     description="Primeira API desenvolvida por Guilherme",
#     version= "0.0.1"
# )
# app.include_router(aluno_rotes.aluno_rotas)
# app.include_router(cardapio_routes.item_cardapio_routes)
# @app.post("/agenda")
# def agenda(contato:agenda):
#     return {"contato":agenda}

# @app.get("/")
# def root():
#     return {"message":"Olá, esta é minha priemira API"}

# @app.get("/sobre")
# def sobre(valor):
#     return {"item":valor}

# @app.get("/saudacao")
# def saudacao():
#     return {"mensagem" : "Olá, Bem-vindo a nossa primeira API"}


# @app.get("/status")
# def status():
#     return {"Servidor Online e Operante"}

# @app.get("/api/versao")
# def app_versao():
#     return {"versao":"v1.0.0"}

# @app.get("/mensagens/inspiracao")
# def mensagens_inspiracao():
#     return {"mensagens":"Você consegue"}

# @app.get("/mensagens/geek")
# def mensagens_geek():
#     return {"mensagens":"Que a força esteja com você!"}

# @app.get("/sobre/autor")
# def sobre_autor():
#     return {"autor":"Guilherme Faccin"}

# @app.get("/mensagens/bom-dia")
# def mensagens_bomdia():
#     return {"mensagens":"Bom dia, excelente semana de estudos!"}

# @app.get("/matematica/pi")
# def meametica_pi():
#     return {"versao":"3,14"}

# @app.get("/matematica/quadrado-de-oito")
# def matematica_quadradodeoito():
#     quadrado = 8**2
#     return quadrado

# @app.get("/matematica/area-quadrado")
# def matematica_areaquadrado():
#     l=15
#     a=l*l
#     return {a}

# @app.get("/matematica/expressao")
# def matematica_areaexpressao():
#     expressao = (10+5)*2
#     return {expressao}

# @app.get("/jogos/dado")
# def jogos_dado():
#     dado = random.randint(1,6)
#     return {dado}

# @app.get("/jogos/moeda")
# def jogos_moeda():
#     moeda = random.choice(["cara","coroa"])
#     return {moeda}

# @app.get("/jogos/numero-sorte")
# def jogos_numerosorte():
#     numero = random.randint(1,100)
#     return {numero}

# @app.get("/seguranca/senha-aleatoria")
# def seguranca_senhaleatoria():
#     senha = random.randrange(1000,9999)
#     return {senha}

# @app.get("/aleatorio/fruta")
# def aleatorio_fruta():
#     fruta = random.choice(["maca","uva","melancia","pera"])
#     return {fruta}

# @app.get("/aleatorio/verdadeiro-falso")
# def aleatorio_verdadeirofalso():
#     aleatorio = random.choice (["verdadeiro","falso"])
#     return {aleatorio}

# @app.get("/relogio/data")
# def relogio_data():
#     data = datetime.date.today()
#     data_br = data.strftime ("%d/%m/%Y")
#     return {data_br}

# @app.get("/relogio/hora")
# def relogio_hora():
#     hora = datetime.datetime.now()
#     hora_agora = hora.strftime ("%H:%M")
#     return {hora_agora}

# @app.get("/relogio/ano")
# def relogio_ano():
#     ano = datetime.date.today()
#     ano_atual = ano.strftime ("%Y")
#     return {ano_atual}

# @app.get("/relogio/mes")
# def relogio_mes():
#     mes= datetime.date.today()
#     mes_atual = mes.strftime ("%m")
#     return {mes_atual}

# @app.get("/listas/vogais")
# def listas_vogais():
#     vogais = (["A","E","I","O","U"])
#     return vogais

# @app.get("/curiosidades/arco-iris")
# def curiosidades_arcoiris():
#     cores = (["vermelho","laranja","amarelo","verde","azul","anil","violeta"])
#     return cores

# @app.get("/texto/maiusculas")
# def texto_maiusculas():
#     texto = "programação web"
#     return texto.upper()

# @app.get("/listas/dias-semana")
# def listas_diassemana():
#     semana = (["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sabado","domingo"])
#     return semana

# @app.get("/texto/tamanho")
# def texto_tamanho():
#     texto = "Desenvolvimento de APIs"
#     return len(texto)

# @app.get("/listas/alfabeto")
# def listas_alfabeto():
#     alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     return alfabeto






















# @app.get("/api/calculadora/soma")
# def soma(numero1:int, numero2:int):
#     return{"soma":numero1 + numero2}

# @app.get("/api/geometria/retangulo/{base}/{altura}")
# def area_retangulo(base:int,altura:int):
#     return{"area":base*altura}

# @app.get("/api/conversores/temperatura/{Celsius}")
# def temperatura(Celsius:float):
#     return {"fahrenheit": (Celsius * 1.8)+32}

# @app.get("/api/escola/media-simples/media_aritimetica")
# def media_simples(nota1:float,nota2:float,nota3:float):
#     media = (nota1+nota2+nota3)/3
#     return {"media_aritimetica":media}

# @app.get("/api/financas/juros-simples")
# def juros_simples (capital:float,taxa_mensal:float,meses:int):
#     juros = capital * (taxa_mensal) * meses
#     return {"juros_simples": juros}

# @app.get("/api/saude/imc")
# def saude (peso:float,altura:float):
#     imc = peso / (altura **2)
#     return {"imc":imc}

# @app.get("/api/conversores/tempo-horas")
# def tempo_horas (minutos:int):
#     horas = minutos//60
#     minutos_restantes = minutos % 60
#     return {"horas":horas , "minutos_restantes":minutos_restantes}

# @app.get("/api/loja/aplicar-desconto/{valor_de_produto}/{valor_de_desconto}")
# def aplicar_desconto (valor_de_produto:float , valor_de_desconto:float):
#     valor_desconto = (valor_de_produto * (valor_de_desconto/100))
#     valor_total = (valor_de_produto - valor_desconto)
#     return {"total_pagar":valor_total}

# @app.get("/api/geometria/circulo/perimetro")
# def geometria (raio:float):
#     perimetro = 2* 3.141 *raio
#     return {"perimetro":perimetro}

# @app.get("/api/veiculos/consumo-medio")
# def consuma_medio (distancia:int,litros:int):
#     km_litro = distancia / litros
#     return {"km_por_litro":km_litro}

# @app.get("/api/financas/cambio")
# def cambio (valor:float,cotacao:float):
#     valor_conversao = valor / cotacao
#     return {"valor_convertido_dolar":f"{(valor_conversao):.2f}"}

# @app.get("/api/pessoa/idade-dias/{idade}")
# def idade_dias (idade:int):
#     dias_vividos = idade * 365
#     return {"dias_vividos_estimados":dias_vividos}

# @app.get("/api/geometria/triangulo/area/{base}/{altura}")
# def triangulo (base:int,altura:int):
#     area = (base * altura) /2
#     return {"area":area}

# @app.get("/api/restaurante/conta")
# def conta (valor_consmo:float,porcentagem_goejeta:float):
#     porcentagem_goejeta = valor_consmo / 10
#     valor_total = valor_consmo + porcentagem_goejeta
#     return {"valor_gorjeta": porcentagem_goejeta, "valor_total": valor_total}

# @app.get("/api/conversores/tempo-completo")
# def conversores (segundos_totais:int):
#     horas = segundos_totais / 60
#     minutos = segundos_totais / 60
#     segundos = segundos_totais / 60
#     return {"horas":horas ,"minutos":minutos ,"segundos":segundos}






