from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to CareerOS 🚀"}


@router.get("/about")
def about():
    return {
        "project": "CareerOS",
        "version": "1.0",
        "status": "Development"
    }