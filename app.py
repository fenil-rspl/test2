import os
from fastapi import FastAPI
from config import config

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to the FastAPI application'}