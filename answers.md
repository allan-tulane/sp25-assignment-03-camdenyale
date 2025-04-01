# CMPS 2200 Assignment 3
## Answers

**Name:**Camden Yale


Place all written answers from `assignment-03.md` here for easier grading.

1)
A. Start with N and an empty list of coins. Find the largest 2^k such that 2^k <= N. Subtract 2^k from N and add 2^k to the list of coins. Repeat steps 2 and 3 until N <= 1. Return the list of coins.   

B. We know this algorithm is optimal because k is a maximum every time. The largest value a coin can have will always be less than or equal to the value of N, no smaller values could replace it without using more coins.   

C. Work = O(log n) Span = O(log n)   

2) 
   
A. D = {1, 3, 4} and N = 6. Algorithm selects the largest coin (4) meaning 6 - 4 = 2. The only way to make two out of our coins is two 1 coins, totalling to three coins {4, 1, 1}. This is not the optimal solution, using two 3 coins only requires two coins {3 , 3}. This shows greedy algorithm does not always produce the minimum number of coins. 
   
B. If the minimum number of coins to make N is given by an optimal combination. When we take one of these coins D, the remaining value calculated by N - D must also be made using the minimum number of coins. If we find a better way to make N - D would be a contradiction. Therrefore, the optimal substructure is the minimum numbfer of coins to make the N value.   

C. Top down method: we must account for each substructure without any repetitions or recursions. Work = O(n) Span = O(n)



