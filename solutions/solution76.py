class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        features = {}
        for ch in t:
            features[ch] = features.setdefault(ch, 0) + 1
        feature_count = len(t)
        ls = len(s)
        left, right = 0, 0
        res_left, res_right = -1, ls + 1
        while right < ls or left < ls:
            if feature_count > 0 and right < ls:
                if s[right] in features:
                    features[s[right]] -= 1
                    if features[s[right]] >= 0:
                        feature_count -= 1
                right += 1
            else:
                if right - left < res_right - res_left and feature_count == 0:
                    res_left, res_right = left, right
                if s[left] in features:
                    if features[s[left]] >= 0:
                        feature_count += 1
                    features[s[left]] += 1
                left += 1
                while left < ls and (s[left] not in features or features[s[left]] < 0):
                    if s[left] in features:
                        features[s[left]] += 1
                    left += 1
        if res_left == -1:
            return ""
        else:
            return s[res_left: res_right]


if __name__ == "__main__":
    print(Solution().minWindow("bbaa", "aba"))
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
