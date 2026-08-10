# LeetCode 739 - Daily Temperatures (Medium)
#
# Given an array temperatures of daily temperatures, return an array answer where
# answer[i] is how many days you have to wait after day i before a warmer
# temperature arrives. If no warmer day ever comes, answer[i] is 0.
#
# Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
#
# The intended O(n) approach keeps a stack of the days still waiting for a warmer
# one. The code below is an unfinished attempt.

def dailyTemperatures(temperatures):
    res = []
    s = []
    for i in range(len(temperatures)):
        if temperatures[-i - 1] < temperatures[i]:
            s.append(temperatures.pop())
        
            
        

