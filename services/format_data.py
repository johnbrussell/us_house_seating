import csv
from collections import namedtuple


electionResults = namedtuple('electionResults', ['state', 'district', 'results'])
candidate = namedtuple("candidate", ['name', 'party', 'votes', 'state', 'district'])
dataWithColumns = namedtuple("dataWithColumns", ['data', 'columns'])


def read_in_data():
    with open('./data/Us_House_of_Representatives_voting.csv') as f:
        unformatted_election_results = csv.reader(f, delimiter=',')
        election_data_nt = separate_columns_from_data(unformatted_election_results)
        candidate_results_list = [format_line(line, election_data_nt.columns) for line in election_data_nt.data]
    return format_results(candidate_results_list)


def format_line(line, cols):
    # Each line corresponds to a candidate's results; this function formats each candidate's result into a
    #  candidate namedtuple.
    party_and_name = line[cols["Candidate"]]
    party = party_and_name[0]
    name = party_and_name[1:].lstrip(' ').lstrip("Winner").strip(' ').rstrip('(i)').rstrip(' ')
    return candidate(name=name, party=party.upper(), votes=line[cols['Vote Total']],
                     state=line[cols['State']], district=line[cols['District']])


def format_results(unformatted_results):
    # This function takes the list of candidate namedtuples and groups them by state and district.
    states = dict()
    for result in unformatted_results:
        if result.state not in states:
            states[result.state] = dict()
        if result.district not in states[result.state]:
            states[result.state][result.district] = list()
        states[result.state][result.district].append(result)

    election_results = list()
    for state in states:
        for district in states[state]:
            election_results.append(states[state][district])

    return election_results


def separate_columns_from_data(data_gen):
    # data_gen is a generator of the data from the CSV file that is the input.  This function separates that
    #  generator into its first element (ie., the columns of the data) and the rest of the data.
    columns = data_gen.next()
    data = dataWithColumns(data=data_gen, columns=create_csv_column_dict(columns))
    return data


def create_csv_column_dict(columns):
    column_index = 0
    column_indices = dict()
    for name in columns:
        column_indices[name] = column_index
        column_index += 1
    return column_indices
