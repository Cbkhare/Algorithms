class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        d = self.root
        l = len(word)
        i=0
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
            i+=1
            if i==l: 
                d['end'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        d = self.root
        l = len(word)
        for char in word:
            if char not in d:
                return False
            d = d[char]
        return bool('end' in d)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        d = self.root
        for char in prefix:
            if char not in d:
                return False
            d = d[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
