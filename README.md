This repository analyzes properties of a proposed new method for electing representatives to the US House.
2016 election data is used to generate results.

The proposal is to have multiple winners of each election.  Each winner will serve a full two-year term,
but each district shall only have one voting representative for each day that Congress is in session.
The winning representatives shall alternate time serving as the voting representative.  However, they
shall not split time equally.  By the end of the two-year term, each winning representative shall
have served as the voting representative a percentage of days that is as close to equivalent as possible
to the percentage of the vote they won, relative to the other winning representatives.

The proposal states that the winning representatives shall be determined as follows.  Each political
party on the ballot shall have at most one winning representative.  Unaffiliated candidates shall each
be considered to be in their own, separate political party.  There shall be a minimum threshold
percentage of the vote necessary for each party or unaffiliated candidate to win.  Any unaffiliated
candidate who surpasses that threshold shall be considered a winner.  The top vote getter from each
political party whose cumulative votes surpass the threshold shall be a winner.  No other candidates win.

For example, suppose an election has the following result and a qualifying threshold of 10%:
* Candidate A, Party A, 60% of vote.
* Candidate B, Party B, 20% of vote.
* Candidate C, Unaffiliated, 7% of vote.
* Candidate D, Party C, 6% of vote.
* Candidate E, Party C, 4% of vote.
* Candidate F, Unaffiliated, 3% of vote.

The winning candidates are A, B, and D, and they shall each be the voting representative for 70%,
23%, and 7% of days in the legislative sessions in the two year term following the election, respectively.

There are varying ways of determining how to determine who shall represent a district for each day in the
Congressional session.  This problem is in the class of problems that involve mapping apportionments that are logical
in a continuous space into a discrete space.  Unfortunately, this class of problem is known to have no solution
that does not have seemingly paradoxical results, as proven in the Balinski-Young Theorem.  There are many
different algorithms for finding a mapping, but I will decline to implement any of them.

I will instead implement an iterative method that works as follows.  That is, first the days of a Congressional
session will be ordered from most to least important.  (Most shall be the first day of the session and least
shall be the last day.)  Second, for each day of the session, in order from most to least important, a winning
candidate shall be chosen to serve that day.  This shall be done by calculating, for each candidate, the difference
between the number of assigned days that they would expect to have served based on their vote share and the actual
number of days that had been assigned to them.  The candidate with the largest such difference shall be assigned
the day in question.  Like the present Huntington-Hill method of Congressional reapportionment, this method will
not suffer from the Alabama Paradox, since adding an additional day to a Congressional session would not change the
decision as to which winning candidate should serve the prior days.

This analysis allocates voting days to winning candidates, then runs some light analysis.  Using a 5% threshold for
a party to have a winning candidate and using the assumption that Congress is in session for 265 days during a two year
term, this repository determines that for the 2016 elections, the following results would have occurred:
* Republican winning candidates won the most votes in 240 seats and Democrats in 195. (In Louisiana's 4th district,
the candidate with the most votes was a Democrat, but the Republican won the runoff election in December 2016, which
is why 241 Republicans and 194 Democrats were seated following the 2016 elections).
* 144 days would see _Democrats_ hold the most seats, 116 would see Republicans hold the most seats, and 5 would
see an even split.
* On 64 days, no party would hold a majority of seats.
* The smallest number of seats held by a party on a day when it has the most seats of all parties in the House is 212.
* 49.59% of seat-days would be held by Democrats, 48.92% by Republicans, 0.74% by Libertarians, and the rest by other
parties.
* The maximum number of seats Democrats will hold on any one day is 272 seats; the maximum number of Republican seats
is 255 seats; the maximum number of Libertarian seats is 9.
* The most consecutive days on which Democrats will hold plurality control is 4; the most consecutive days on
which Republicans will hold a plurality is 3.

I see three possible reasons for the difference between the facts that under the current system Republicans have a
majority, but under the system analyzed Democrats will have more time as the majority party.
* The popular vote in the 2016 elections had only about a 1% margin for Republicans -- less than a 241/194 split
would seem to indicate.
* As alluded to above, Louisiana's unconventional system of elections would sometimes dilute the power of the dominant
party under this proposal; Louisiana is a Republican-leaning state.
* Successful third-party candidates tend to be in conservative states.  Of the 60 third-party and unaffiliated
candidates who earned at least 5% of the vote in their districts, a manual count indicates that 37 of those candidates
ran in districts ultimately won by Republicans.
Note that summing the non-blank vote totals in the data set in this repository yields 58M votes for Republicans and
55M for Democrats.

Additional reading and research sources:
* https://en.wikipedia.org/wiki/Apportionment_paradox#Balinski.E2.80.93Young_theorem
* http://rangevoting.org/Apportion.html
* https://data.world/lonelyguppy/2016-us-house-of-rep-voting-by-state-and-district -- source of data set
