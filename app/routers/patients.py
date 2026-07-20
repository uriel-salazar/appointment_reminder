from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_a_hello():
    return {"HELLOOOO"}
