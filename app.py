from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from users_management import router as users_management_router
from admin import router as admin_router
from security.web import auth_api


app = FastAPI()
app.include_router(
    users_management_router,
    prefix="/users",
    dependencies=[
        Depends(auth_api.admin_oauth2_scheme),
    ],
)
app.include_router(
    admin_router,
    prefix="/admin",
    dependencies=[],
)
app.include_router(auth_api.router, prefix="/token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    import bootstrap

    await bootstrap.on_startup()
