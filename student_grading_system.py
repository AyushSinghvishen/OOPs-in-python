class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:   # validation
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grade_letter(self):
        avg = self.average_grade()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average_grade():.2f}, Grade: {self.get_grade_letter()}"


class GradeSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)


# Example usage
if __name__ == "__main__":
    system = GradeSystem()

    # Create students
    s1 = Student("Ayush")
    s2 = Student("Anita")

    # Add grades
    s1.add_grade(85)
    s1.add_grade(90)
    s2.add_grade(60)
    s2.add_grade(72)

    # Add to system
    system.add_student(s1)
    system.add_student(s2)

    # Show results
    system.show_all_students()
