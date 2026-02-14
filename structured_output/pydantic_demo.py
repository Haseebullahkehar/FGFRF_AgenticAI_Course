from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str= "Hassii"
    age : Optional[int] = None
    # email: EmailStr
    cgpa: float = Field(ge=0.0, le=4.0, default=3, description="The cumulative grade point average of the student")  # cgpa between 0.0 and 4.0


# new_student = {'name':'haseeb'}
# new_student = {'name':23}
new_student = {'age': 32, 'cgpa': 3.5} # by default 


student = Student(**new_student)

print(student)
  