def get_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter mark for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "Fail"


def main():
    print("===== Student Mark App =====")

    name = input("Enter student name: ").strip()
    city = input("Enter city: ").strip()

    subjects = []
    marks = []

    for number in range(1, 6):
        subject_name = input(f"Enter subject {number} name: ").strip()
        if not subject_name:
            subject_name = f"Subject {number}"

        mark = get_mark(subject_name)
        subjects.append(subject_name)
        marks.append(mark)

    total_mark = sum(marks)
    average = total_mark / len(marks)
    grade = calculate_grade(average)

    print("\n===== Student Report =====")
    print(f"Name         : {name}")
    print(f"City         : {city}")
    print("\nSubject Marks")

    for subject_name, mark in zip(subjects, marks):
        print(f"{subject_name:<12}: {mark}")

    print("\nResult")
    print(f"Total Mark   : {total_mark}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")


if __name__ == "__main__":
    main()
