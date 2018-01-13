from services import determine_winners
import sys


DAYS_IN_TERM = 265  # Congress is in session a little more than 130 days per year.


def allocate(results):
    winners = determine_winners.determine_winners(results)
    return determine_day_allocation(winners)


def determine_day_allocation(all_winners):
    days_won = [determine_days_won(district_winners) for district_winners in all_winners]
    return days_won


def determine_days_won(district_winners):
    vote_shares = calculate_vote_shares(district_winners)
    days_served = initialize_days_served(district_winners)
    exp_days_served = add_expected_days_served(days_served.copy(), vote_shares)
    difference_days_served = calculate_differences(exp_days_served, days_served)

    representative_list = list()
    for day in range(0, DAYS_IN_TERM):
        candidate = determine_days_candidate(difference_days_served, district_winners)
        representative_list.append(candidate)
        days_served[candidate.name] += 1
        exp_days_served = add_expected_days_served(exp_days_served, vote_shares)
        difference_days_served = calculate_differences(exp_days_served, days_served)

    return representative_list


def calculate_vote_shares(district_winners):
    total_votes = sum([(int(candidate.votes) if candidate.votes != "NA" else 1) for candidate in district_winners])
    vote_shares = dict()
    for candidate in district_winners:
        vote_shares[candidate.name] = (int(candidate.votes) if candidate.votes != 'NA' else 1) / float(total_votes)
    return vote_shares


def initialize_days_served(candidates):
    days_served = dict()
    for candidate in candidates:
        days_served[candidate.name] = 0
    return days_served


def determine_days_candidate(differences, candidates):
    maximum_difference = -sys.maxint
    chosen_candidate = None
    for candidate_name in differences:
        if differences[candidate_name] > maximum_difference:
            maximum_difference = differences[candidate_name]
            days_winners = [candidate for candidate in candidates if candidate.name == candidate_name]
            chosen_candidate = days_winners[0]
    return chosen_candidate


def add_expected_days_served(days_served, vote_shares):
    for candidate in vote_shares:
        days_served[candidate] += vote_shares[candidate]
    return days_served


def calculate_differences(exp, actual):
    differences = dict()
    for name in exp:
        differences[name] = exp[name] - actual[name]
    return differences
