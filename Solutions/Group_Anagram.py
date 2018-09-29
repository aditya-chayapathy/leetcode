class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for word in strs:
            sorted_version = "".join(sorted(word))
            if sorted_version in res_dict:
                res_dict[sorted_version].append(word)
            else:
                res_dict[sorted_version] = [word]

        return [res_dict[item] for item in res_dict.keys()]
