import logging

## keep all logs 
logging.basicConfig(
    filename="student_app.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

### rewrite log file every time
# logging.basicConfig(
#     filename="student_app.log",
#     filemode="w",
#     level=logging.DEBUG,
#     format="%(levelname)s: %(message)s"
# )


def calculate_average(marks):
    total_marks = sum(marks)
    try:
        average = total_marks / len(marks)
    
    except ZeroDivisionError:
        print("Cannot calculate average because number of subjects is zero.")
        logging.error("ZeroDivisionError while calculating average.")
        return None
    
    else:
        logging.info("Average calculated successfully.")
        
    return average

def get_result(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Very Good"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"
    

def process_student():

    try:
        logging.info("Student processing started.")

        student_name = input("Enter student name: ")
        logging.info("Student name received.")

        while True:
            try:
                number_of_subjects = int(
                    input("Enter number of subjects: ")
                )

                if number_of_subjects <= 0:
                    print("Number of subjects must be greater than 0.")
                    logging.warning(
                        "Invalid number of subjects: %s",
                        number_of_subjects
                    )
                    continue

            except ValueError:
                print("Please enter a valid number.")
                logging.error("Invalid number of subjects entered.")

            else:
                break

        marks = []

        for i in range(1, number_of_subjects + 1):

            while True:
                try:
                    mark = float(
                        input(f"Enter marks for subject {i}: ")
                    )

                    if mark < 0 or mark > 100:
                        print("Marks must be between 0 and 100")
                        logging.error("Invalid mark entered.")
                        continue

                except ValueError:
                    print("Please enter a valid number.")
                    logging.error("Non-numeric mark entered.")

                else:
                    marks.append(mark)

                    if mark < 50:
                        logging.warning(
                            "Student mark is below passing range."
                        )

                    break

        logging.info("Marks entered successfully.")

        average = calculate_average(marks)
        if average is None:
            return
        
        result = get_result(average)

        print("\n----- Student Result -----")
        print(f"Student Name : {student_name}")
        print(f"Average      : {average:.2f}")
        print(f"Result       : {result}")

        logging.info("Student result calculated successfully.")
        
        highest_mark = max(marks)
        lowest_mark = min(marks)

        print("\n----- Student Statistics -----")
        print(f"Highest Mark : {highest_mark:.2f}")
        print(f"Lowest Mark  : {lowest_mark:.2f}")
        print(f"Average Mark : {average:.2f}")
        print(f"Result       : {result}")

        logging.info("Student statistics calculated successfully.")

    finally:
        print("Processing completed.")

def main():
    ## separator in log file for identification logs every time when it run and append
    with open("student_app.log", "a") as file:
        file.write("\n" + "=" * 60 + "\n")
        
    logging.info("Application started.")
    while True:
        process_student()
        choice = input("Do you want to enter another student?(yes/no): ")
            
        if choice.lower() !="yes":
            break

if __name__ == "__main__":
    main()
    

    





# import logging

# logging.basicConfig(
#     filename="student_app.log", #all logging messages go into this file
#     #level=logging.ERROR,
#     level=logging.DEBUG,
#     format="%(levelname)s: %(message)s"
# )

# def process_student():
#     logging.info("Student processing started.")
#     student_name = input("Enter student name: ")
#     logging.info("Student name received.")
    
#     while True:
#         try:
#             number_of_subjects = int(input("Enter number of subjects: "))
#             if number_of_subjects <= 0:
#                 print("Number of subjects must be greater than 0.")
#                 logging.warning("Invalid number of subjects: %s", number_of_subjects)
#                 continue    
#         except ValueError:
#             print("Please enter a valid number.")
#             logging.error("Invalid number of subjects entered.")
#         else:
#             break
    
#     marks = []
#     for i in range(1, number_of_subjects + 1):
#         while True:
#             try:
#                 mark = float(input(f"Enter marks for subject {i}: "))
#                 if mark < 0 or mark > 100:
#                     print("Marks must be between 0 and 100")
#                     logging.error("Invalid mark enetered")
#                     continue
#             except ValueError:
#                 print("Please enter a valid number")
#                 logging.error("Non numeric mark entered")
#             else:
#                 marks.append(mark)
#                 if mark < 50:
#                     logging.warning("Student mark is below passing range.")
#                 break
#     logging.info("Marks entered successfully.")
    
#     total_marks = sum(marks)
#     try:
#         average = total_marks / number_of_subjects
#     except ZeroDivisionError:
#         print("Cannot calculate average because number of subjects is zero.")
#         logging.error("ZeroDivisionError while calculating average.")
#     else:
#         logging.info("Average calculated successfully.")
       
#     result = "" 
#     if average >= 90:
#         result = "Excellent"
#     elif average >= 75:
#         result = "Very Good"
#     elif average >= 50:
#         result = "Pass"
#     else:
#         result = "Fail"
        
#     print("\n----- Student Result -----")
#     print(f"Student Name : {student_name}")
#     print(f"Average      : {average:.2f}")
#     print(f"Result       : {result}")
    
#     logging.info("Student result calculated successfully.")        
    

# if __name__ == "__main__":
#     process_student()
