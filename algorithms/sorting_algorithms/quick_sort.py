'''Quick Sort

It is a divide-and-conquor comparison-based algorithm.

It's generally faster than MergeSort.

Pick a random element - the pivot - and partition the array, so that all numbers that are less than the partitioning element come before elements that are greater than it. The partitioning happens through a series of swaps. The partitioned element is not guaranteed to be the median, so our sorting could be very slow, thus the worst case runtime.

This is a recursive function
- we will repeatedly call quicksort on the left partition and on the right partition until it is all sorted.

It's very effective for large data sets. Think of it when... "you don’t need a stable sort and average case performance matters more than worst case performance. A quick sort is O(N log N) on average, O(N²) in the worst case. A good implementation uses O(log N) auxiliary storage in the form of stack space for recursion."

Most of the time quicksort is faster than mergesort in real life, since Big O doesn't take into account constants and negligable terms.
####################################################
Example:
 "To start, let’s imagine you have an unordered list, or array, of eight numbers that you want to order.
 4    2    13   6    15    12    7    9
 Your first step is to choose a number in the list called the pivot. Choosing the right pivot number will make all the difference in how fast your QuickSort performs, and there are ready-made formulas to follow for choosing good pivots. But for now, let’s keep it simple and just go with the last number in the array for our pivot number: 9.
 To make the next step easier to follow, we’ll create a separator at the beginning of the array and represent it with the pound-sign.
 #    4    2    13   6    15    12    7    9
 Moving from left to right through our array, our goal is to put any number smaller than the pivot (9) to the left of the separator, and any number greater than (or equal to) the pivot to the right of the separator. We start with the first number in our array: 4. To move it to the left of the separator, we just move the separator up one element:
 4    #    2    13   6    15    12    7    9
 We do the same with the next number: 2.
 4    2    #    13   6    15    12    7    9
 But then we get to 13, which is larger than the pivot number 9 and already to the right side of the separator. So we leave it alone. Next we come to 6, which needs to go to the left of the separator. So first, we swap it with 13 to get it into position:
 4    2    #    6    13    15    12    7    9
 Then we move the separator passed it:
 4    2    6    #    13    15    12    7    9
 Next up is 15, which is already to the right of the separator, so we leave it alone. Then we have 12. Same thing. But 7, our last number before reaching the pivot, needs the same kind of help moving as 6 did. So we swap 7 with 13 to get it into position:
 4    2    6    #    7    15    12    13    9
 Then, once again, we move the separator passed it:
 4    2    6    7    #    15    12    13    9
 Finally, we come to our pivot number: 9. Following the same logic as we have above, we swap 15 with 9 to get the pivot number where it needs to be:
 4    2    6    7   #    9    12    13    15
 Since all the numbers to the left of 9 are now smaller than 9, and all the numbers to the right of 9 are greater than 9, we’re done with our first cycle of QuickSort. Next, we’ll treat each set of four numbers on either side of the separator as a new array to apply QuickSort to. We’ll spare you the details, but the next round will give us four pairs of numbers to easily apply our final round of QuickSort to. The end result will be the following ordered list that took us less time to generate than it would have with the simpler MergeSort:
 2    4    6    7    9    12    13    15" (https://towardsdatascience.com)

####################################################
RUNTIME:
O(n log(n)) on average, worstcase though is exponential, or O(n^2)
memory or space complexity: O(log(n)), which is better than mergesort.

Resources:
- https://www.youtube.com/watch?v=RFyLsF9y83c
- https://towardsdatascience.com/top-algorithms-and-data-structures-you-really-need-to-know-ab9a2a91c7b5


'''
