# Staircase_Problem

This programme solves the Staircase Problem by dynamic programming. The problem is described in detail below:
Let there be n stairs. A person standing at the bottom wants to reach the top. The person can climb either 1 stair or p stairs at a time,
where p is a prime number. Count the number of ways, the person can reach the top.

Examples:
Let n = 1, the person can take 1 step to reach the top. There is only 1 way to reach the top.
Let n = 2 we have (1, 1), (2), i.e., 2 ways to reach the top.
For n = 3 we have (1, 1, 1), (1, 2), (2, 1), (3), i.e., 4 ways to reach the top. 
For n = 6 we have (1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 1, 2, 1), (1, 1, 1, 3), (1, 1, 2, 1, 1), (1, 1, 2, 2), 
(1, 1, 3, 1), (1, 2, 1, 1, 1), (1, 2, 1, 2), (1, 2, 2, 1), (1, 2, 3), (1, 3, 1, 1), (1, 3, 2), (1, 5), (2, 1, 1, 1, 1), 
(2, 1, 1, 2), (2, 1, 2, 1), (2, 1, 3), (2, 2, 1, 1), (2, 2, 2), (2, 3, 1), (3, 1, 1, 1), (3, 1, 2), (3, 2, 1), (3, 3), (5, 1), i.e., 26 ways to reach the top.
