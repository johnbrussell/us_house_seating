This repository analyzes properties of a proposed new method for electing representatives to the US House.
2016 election data is used to generate results.

The proposal is to have multiple winners of each election.  Each winner will serve a full two-year term,
but each district shall only have one voting representative for each day that Congress is in session.
The winning representatives shall alternate time serving as the voting representative.  However, they
shall not split time equally.  By the end of the two-year term, each winning representative shall
have served as the voting representative a percentage of days that is equivalent (or as close to
equivalent as possible) to the percentage of the vote they won, relative to the other winning
representatives.

The proposal states that the winning representatives shall be determined as follows.  Each political
party on the ballot shall have at most one winning representative.  Unaffiliated candidates shall each
be considered to be in their own, separate political party.  There shall be a minimum threshold
percentage of the vote necessary for each party or unaffiliated candidate to win.  Any unaffiliated
candidate who surpasses that threshold shall be considered a winner.  The top vote getter from each
political party whose votes surpass the threshold shall be a winner.  If no individual candidate from
a party reaches the threshold, but the sum of that party's candidates exceeds the threshold, the
party's top vote getter shall be a winning candidate.

For example, suppose an election has the following result and a qualifying threshold of 10%:
* Candidate A, Party A, 60% of vote.
* Candidate B, Party B, 20% of vote.
* Candidate C, Unaffiliated, 7% of vote.
* Candidate D, Party C, 6% of vote.
* Candidate E, Party C, 4% of vote.
* Candidate F, Unaffiliated, 3% of vote.
The winning candidates are A, B, and D, and they shall each be the voting representative for 70%,
23%, and 7% of days in the legislative sessions in the two year term following the election, respectively.

There are varying ways of determining how to implement the proposal.  This problem is, in fact, similar
to the varying ways of determining how many congressional districts each state should have following
the census each decade.  There are varying methods that have subtly different results.

For the purpose of this analysis, days shall be allocated to candidates iteratively, and in reverse.
So, the representative who serves as voting representative on the last day of the Congressional session
shall be decided first, then the representative to serve on the second-to-last day shall be decided next,
and so on.  The candidate with the most votes shall serve the last day of the session.  Then, to decide each
prior day, the difference between the number of days in office that each winner should expect to
have served, among days that have already had the voting representative decided, and the number of days
the winner has actually served as the voting representative, among days already decided, shall be calculated.
The winner with the largest such difference shall be the voting representative for that day.

This analysis allocates voting days to winning candidates, then for that allocation determines:
* The percentage of seat-days held by each party.
* The percentage of days in each legislative session where each party holds a majority of votes in the House.
* The maximum number of voting representatives each party holds for at least one day in the session.
