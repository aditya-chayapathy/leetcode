class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = [chr(alphabet) for alphabet in range(ord('a'), ord('z') + 1)]

        alphabet_mapping = {}
        for item in zip(alphabets, alphabet_codes):
            alphabet_mapping[item[0]] = item[1]

        results = set()
        for word in words:
            transformation = ""
            for character in word:
                transformation = transformation + alphabet_mapping[character]
            results.add(transformation)

        return len(results)