from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_a_hello_for_appointment():
    return {"message":"yesss"}
