# Task 2
"""
In input string word(1 word):
• replace the vowel with the nearest left consonant.
• replace the consonant with the nearest right vowel.
P.S. To complete this task imagine the alphabet is a circle (connect the first and last element of the
array in the mind). For example, 'a' replace with 'z', 'y' with 'a', etc.(see below)
For example:
'cat' => 'ezu'
'abcdtuvwxyz' => 'zeeeutaaaaa'
It is preloaded:
const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
const consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'];
const vowels = ['a','e','i','o','u'];
P.S. You work with lowercase letters only.
"""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

def next_vowel(ind: int) -> str:
    """
    Function that replaces a consonant with the closest vowel to the right
    :param ind: the index of the character in the alphabet
    :return: the nearest right vowel
    """
    while alphabet[ind] not in vowels:
        ind += 1
        if ind > 25:
            ind -= 26
    return alphabet[ind]


def replace_letters(string: str) -> str:
    """
    Function that replaces vowels with the nearest left consonants,
    and consonants with the nearest right vowels
    :param string: the word in which letters will be replaced
    :return: the word with rearranged letters
    """
    return ''.join(
        next_vowel(alphabet.index(char)) if char not in vowels
        else alphabet[alphabet.index(char) - 1]
        for char in string)


if __name__ == "__main__":

    words = 'cat', 'abcdtuvwxyz'
    assert replace_letters(words[0]) == 'ezu'
    assert replace_letters(words[1]) == 'zeeeutaaaaa'
    for word in words:
        result = replace_letters(word)
        print(f'Result: {word} => {result}')
