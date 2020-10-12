'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

************************************************************************

What are base cases?
    empty string?
    word can't contain 'th' (less than 2 characters)

    Both of those can be combined into a less than 2 character case

We can traverse the string by character, looking for `th` - and if we find it, add to a result,
then move 2 characters to the right, and check again

if we don't find it in the first character, we move over one character until we do, moving towards our base case

'''


def count_th(word):

    if len(word) < 2:  # base case
        return 0

    elif word[0:2] == 'th':  # we find an occurance of 'th'
        return 1 + count_th(word[2:])  # add to the total and move right 2 index spaces

    else:  # couldn't find it
        return count_th(word[1:])  # move to the right 1  index space
