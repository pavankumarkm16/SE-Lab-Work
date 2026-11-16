
def nights_stayed(days):
    if not isinstance(days, str):
        return 0

    parts = days.split('-')

    if len(parts) != 2:
        return 0

    check_in, check_out = parts

    if not check_in.isdecimal() or not check_out.isdecimal():
        return 0

    check_in = int(check_in)
    check_out = int(check_out)

    if not (1 <= check_in <= 31 and 1 <= check_out <= 31):
        return 0

    if check_out < check_in:
        return 0

    return check_out - check_in


def room_floor(room_code):
    if not isinstance(room_code, str):
        return 0

    parts = room_code.split('-')

    if len(parts) != 2:
        return 0

    building, number = parts

    if not building.isalpha() or not number.isdecimal():
        return 0

    return int(number[0])


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return "Unknown +0"

    names = [n.strip() for n in names_csv.split(',') if n.strip()]

    if not names:
        return "Unknown +0"

    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
