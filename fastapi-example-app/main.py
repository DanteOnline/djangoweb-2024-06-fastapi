import csv
import io
from typing import Annotated

from pydantic import EmailStr

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Query
from fastapi import Body
from starlette.responses import FileResponse
from starlette.responses import StreamingResponse

from create_fastapi_app import create_app
from api import router as api_router
from core.models import Base, db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown

app = create_app(create_custom_static_urls=True, lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
def hello_root():
    return {"message": "Hello World"}


@app.get("/hello/")
def hello_name(
    name: Annotated[
        str,
        Query(min_length=3),
    ],
):
    return {"message": f"Hello {name}!"}


@app.post("/create-user/")
def create_user(email: Annotated[EmailStr, Body(embed=True)]):
    return {
        "id": 1,
        "email": email,
    }


@app.get("/file.pdf/", response_class=FileResponse)
def send_pdf_file():
    return "/Users/suren/Downloads/Get_Started_With_Smallpdf.pdf"


@app.get("/file.csv/", response_class=StreamingResponse)
def send_csv_file():
    file = io.StringIO()
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(
        [
            {
                "name": "John",
                "age": 42,
            },
            {
                "name": "Bob",
                "age": 55,
            },
        ]
    )
    file.seek(0)
    return StreamingResponse(file, media_type="text/csv")
