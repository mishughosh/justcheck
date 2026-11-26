from pydantic import BaseModel,Field
from typing import Optional

class StudentCreate(BaseModel):
    name:str
    age:int
    email:str
    roll:int
    session:str
    english_score:int=Field(le=100, ge=0)
    math_score:int=Field(le=100, ge=0)
    history_score:int=Field(le=100, ge=0)

    def to_student_dict(self):
        return self.model_dump(exclude={"english_score","math_score","history_score"})

class StudentResponse(StudentCreate):
    id:int
    comment:Optional[str]

    class Config:
        from_attributes = True