from fastapi import FastAPI

app = FastAPI(title="API de Validation CI")


@app.get("/")
def read_root():
    """Point d'entrée principal de l'API."""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Récupère un élément par son identifiant."""
    return {"item_id": item_id, "query": q}