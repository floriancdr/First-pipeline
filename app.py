import os
from fastapi import FastAPI

# Lecture de la variable d'environnement 'APP_ENV', valeur par défaut 'development'
ENV_MODE = os.getenv("APP_ENV", "development")

app = FastAPI(title=f"API de Validation CI - Mode {ENV_MODE.upper()}")


@app.get("/")
def read_root():
    """Point d'entrée principal de l'API."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "environment": ENV_MODE,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Récupère un élément par son identifiant."""
    return {"item_id": item_id, "query": q}
