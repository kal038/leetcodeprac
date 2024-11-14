class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        #build adj list
        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[: j] + '*' + word[j+1 :]
                neigh[pattern].append(word)

        #setup BFS
        queue = collections.deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        res = 0

        #spread BFS
        while queue:
            res += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[: j] + '*' + word[j+1 :]
                    for nword in neigh[pattern]:
                        if nword in visited:
                            continue
                        else:
                            visited.add(nword)
                            queue.append(nword)
        return 0
        




        
