

def student_details():
    student_details.full_name = input("Enter your first and last name: ")
    student_details.student_ID = input("Enter your student ID: ")
    student_details.student_gender = input("Enter your gender: ")
    student_details.mailing_address = input("Enter your mailing address: ")
    student_details.city = input("Enter your city: ")
    student_details.country = input("Enter your country: ")
    student_details.region = input("Enter your region[A or O]: ")
    student_details.email = input("Enter your email address: ")
    student_details.phoneNumber = input("Enter your phone number: ")


def average_test_score():
    testscore = []
    average_test_score = 0

    for quiz in range(1, 4):
        quiz_score = int(input(f"Enter your quiz {quiz} score: "))
        testscore.append(quiz_score)
    for test in range(1, 3):
        test_score = int(input(f"Enter your test {test} score: "))
        testscore.append(quiz_score)
    average_test_score.programming_score = int(input("Enter your programming assignment score[0 – 10]: "))
    average_test_score.zoom_score = int(input("Enter your zoom score [0 – 9]: "))
    average_test_score = sum(testscore) / len(testscore)

    return average_test_score


def scholarship_check():
    # TODO: call the student gender, average score and validate the scholorship
    # average_score()
    # Student_details.student_gender

    if student_details.region == 'A':
        if student_details.student_gender == 'male':
            if average_test_score.average_test_score >= 80 and average_test_score.average_test_score.programming_score >= 10 and average_test_score.average_test_score.zoom_score >= 3:
                print(
                    f"The student {student_details.full_name} is eligible for a scholarship.")
        elif student_details.student_gender == 'female':
            if average_test_score.average_test_score >= 76 and average_test_score.average_test_score.programming_score >= 10 and average_test_score.average_test_score.zoom_score >= 3:
                print(
                    f"The student {student_details.full_name} is eligible for a scholarship.")
    elif student_details.region == 'O':
        print(
            f"Sorry, based on your region ({student_details.region}), you are not eligible for a scholarship.")

    return scholarship_check


def display_scholarship_info():
    while True:
        student_details()
        average_test_score()
        scholarship_check()

        print("**********************STUDENT DETAILS ************************")
        print(f"Full name is ", student_details.full_name)
        print(f"The{student_details.full_name} id is  ", student_details.student_ID)
        print(f"The{student_details.full_name} gender is  ", student_details.student_gender)
        print(f"The{student_details.full_name} mailing address is ", student_details.mailing_address)
        print(f"The{student_details.full_name} city is  ", student_details.city)
        print(f"The{student_details.full_name} country is  ", student_details.country)
        print(f"The{student_details.full_name} region is ", student_details.region)
        print(f"The{student_details.full_name} email is  ", student_details.email)
        print(f"The{student_details.full_name} phone number is  ", student_details.phoneNumber)
        print()
        print("**********************STUDENT AVERAGE SCORE ************************")
        print(f"The{student_details.full_name} zoom score is ", str(average_test_score.zoom_score))
        print(f"The{student_details.full_name} programming assignment score is ", str(average_test_score.programming_score))
        print(f"{student_details.full_name} average score is {average_test_score.average_test_score}")
        print()
        print("**********************STUDENT SCHOLARSHIP CHECK ************************")
        display_scholarship_info()


display_scholarship_info()

