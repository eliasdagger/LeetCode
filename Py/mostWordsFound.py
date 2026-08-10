# LeetCode 2114 - Maximum Number of Words Found in Sentences (Easy)
#
# You are given an array of strings sentences. Each sentence is a list of words
# separated by single spaces, with no leading or trailing spaces.
#
# Return the number of words in the sentence that has the most words.
#
# Since the spacing is guaranteed to be clean, a sentence's word count is just its
# number of spaces plus one.
#
# Example: ['alice and bob love leetcode','i think so too','this is great thanks very much']
#       -> 6

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # for each string in the list we will cound spaces, then add one, this will sum all words, return the max of all the sums. ex. 'one_two_three' = 2 spaces + 1 = 3 words
        return max(s.count(" ") for s in sentences) + 1
        