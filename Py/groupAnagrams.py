# LeetCode 49 - Group Anagrams (Medium)
#
# Given an array of strings strs, group together all of the anagrams - words built
# from exactly the same letters in a different order.
#
# Return a list of the groups. The groups may be in any order, and so may the
# words inside each group.
#
# Example: ['eat','tea','tan','ate','nat','bat']
#       -> [['eat','tea','ate'],['tan','nat'],['bat']]

class Solution(object):
    def groupAnagrams(self, strs):
        ga = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in ga:
                ga[sorted_word] = []
            
            ga[sorted_word].append(word)




        return list(ga.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        