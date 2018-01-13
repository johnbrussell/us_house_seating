from services import format_data, determine_allocation, analyze_allocation


if __name__ == "__main__":
    # Read in a list of results by congressional district.
    data = format_data.read_in_data()

    # Convert that into a list of seats, each of which is a list of who will serve each day of the session.
    seating_allocation = determine_allocation.allocate(data)

    # Create the desired summary statistics.
    analyze_allocation.analyze_allocation(seating_allocation)
