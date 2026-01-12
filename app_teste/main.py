from fastapi import FastAPI

app = FastAPI()

vendas = {1: {}, 2: {}, 3: {}}


@app.get("/")
def home():
    return "homepage"


@app.get("/venda/{id_venda}")
def consulta_vendas(id_venda: int):
    return vendas[id_venda]
