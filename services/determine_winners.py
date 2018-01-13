PERCENT_TO_WIN = 5


def determine_winners(results):
    winners_only_results = [filter_for_winners(district_result) for district_result in results]
    return winners_only_results


def filter_for_winners(district_result):
    party_winners = dict()
    party_votes = dict()
    for candidate in district_result:
        if candidate.party not in party_winners:
            if candidate.party == 'I':
                party_winners[candidate.name] = candidate
                party_votes[candidate.name] = int(candidate.votes) if candidate.votes != 'NA' else 1
            else:
                party_winners[candidate.party] = candidate
                party_votes[candidate.party] = int(candidate.votes) if candidate.votes != 'NA' else 1
        else:
            if (int(candidate.votes) if candidate.votes != 'NA' else 1) > party_winners[candidate.party].votes:
                party_winners[candidate.party] = candidate
            party_votes[candidate.party] += int(candidate.votes) if candidate.votes != 'NA' else 1

    total_votes = sum([int(candidate.votes) if candidate.votes != "NA" else 1 for candidate in district_result])
    threshold_votes = total_votes * PERCENT_TO_WIN / 100
    winning_parties = list()

    for party in party_votes:
        if party_votes[party] > threshold_votes:
            winning_parties.append(party)

    winning_candidates = [candidate for candidate in district_result if
                          is_winning_party(candidate, winning_parties) and is_party_winner(candidate, party_winners)]
    return winning_candidates


def is_winning_party(candidate, winning_parties):
    if candidate.party in winning_parties:
        return True
    if candidate.name in winning_parties and candidate.party == 'I':
        return True
    return False


def is_party_winner(candidate, party_winners):
    party = candidate.party
    if candidate.party == 'I':
        party = candidate.name

    return party_winners[party].name == candidate.name
