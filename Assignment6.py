import sys

#TODO: use functions

# Student information blueprint
class Student_details:
    # Students attributes
    def __init__(self):
        self.full_name = input("Enter your first and last name: ")
        self.student_ID = input("Enter your student ID: ")
        self.student_gender = input("Enter your student gender: ")
        self.mailing_address = input("Enter your mailing address: ")
        self.city = input("Enter your city: ")
        self.country = input("Enter your country: ")
        self.region = input("Enter your region[A or O]: ")
        self.email = input("Enter your email address: ")
        self.phoneNumber = input("Enter your phone number: ")

    def show(self):
        print("Full name is ", self.full_name)
        print("The student id is  ", self.student_ID)
        print("The student gender is  ", self.student_gender)
        print("The student mailing address is ", self.mailing_address)
        print("The student city is  ", self.city)
        print("The student country is  ", self.country)
        print("The student region is ", self.region)
        print("The student email is  ", self.email)
        print("The student phone number is  ", self.phoneNumber)

    def scholarship_check(self):
       #TODO: call the student gender, average score and validate the scholorship
        average_score()
        Student_details.student_gender
        if student_details.region == 'A':
            if student_details.student_gender == 'male':
                if average_test_score.average_test_score >= 80 and average_test_score.average_test_score.programming_score >= 10 and average_test_score.average_test_score.zoom_score >= 3:
                    print(f"The student {student_details.full_name} is eligible for a scholarship.")
                elif student_details.student_gender == 'female':
                    if average_test_score.average_test_score >= 76 and average_test_score.average_test_score.programming_score >= 10 and average_test_score.average_test_score.zoom_score >= 3:
                        print(f"The student {student_details.full_name} is eligible for a scholarship.")
        elif student_details.region == 'O':
            print(f"Sorry, based on your region ({student_details.region}), you are not eligible for a scholarship.")


class average_score:
    def __init__(self):
        self.testscore = []
        self.average_test_score = 0
        self.quiz_one = int(input("Enter your first quiz score: "))
        self.quiz_two = int(input("Enter your second quiz score: "))
        self.quiz_three = int(input("Enter your third quiz score: "))
        self.test_one = int(input("Enter your first test score: "))
        self.test_two = int(input("Enter your second test score: "))
        self.zoom_score = int(input("Enter your zoom score: "))
        self.programming_score = int(input("Enter your programming assignment score: "))
        self.testscore.append(self.quiz_one)
        self.testscore.append(self.quiz_two)
        self.testscore.append(self.quiz_three)
        self.testscore.append(self.test_one)
        self.testscore.append(self.test_two)
        self.average_test_score = sum(self.testscore) / len(self.testscore)
        self.gender = Student_details.student_gender

    def show_test_scores(self):
        print("first quiz score ", str(self.quiz_one))
        print("The student second quiz score is ", str(self.quiz_two))
        print("The student third quiz score is ", str(self.quiz_three))
        print("The student zoom score is ", str(self.zoom_score))
        print("The student programming assignment score is ", str(self.programming_score))

    def student_average_score(self):
        print("The student Average score is " + str(self.average_test_score))


student1 = Student_details()
student1.show()
student1.scholarship_check()
student1 = average_score()
student1.show_test_scores()
student1.student_average_score()
# # student1.average_score.self.average_test_score
