def is_anagram1(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

def is_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False

    letters = {}

    for c in s1:
        letters[c] = letters.get(c, 0) + 1

    for c in s2:
        try:
            # Found more c's in s2 than s1
            if letters[c] == 0:
                return False

        # Found letter in s2 that doesn't exist in s1
        except KeyError:
            return False

        letters[c] -= 1

    return True
