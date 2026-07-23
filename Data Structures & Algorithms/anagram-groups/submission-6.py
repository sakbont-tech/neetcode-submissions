class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagram = defaultdict(list)

        for s in strs:
            
            listChar = [0] * 26

            for c in s:
                listChar[ord(c) - ord('a')] += 1
            
            dictAnagram[tuple(listChar)].append(s)
            
        return list(dictAnagram.values())