'''
Merge Sort:

"Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list."
- from Interview textbook - p. 146

Think of merge sort "...when you need a stable, O(N log N) sort, this is about your only option. The only downsides to it are that it uses O(N) auxiliary space and has a slightly larger constant than a quick sort. There are some in-place merge sorts, but AFAIK they are all either not stable or worse than O(N log N). Even the O(N log N) in place sorts have so much larger a constant than the plain old merge sort that they’re more theoretical curiosities than useful algorithms."

Example
"...You need to create an ordered line of people out of an unordered group. You don’t have much time, so you come up with a strategy to speed things up.

You first have the group of people, which are all huddled together, divide into two. Then you have each of the two groups divide into two again, and so on, until you are dealing entirely with individuals. You then begin to pair the individuals up, and have the taller of the two in each pair stand to the right of the other one. Pretty soon everyone is organized into these left-right ordered pairs.

Next, you start merging the ordered pairs into ordered groups of four; then merging the ordered groups of four into ordered groups of eight; and so on. Finally, you find that you have a complete, height-ordered line of people, just like the one you encountered above. Without knowing it, you have followed the MergeSort algorithm to accomplish your feat."

- from https://towardsdatascience.com/top-algorithms-and-data-structures-you-really-need-to-know-ab9a2a91c7b5



runtime: O(n log(n)). memory: depends.
comparison based / divide and conquer sorting algorithm





'''
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    #find the middle point and divide it:
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))

def merge(left_half, right_half):
    res = []
    while len(left_half) !=0 and len(right_half) !=0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


unsorted_list = [64, 89, 1000, 54, 2, 7, 9, 856]
print(merge_sort(unsorted_list))
