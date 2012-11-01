def isSubstring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return isSubstring(s2, s1 + s1)
