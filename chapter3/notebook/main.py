from typing import Optional
from fastapi import FastAPI  
from pydantic import BaseModel
import pandas as pd
 
app = FastAPI()
df = pd.read_csv("data.csv")
 
class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return df.to_dict()  
 
@app.get("/items/{item_id}")
def read_item(item_id: int, q:str, limit: int = 10):
    result_df = df[(df['item_id']==item_id)][q].head(limit)
    return {"result": result_df.to_list()}

@app.post("/items/{item_id}")
def save_item(item_id: int, item: Item):
    df.loc[len(df.index)] = {"item_id" : item_id, "name" : item.name, "price" : item.price}
    return {"result": f"item_id {item_id} is saved!"}