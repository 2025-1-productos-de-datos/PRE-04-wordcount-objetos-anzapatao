class CountWordsMixin:

    def count_words(self):
        """Count occurrences of each word using a plain dictionary."""
        self.word_counts = {}
        for word in self.words:
            self.word_counts[word] = self.word_counts.get(word, 0) + 1
