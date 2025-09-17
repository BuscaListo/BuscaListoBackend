import os
import httpx
import socket
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.interfaces.api import product_router, bcv_router, category_router, offer_router, company_router
from app.infrastructure.config.constants import PROJECT_NAME, VERSION, DESCRIPTION, ALLOW_ORIGINS, DB_TYPE, HOST, PORT, RELOAD, NAMEDB

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    root_path="",  # Para manejar correctamente los redirects
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware for proxy headers
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["*"]
)

# Custom middleware to force HTTPS in redirects
class ForceHTTPSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Si es un redirect 307, cambiar http por https en la location
        if response.status_code == 307 and "location" in response.headers:
            location = response.headers["location"]
            if location.startswith("http://"):
                response.headers["location"] = location.replace("http://", "https://")
        
        return response

app.add_middleware(ForceHTTPSMiddleware)
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
        "db_type": DB_TYPE,
        "Name_db": NAMEDB,
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
        "Name_db": os.getenv("NAMEDB", "Undefined"),
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
        host=HOST,
        port=PORT,
        reload = RELOAD,
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
        reload_includes=["*.py", "*.html", "*.css", "*.js"],
        proxy_headers=True,
        forwarded_allow_ips="*"
    )
