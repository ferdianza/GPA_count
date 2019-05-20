try:
    total_credit = int(input("Enter your total credits: "))
    total_courses = int(input("Enter your total course: "))
    print("\n")

    grade = ["a", "b", "c", "d", "e"]
    is_grade = True
    in_value = 0
    total_value = 0
    total_crs = 0

    for course in range(total_courses):
        value = input("Your Course " + str(int(course + 1)) + ": ")
        crs = int(input("Number of Credits: "))

        if value.lower() not in grade:
            is_grade = False

            while is_grade == False:
                print("Input Error make sure you write A, B, C, D, or E\n")
                value = input("Your Course " + str(int(course + 1)) + ": ")
                crs = int(input("Number of Credits: "))

                if value.lower() in grade:
                    is_grade = True

        if value.lower() == "a":
            in_value = 4
        elif value.lower() == "b":
            in_value = 3
        elif value.lower() == "c":
            in_value = 2
        elif value.lower() == "d":
            in_value = 1
        elif value.lower() == "e":
            in_value = 0

        in_value = in_value * crs
        total_value += in_value
        total_crs += crs

    if total_crs != total_credit:
        print("\nThe total credit and total number of credit NOT MATCH, please check again")
    else:
        GPA = float(total_value / total_credit)
        print("\nYour GPA: %.2f" % (GPA))

except ValueError:
    print("You Enter Wrong Value, Value ERROR")