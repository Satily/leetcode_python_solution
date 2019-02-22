from queue import Queue


class Solution:
    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        deck.sort(reverse=True)
        q = Queue()
        q.put(deck[0])
        for card in deck[1:]:
            q.put(q.get())
            q.put(card)
        result = []
        while not q.empty():
            result.append(q.get())
        result.reverse()
        return result


if __name__ == "__main__":
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # [2,13,3,11,5,17,7]
