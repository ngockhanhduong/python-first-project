def main():
    name = input("What's your name? ")
    house_sort(name)


# basic syntax using if-else clause
def house_sort_basic(student_name):
    if student_name == "Harry" or student_name == "Ron" or student_name == "Hermione":
        print("Gryffindor")
    elif student_name == "Draco":
        print("Slytherin")
    else:
        print("Who?")


# alternative syntax using match
def house_sort(student_name):
    match student_name:
        case "Harry" | "Ron" | "Hermione":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _: # whatever case that has not been handled
            print("Who?")


main()