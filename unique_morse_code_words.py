'''International Morse Code defines a standard encoding where each letter is mapped to a series of
dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of
each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation
"-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".


Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
'''
#####################################
'''# from Leetcode solution, time complexity 0(S), where S is the sum
of the length of words in words. I admittedly don't understand this complicated set comprehension yet'''
#####################################

def morse_representations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    seen = {"".join(morse[ord(c) - ord('a')] for c in word) for word in words} # this is a set!
    #return len(seen)
#print(morse_representations(["gin", "zen", "gig", "msg"]))


#####################################
'''A longer approach, sorted out with my brains and another person's code,
using multiple forloops, probably n^2?'''
#####################################


def mc_transform(words):
    m_alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    combo_alpha = dict(zip(alpha,m_alpha))
    one_and_only = set()
    for word in words:
        morsecode_words = str()
        for letter in word:
            morsecode_words = morsecode_words + combo_alpha[letter]
        if morsecode_words not in one_and_only:
            one_and_only.add(morsecode_words)
    return len(one_and_only)

#print(mc_transform(["gin", "zen", "gig", "msg"]))


# def m_transform returns the actual morse patterns formed by the words.
def m_transform(words):
    m_alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    combo_alpha = dict(zip(alpha,m_alpha))
    #one_and_only = set()
    one_and_only = str()
    for word in words:
        morsecode_words = str()
        for letter in word:
            morsecode_words = morsecode_words + combo_alpha[letter]
        #one_and_only.append(morsecode_words)
        one_and_only = one_and_only + morsecode_words
    return one_and_only
print(m_transform(["gin", "zen", "gig", "msg"]))
