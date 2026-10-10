/*
 * LeetCode 2703 - Return Length of Arguments Passed (Easy)
 *
 * Write a function argumentsLength that accepts any number of arguments and
 * returns how many it was called with.
 *
 * The arguments can be of any type, including objects, arrays and null, and
 * the function may be called with no arguments at all.
 *
 * Example: argumentsLength(5)             ->  1
 *          argumentsLength({}, null, "3")  ->  3
 */

var argumentsLength = function(...args) {
    // return length of args param
    return args.length;
};