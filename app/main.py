import os
import httpx
import socket
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.api import product_router, bcv_router, category_router, offer_router, company_router
PROJECT_NAME = os.getenv("PROJECT_NAME", "My FastAPI Project")
VERSION = os.getenv("VERSION", "1.0.0")
DESCRIPTION = os.getenv("DESCRIPTION", "Generic FastAPI Boilerplate API.")

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOW_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root(request: Request):
    """
    Endpoint básico que devuelve información del proyecto + IPs.
    """
    client_host = request.headers.get("x-forwarded-for") or request.client.host
    server_ip = socket.gethostbyname(socket.gethostname())

    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.ipify.org?format=json")
        public_ip = r.json()["ip"]

    return {
        "project": PROJECT_NAME,
        "version": VERSION,
        "status": "running",
        "db_type": os.getenv("DB_TYPE", "sqlite"),
        "client_ip": client_host,
        "server_ip": server_ip,
        "public_ip": public_ip
    }

@app.get("/api")
async def api_root(request: Request):
    """
    Endpoint de la API que devuelve información del proyecto + IPs.
    """
    client_host = request.headers.get("x-forwarded-for") or request.client.host
    server_ip = socket.gethostbyname(socket.gethostname())

    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.ipify.org?format=json")
        public_ip = r.json()["ip"]

    return {
        "project": PROJECT_NAME,
        "version": VERSION,
        "status": "running",
        "db_type": os.getenv("DB_TYPE", "sqlite"),
        "client_ip": client_host,
        "server_ip": server_ip,
        "public_ip": public_ip,
        "message": "BuscaListo Backend API is running!"
    }

# Include Routers Execute
app.include_router(product_router.router, prefix="/api")
app.include_router(category_router.router, prefix="/api")
app.include_router(bcv_router.router, prefix="/api/currencies", tags=["currencies"])
app.include_router(offer_router.router, prefix="/api")
app.include_router(company_router.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload = os.getenv("RELOAD", "1") == "1",
        reload_dirs=[os.path.dirname(os.path.abspath(__file__))],
        reload_excludes=[
            "*/.git/*",
            "*/__pycache__/*",
            "*.pyc",
            "*/.pytest_cache/*",
            "*/.vscode/*",
            "*/.idea/*"
        ],
        reload_delay=1,
        reload_includes=["*.py", "*.html", "*.css", "*.js"]
    )
