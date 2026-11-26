from sqlalchemy import delete
from db import session_local
from model.subject import Subjects

class CourseRepository:
    def __init__(self):
        self.connection=session_local()
    
    
    def add_subject_score(self,subjects:Subjects):
        self.connection.add(subjects)
        self.connection.commit()


    def get_course_by_roll(self, roll:int):
        course_score= self.connection.query(Subjects).filter(Subjects.student_roll== roll).first()
        return course_score
