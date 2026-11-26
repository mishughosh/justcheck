from fastapi import APIRouter, status
from service.student_service import StudentService
from utils.schema import StudentCreate 

router = APIRouter(prefix="/students", tags=["Student"])


@router.get("/all", status_code=status.HTTP_200_OK)
def get_all_students():
    service = StudentService()
    return service.get_students()


@router.post("/add", status_code= status.HTTP_201_CREATED)
def add_student(student_payload: StudentCreate):
    service = StudentService()
    service.add_student(student_payload)