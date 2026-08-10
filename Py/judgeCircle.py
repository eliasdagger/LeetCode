# LeetCode 657 - Robot Return to Origin (Easy)
#
# A robot starts at position (0, 0) and is handed a string moves, where 'U', 'D',
# 'L' and 'R' move it one unit up, down, left and right respectively.
#
# Return true if the robot is back at the origin after running through all of the
# moves, false otherwise.
#
# Note that this asks about the final position only - the path in between does not
# matter, and the moves in each opposite pair simply have to balance out.
#
# Example: 'UD'  ->  true
#          'LL'  ->  false

class Solution(object):
    def judgeCircle(self, moves):
        # if opposite direction moves are made equally they cancel eachother out thus we are still at the centre. 
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
