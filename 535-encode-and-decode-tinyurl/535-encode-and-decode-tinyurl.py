class Codec:
    def __init__(self):
        self.db = {}
        self.MOD = 10**9

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        val = 0
        for index,char in enumerate(list(longUrl)):
            val += ord(char)*index
        val = val % self.MOD
        val = str(val)
        self.db[val] = longUrl
        return val
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))