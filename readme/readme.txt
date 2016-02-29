Plugin adds one command, "Sum Lines", which sums numbers in all lines affected 
by selection (any type of selection, entire lines taken, float nums allowed). 
It outputs result sum to new tab, and outputs list of lines which contain invalid 
numbers (ie mistakes).

Example of sel-text:

    10
    100.10
    dd
    20.005
    100.10d

Output is:

    Sum: 130.105
    Lines processed: 6
    Lines skipped: 2
      Line 3: dd
      Line 5: 100.10d


Author: Alexey T.
