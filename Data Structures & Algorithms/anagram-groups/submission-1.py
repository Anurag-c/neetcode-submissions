class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            grouped[key].append(word)

        return list(grouped.values())