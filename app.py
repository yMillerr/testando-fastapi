from fastapi import FastAPI; 
from pydantic import BaseModel;

app = FastAPI();

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
};

class venda(BaseModel):
  item: str;
  preco_unitario: int;
  quantidade: int;
  
  model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Foo",
                    "preco_unitario":3,
                    "quantidade": 2,
                }
            ]
        }
    }


@app.post("/venda")
async def adicionarVenda(venda: venda):
  vendas[len(vendas) + 1] = {
    "item": venda.item,
    "preco_unitario": venda.preco_unitario,
    "quantidade": venda.quantidade,
  };
  
  return vendas;
  
  

@app.get("/")
def home():
  return {"Vendas": len(vendas)};


@app.get("/vendas/{id_venda}")
def venda(id_venda: int):
  if id_venda in vendas:
    return vendas[id_venda];
  else:
    return;
   

