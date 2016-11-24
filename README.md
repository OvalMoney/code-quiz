# Oval code-quiz

## Problem

You are hosting a party with `G` guests and notice that there is an odd number of
guests! When planning the party you deliberately invited only couples and gave
each member of the couple the same unique number `C` on their invitation.
You would like to single out whoever came alone by asking all of the guests for
their invitation numbers.

### Input

The first line of input gives the number of cases, `N`.
`N` test cases follow. For each test case there will be:

One line containing the value `G` the number of guests.
One line containing a space-separated list of `G` integers. Each integer `C`
indicates the invitation code of a guest.

### Output

For each test case, output one line containing `Case #x: ` followed by the
number `C` of the guest who is alone.

### Limits

1 ≤ N ≤ 50
0 < C ≤ 2147483647
Small dataset

3 ≤ G < 100
Large dataset

3 ≤ G < 1000

*Sample*

```
Input

3
3
1 2147483647 2147483647
5
3 4 7 4 3
5
2 10 2 10 5

Output

Case #1: 1
Case #2: 7
Case #3: 5
```

## How to participate

Fork this project and submit a pull request with your code and your output.
We expect the output files in the top-level directory, with these file names:

`oval-quiz-sm.out`

`oval-quiz-lg.out`
