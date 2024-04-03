# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def canConstruct(ransomNote, magazine):
  if ransomNote in magazine:
    return True
  else:
    return False
  
input1 = "a"
input2 = "b"
print(canConstruct(input1, input2)) # False

input1 = "aa"
input2 = "ab"
print(canConstruct(input1, input2)) # False

input1 = "aa"
input2 = "aab"
print(canConstruct(input1, input2)) # True