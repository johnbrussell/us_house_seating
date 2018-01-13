import math


SEATS_IN_US_HOUSE = 435


def analyze_allocation(allocation):
    daily_seats_by_party = determine_daily_party_seats(allocation)
    seats_won_under_old_system = seats_with_most_votes_by_party(daily_seats_by_party)
    print "Seats where candidate won most votes", seats_won_under_old_system
    days_of_control = determine_days_of_control(daily_seats_by_party)
    print "Days as largest party:", days_of_control
    days_of_plurality = determine_days_without_majority(daily_seats_by_party)
    print "Days where largest party has plurality, not majority:", days_of_plurality
    smallest_plurality = determine_smallest_plurality(daily_seats_by_party)
    print "Smallest number of seats held by largest party:", smallest_plurality
    percent_of_seat_days_by_party = determine_percent_control(daily_seats_by_party)
    print "Percent control by party:", percent_of_seat_days_by_party
    maximum_control_by_party = determine_maximum_control_by_party(daily_seats_by_party)
    print "Maximum control by party:", maximum_control_by_party
    longest_consecutive_control = determine_longest_consecutive_control(daily_seats_by_party)
    print "Most consecutive days of control by party:", longest_consecutive_control


def determine_daily_party_seats(days_by_seat):
    seats_by_day = switch_allocation_structure(days_by_seat)
    daily_seats_by_party = list()
    for list_of_seats in seats_by_day:
        dict_of_party_control = dict()
        for seat in list_of_seats:
            dict_of_party_control = add_seat_to_party_control_dict(seat, dict_of_party_control)
        daily_seats_by_party.append(dict_of_party_control)
    return daily_seats_by_party


def switch_allocation_structure(list1):
    # Takes a list of identical-length lists of candidates and returns a list of identical-length lists of candidates.
    list2 = list(zip(*list1))
    list2 = [list(item) for item in list2]
    return list2


def add_seat_to_party_control_dict(seat, pc_dict):
    if seat.party not in pc_dict:
        pc_dict[seat.party] = 0
    pc_dict[seat.party] += 1
    return pc_dict


def determine_days_of_control(daily_seats_by_party):
    days_of_control = dict()
    for day in daily_seats_by_party:
        party_in_control = determine_largest_party(day)
        if party_in_control not in days_of_control:
            days_of_control[party_in_control] = 0
        days_of_control[party_in_control] += 1
    return days_of_control


def determine_largest_party(seats_per_party):
    largest_party = ''
    largest_seats = 0
    for party in seats_per_party:
        if seats_per_party[party] == largest_seats:
            largest_party = "Multiple"
        if seats_per_party[party] > largest_seats:
            largest_party = party
            largest_seats = seats_per_party[party]
    return largest_party


def determine_percent_control(daily_seats_by_party):
    seat_days_by_party = dict()
    for day in daily_seats_by_party:
        for party in day:
            if party not in seat_days_by_party:
                seat_days_by_party[party] = 0
            seat_days_by_party[party] += day[party]

    total_seat_days = sum(seat_days_by_party.values())
    percent_of_seat_days = dict()
    for party in seat_days_by_party:
        percent_of_seat_days[party] = round(seat_days_by_party[party] / float(total_seat_days) * 100, 2)

    return percent_of_seat_days


def determine_maximum_control_by_party(daily_seats_by_party):
    maximum_control_dict = dict()
    for day in daily_seats_by_party:
        for party in day:
            if party not in maximum_control_dict:
                maximum_control_dict[party] = 0
            if day[party] > maximum_control_dict[party]:
                maximum_control_dict[party] = day[party]
    return maximum_control_dict


def determine_longest_consecutive_control(daily_seats_by_party):
    current_party = 'not_a_party'
    current_days = 0
    longest_control = dict()
    for day in daily_seats_by_party:
        largest_party = determine_largest_party(day)
        if largest_party == current_party or largest_party == 'Multiple':
            current_days += 1
        elif largest_party != 'Multiple':
            current_party = largest_party
            current_days = 1

        if current_party not in longest_control:
            longest_control[current_party] = 0
        if longest_control[current_party] < current_days:
            longest_control[current_party] = current_days
    return longest_control


def seats_with_most_votes_by_party(daily_seats_by_party):
    return daily_seats_by_party[0]


def determine_days_without_majority(daily_seats_by_party):
    days_without_majority = 0
    for day in daily_seats_by_party:
        if max(day.values()) < math.ceil(float(SEATS_IN_US_HOUSE) / 2):
            days_without_majority += 1
    return days_without_majority


def determine_smallest_plurality(daily_seats_by_party):
    smallest_plurality = SEATS_IN_US_HOUSE
    for day in daily_seats_by_party:
        if max(day.values()) < smallest_plurality:
            smallest_plurality = max(day.values())
    return smallest_plurality
