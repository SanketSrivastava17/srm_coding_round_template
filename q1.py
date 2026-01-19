"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""


def first_stable_character(s):
    """
    Find the first stable character in the string.

    A character is stable if:
    1. It appears at least twice
    2. All occurrences are in one continuous group

    Args:
        s (str): Input string

    Returns:
        str or None: First stable character, or None if no stable character exists

    Examples:
        >>> first_stable_character("abccba")
        'c'
        >>> first_stable_character("abc")
        None
        >>> first_stable_character("a")
        None
    """
    if len(s) == 0:
        return None
    
    seen = set()
    
    i = 0
    while i < len(s):
        char = s[i]
        
        
        if char in seen:
            i += 1
            continue
        
        
        count = 1
        j = i + 1
        while j < len(s) and s[j] == char:
            count += 1
            j += 1
        
        appears_later = False
        for k in range(j, len(s)):
            if s[k] == char:
                appears_later = True
                break
        
        if count >= 2 and not appears_later:
            return char
        
        seen.add(char)
        i = j if j > i else i + 1
    
    return None


if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  
    print(first_stable_character("abc"))     
    print(first_stable_character("a"))       
