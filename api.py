from fastapi import FastAPI
import heroku



app= FastAPI()

@app.get("/")
def home():
    return {"PAGINA HOME"}

@app.get("/correcao")
def correcao():
    return {"PAGINA de CORRECAO"}    

@app.get("/result")
def resultado():
    return {"PAGINA de RESULTADO"}    