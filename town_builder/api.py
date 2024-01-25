from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from build_town import build_town
from build_store import StoreBuilder, store_types
from build_char import NPCCharacter
from build_service import BuildServices, service_types

app = FastAPI()


@app.post("/build_town")
async def build_town_api_call():
    return build_town()

@app.post("/build_npc")
async def build_npc_api_call():
    return NPCCharacter().__dict__

@app.post("/build_store")
async def build_store_api_call(store_type: str):
    if store_type not in store_types:
        raise HTTPException(status_code=404, detail=f"Service type not found, please choose{store_types.keys()}")
    return StoreBuilder(store_type).build_store()


@app.post("/build_service")
async def build_service_api_call(service_type: str):
    if service_type not in service_types.keys():
        raise HTTPException(status_code=404, detail=f"Store type not found, please choose{service_types.keys()}")
    return  BuildServices(service_type).build_service()

