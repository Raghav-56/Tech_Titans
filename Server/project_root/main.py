from cli import cli_interface


from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from database import init_db

import os
import sys

# from flask import flask, jsonify

# app = flask(__name__)

# Instead of:
# from api.routes import router
# from database.chroma_db import init_db
# from cli.interface import cli_interface

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize the database
    init_db()
    yield
    # Shutdown: Add any cleanup code here if needed
    # For example: await close_db_connection()
    await close_db_connection()


# @app.on_event("startup")

async def startup_event():
    init_db() 

@app.get("/api/some-endpoint")
async def get_data():
    # Some logic to interact with ChromaDB or other databases
    return {"message": "Data from the backend"}


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        cli_interface()
    else:
        import uvicorn

        print("Starting FastAPI server...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
