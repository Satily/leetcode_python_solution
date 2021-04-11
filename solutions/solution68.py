class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        if len(words) == 0:
            return []

        current_line, current_length = [words[0]], len(words[0])
        result = []
        for word in words[1:]:
            lw = len(word)
            if current_length + 1 + lw > maxWidth:
                line = ""
                reset_width, space_count = maxWidth - current_length, len(current_line) - 1
                if space_count == 0:
                    line = current_line[0] + " " * reset_width
                else:
                    base, addition = reset_width // space_count + 1, reset_width % space_count
                    for i in range(addition):
                        line += current_line[i] + " " * (base + 1)
                    for i in range(addition, space_count):
                        line += current_line[i] + " " * base
                    line += current_line[-1]
                result.append(line)
                current_line = [word]
                current_length = lw
            else:
                current_line.append(word)
                current_length += lw + 1
        line = ' '.join(current_line)
        line += ' ' * (maxWidth - len(line))
        result.append(line)
        return result



if __name__ == "__main__":
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                                  "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
