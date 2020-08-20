class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        ms = 99990
        ans = ""
        for i in strs:
            if len(i)<ms:
                ms = len(i)
        for i in range(ms):
            for j in range(1,len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:ms]
