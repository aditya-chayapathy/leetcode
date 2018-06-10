import uuid


class Codec:

    def __init__(self):
        self.my_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        random_id = str(uuid.uuid4())[:8]
        self.my_dict[random_id] = longUrl

        return random_id

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.my_dict.keys():
            return self.my_dict[shortUrl]

        return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))