"""
    Features:
    Calculate Overall GPA
        Sum(Grade Point * Credit amount) / Total Number of Credits
    Calculate number of credits
    Calculate Course Code specific GPA (e.g. EECS, PHIL, MATH)
    Calculate GPA based on terms (e.g. FW, S1, S2, SU)
"""


def get_code(line):
    return line[8:17]


def get_grade(line):
    index_of_last_tab = line.rfind('\t')
    return line[index_of_last_tab+1:len(line)-1]
    # if line[-2] == "+":
    #     return line[-3:-1]
    # return line[-2]


def get_credits(line):
    return line[19:23]


def get_term(line):
    return line[0:4]


letter_to_gp = {
    "A+": 9.0,
    "A": 8.0,
    "B+": 7.0,
    "B": 6.0,
    "C+": 5.0,
    "C": 4.0,
    "D+": 3.0,
    "D": 2.0,
    "E": 1.0
}
gpt = 0
ct = 0

# Read File
transcript = open("Transcript.txt", 'r')
file = transcript.readlines()
course_code_filter = input("Enter Course Code Specific (Press enter for None or 'X' to terminate):").upper()
term_filter = input("Enter Term (Press enter for None or 'X' to terminate):").upper()
while course_code_filter != 'X' and term_filter != 'X':
    if course_code_filter == '\n':
        course_code_filter = None

    for i, x in enumerate(file):
        if i == len(file)-1:
            if x[-1] != '\n':
                x += "\n"       # Append \n if absent

        if get_code(x).__contains__(course_code_filter) and letter_to_gp.get(get_grade(x)) is not None:
            if get_term(x).__contains__(term_filter):
                print("{}\t {}\t {}\t {}\t {}".format(i+1, get_term(x), get_code(x), get_grade(x), letter_to_gp.get(get_grade(x))))
                gpt += float(get_credits(x)) * letter_to_gp.get(get_grade(x))
                ct += float(get_credits(x))
    if ct == 0:
        print("Error: No courses found")
    else:
        print("Your Grade Point Total: {}".format(gpt))
        print("Your Credit Total: {}".format(ct))
        print("Your Grade Point Average: {:.4f}".format(gpt/ct))
    course_code_filter = input("Enter Course Code Specific (Press enter for None or 'X' to terminate):").upper()
    term_filter = input("Enter Term (Press enter for None or 'X' to terminate):").upper()
    gpt = 0
    ct = 0
