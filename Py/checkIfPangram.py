# LeetCode 1832 - Check if the Sentence Is Pangram (Easy)
#
# A pangram is a sentence that uses every letter of the English alphabet at least
# once. Given a string sentence made up of lowercase English letters, return true
# if it is a pangram and false otherwise.
#
# Example: 'thequickbrownfoxjumpsoverthelazydog'  ->  true
#          'leetcode'                             ->  false

class Solution(object):
    def checkIfPangram(self, sentence):
        return True if len(set(sentence)) == 26 else False
        """
        :type sentence: str
        :rtype: bool
        """
        