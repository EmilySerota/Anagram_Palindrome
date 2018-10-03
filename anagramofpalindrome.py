"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    letter_count = []
    for letter in word:
        if letter in letter_count:
            letter_count.remove(letter)
        else:
            letter_count.append(letter)
    if len(letter_count) > 1:
        return False
    return True



def isPalindrome(word):
    """returns true is word is a palindrome."""
    end_letter = len(word) - 1

    for i in range(len(word)):
        
        if word[i] != word[end_letter]:
            return False

        end_letter = end_letter - 1

    return True 

#print(is_anagram_of_palindrome("racecar"))
#print(is_anagram_of_palindrome("koala"))



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
