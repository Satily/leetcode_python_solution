class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--.."
        ]
        morse_map = {chr(97 + index): code for index, code in enumerate(morse)}
        return len({''.join([morse_map[ch] for ch in word]) for word in words})


if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))



