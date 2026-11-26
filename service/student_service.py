from os.path import commonpath
from repository.student_repository import StudentRepository
from repository.courese_repository import CourseRepository
from utils.schema import StudentResponse, StudentCreate
# from utils.schema import StudentUpdate
from model.students import Students
from model.subject import Subjects

class StudentService:
    def __init__(self):
        self.Std_repository = StudentRepository()
        self.subject_reository = CourseRepository()

    def get_students(self):
        students =  self.Std_repository.get_all_student()
        student_list = []
        for student in students:
            course_scoore = self.subject_reository.get_course_by_roll(student.roll)

            average = (course_scoore.english_score + course_scoore.math_score+course_scoore.history_score) / 3
            if average>=90:
                comment="Excellent"
            elif average>=80:
                comment="Better"
            elif average>=70:
                comment="Good"
            else:
                comment="Need improvement"

            student_response = StudentResponse(
                id=student.id,
                name=student.name,
                age=student.age,
                email=student.email,
                roll=student.roll,
                session=student.session,
                english_score=course_scoore.english_score,
                history_score=course_scoore.math_score,
                math_score=course_scoore.math_score,
                comment=comment
            )
            student_list.append(student_response)

        return student_list

    def add_student(self, student_payload: StudentCreate):
        student = Students(**student_payload.to_student_dict())
        self.Std_repository.create_student(student)


        subject= Subjects(student_roll= student_payload.roll,
                          english_score= student_payload.english_score,
                          math_score= student_payload.math_score,
                          history_score= student_payload.history_score)
        self.subject_reository.add_subject_score(subject)
