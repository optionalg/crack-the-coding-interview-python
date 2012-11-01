# Time complexity: O(n)
# Space complexity: O(n)
def is_unique(s):
    letters = {}

    for c in s:
        if letters.get(c):
            return False

        letters[c] = True

    return True

# Time complexity: O(n^2)
# Space complexity: O(1)
def is_unique_no_datastructures(s):
    for i, c in enumerate(s):
        for current_c in s[i + 1:]:
            if c == current_c:
                return False

    return True
