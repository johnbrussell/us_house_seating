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

This analysis allocates voting days to winning candidates, then for that allocation determines:
* The percentage of seat-days held by each party.
* The percentage of days in each legislative session where each party holds a majority of votes in the House.
* The maximum number of voting representatives each party holds for at least one day in the session.

Additional reading and research sources:
* https://en.wikipedia.org/wiki/Apportionment_paradox#Balinski.E2.80.93Young_theorem
* http://rangevoting.org/Apportion.html
