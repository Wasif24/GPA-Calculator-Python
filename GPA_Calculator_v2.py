transcript = open("Transcript.txt", "r")
file = transcript.readlines()
course_array = []
grade_array = []
credit_array = []
eecs_course_array = []
eecs_grade_array = []
eecs_credit_array = []
true_ct = 0


def letter_to_point(letter):
    if letter.__contains__("NCR"):
        return -1.0
    else:
        if letter == "A+":
            return 9.0
        elif letter == "A":
            return 8.0
        elif letter == "B+":
            return 7.0
        elif letter == "B":
            return 6.0
        elif letter == "C+":
            return 5.0
        elif letter == "C":
            return 4.0
        elif letter == "D+":
            return 3.0
        elif letter == "D":
            return 2.0
        elif letter == "E":
            return 1.0
        else:
            return 0.0


def find_name(line):
    return line[8:17]


def find_credits(line):
    return line[19:23]


def find_grade(line):
    index_of_last_tab = line.rfind("\t")
    return line[index_of_last_tab + 1:len(line) - 1]


def is_eecs(course):
    if course.__contains__("EECS"):
        return True
    else:
        return False


def calculate_credits(credits):
    k = 0
    ct = 0
    while k < len(credits):
        ct += credits[k]
        k += 1
    return ct


def calculate_gpa(credits, grades):
    k = 0
    gpt = 0
    ct = 0
    while k < len(credits):
        gpt += credits[k] * letter_to_point(grades[k])
        ct += credits[k]
        k += 1
    return float(gpt / ct)


def process_course(line, courses, credits, grades):
    if line[len(line) - 1] != '\n':
        line = line + '\n'
    if courses.__contains__(find_name(line)):
        i = courses.index(find_name(line))
        if letter_to_point(grades[i]) < letter_to_point(find_grade(line)):
            grades[i] = find_grade(line)
    else:
        if find_grade(line).__contains__("NCR") or find_grade(line) == 'P':
            credits.append(0.00)
            grades.append(find_grade(line))
        elif len(find_grade(line)) > 6:
            credits.append(0.00)
            grades.append("NGR")
        else:
            credits.append(float(find_credits(line)))
            grades.append(find_grade(line))
        courses.append(find_name(line))


for x in file:
    if find_grade(x).__contains__("NCR") or find_grade(x) == 'P' or len(find_grade(x)) > 6:
        pass
    else:
        true_ct += float(find_credits(x))
        pass
    process_course(x, course_array, credit_array, grade_array)
    if is_eecs(find_name(x)):
        process_course(x, eecs_course_array, eecs_credit_array, eecs_grade_array)

print("Overall Earned Credits: " + str(true_ct))
print("Your Total GPA: " + str(calculate_gpa(credit_array, grade_array)))
print("\nEECS Earned Credits : " + str(calculate_credits(eecs_credit_array)))
print("Your EECS GPA: " + str(calculate_gpa(eecs_credit_array, eecs_grade_array)))
input("\nPress Enter To Close")
