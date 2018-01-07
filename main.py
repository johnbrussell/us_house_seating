from services import format_data, determine_allocation


if __name__ == "__main__":
    data = format_data.read_in_data()
    seating_allocation = determine_allocation.allocate(data)
