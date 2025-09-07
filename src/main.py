from fastapi import FastAPI

app = FastAPI(title="Hello World API", version="1.0.0")

@app.get("/")
async def hello_world():
    """Return a hello world message."""
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello_name(name: str):
    """Return a personalized hello message."""
    return {"message": f"Hello {name}"}
