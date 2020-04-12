# Given an array of string words. Return all strings in words which is substring of another word in any order. 

# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
 

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        d = dict()
        result = set()
        for word in words:
            print ('word', word)
            for char_index in range (len(word)):
                char = word[char_index]
                if char in d:
                    for combination in d[char]:
                        print (word[char_index: char_index+ len(combination) ])
                        if combination == word[char_index: char_index + len(combination) ]:
                            result.add(combination)
                            d[char].remove(combination)

            d[word[0]] = [word] if word[0]  not in d else d[word[0]] + [word]
        print (result)
        print (d)
        for word in words:
            for char_index in range (len(word)):
                char = word[char_index]
                if char in d:
                    print (d[char])
                    for combination in d[char]:
                        if word == combination: continue
                        if combination == word[char_index: char_index+ len(combination)]:
                            result.add(combination)
                            d[char].remove(combination)
            
                            
        return result
