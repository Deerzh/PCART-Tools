from fastapi import FastAPI, APIRouter
from fastapi.routing import APIRoute
from starlette.routing import Route

def example_endpoint():
    return {'message': 'Hello'}
router = APIRouter(default_response_class=None)
