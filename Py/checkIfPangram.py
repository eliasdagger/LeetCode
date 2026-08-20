# LeetCode 1832 - Check if the Sentence Is Pangram (Easy)
#
# A pangram is a sentence that uses every letter of the English alphabet at least
# once. Given a string sentence made up of lowercase English letters, return true
# if it is a pangram and false otherwise.
#
# Example: 'thequickbrownfoxjumpsoverthelazydog'  ->  true
#          'leetcode'                             ->  false

class Solution:
    # if the string is a pangram, then each letter of the alphabet must appear once, thus if the length of the set which removes duplicates == 26, then pangram
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        