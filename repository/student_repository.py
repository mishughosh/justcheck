from sqlalchemy import delete
from sqlalchemy.orm import Session
from model.students import Students
from db import session_local

class StudentRepository:
    def __init__(self):
        self.connection = session_local()
    

    def get_all_student(self):
        return self.connection.query(Students).all()


    def create_student(self, student: Students):
        self.connection.add(student)
        self.connection.commit()