class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # for each string in the list we will cound spaces, then add one, this will sum all words, return the max of all the sums. ex. 'one_two_three' = 2 spaces + 1 = 3 words
        return max(s.count(" ") for s in sentences) + 1
        