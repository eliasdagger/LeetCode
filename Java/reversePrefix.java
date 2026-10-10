/*
 * LeetCode 2000 - Reverse Prefix of Word (Easy)
 *
 * Given a string word and a character ch, find the first occurrence of ch and
 * reverse the part of word from index 0 up to and including that occurrence.
 * Return the resulting string.
 *
 * If ch does not appear in word at all, return word unchanged. Only the first
 * occurrence matters.
 *
 * Example: word = "abcdefd", ch = 'd'  ->  "dcbaefd"
 *          word = "abcd", ch = 'z'     ->  "abcd"
 */

class Solution {
    public String reversePrefix(String word, char ch) {
        // create a stack to reverse order, identify where are prefix will end, push all chars, pop and simultaneously reverse order then rebuild the string
        Deque<Character> stack = new ArrayDeque<>();
        StringBuilder prefix = new StringBuilder();


        int indexChar = word.indexOf(ch);

        if (indexChar == -1) return word;

        for (int i = 0; i <= indexChar; i++){
            stack.push(word.charAt(i));
        }

        while (!stack.isEmpty()){
            prefix.append(stack.pop());
        }

        return prefix.toString() + word.substring(indexChar + 1);
    }
}