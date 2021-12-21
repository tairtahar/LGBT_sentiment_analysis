import re


def load_dict_contractions() -> dict:
    return {
        "ain't": "is not",
        "afaik": "as far as I know",
        "amn't": "am not",
        "aren't": "are not",
        "asap": "as soon as possible",
        "can't": "cannot",
        "'cause": "because",
        "cos": "because",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "could've": "could have",
        "daren't": "dare not",
        "daresn't": "dare not",
        "dasn't": "dare not",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "e'er": "ever",
        "em": "them",
        "everyone's": "everyone is",
        "finna": "fixing to",
        "gimme": "give me",
        "gonna": "going to",
        "gon't": "go not",
        "gotta": "got to",
        "hadn't": "had not",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'll": "he will",
        "he's": "he is",
        "he've": "he have",
        "how'd": "how would",
        "how'll": "how will",
        "how're": "how are",
        "how's": "how is",
        "I'd": "I would",
        "I'll": "I will",
        "I'm": "I am",
        "I'm'a": "I am about to",
        "I'm'o": "I am going to",
        "isn't": "is not",
        "it'd": "it would",
        "it'll": "it will",
        "it's": "it is",
        "I've": "I have",
        "kinda": "kind of",
        "let's": "let us",
        "mayn't": "may not",
        "may've": "may have",
        "mightn't": "might not",
        "might've": "might have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "must've": "must have",
        "needn't": "need not",
        "ne'er": "never",
        "np": "no problem",
        "o'": "of",
        "o'er": "over",
        "ol'": "old",
        "oughtn't": "ought not",
        "shalln't": "shall not",
        "shan't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "should've": "should have",
        "somebody's": "somebody is",
        "someone's": "someone is",
        "something's": "something is",
        "that'd": "that would",
        "that'll": "that will",
        "that're": "that are",
        "that's": "that is",
        "there'd": "there would",
        "there'll": "there will",
        "there're": "there are",
        "there's": "there is",
        "these're": "these are",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "this's": "this is",
        "those're": "those are",
        "tysm": "thank you so much",
        "'tis": "it is",
        "'twas": "it was",
        "wanna": "want to",
        "wasn't": "was not",
        "we'd": "we would",
        "we'd've": "we would have",
        "we'll": "we will",
        "we're": "we are",
        "weren't": "were not",
        "we've": "we have",
        "what'd": "what did",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "when's": "when is",
        "where'd": "where did",
        "where're": "where are",
        "where's": "where is",
        "where've": "where have",
        "which's": "which is",
        "who'd": "who would",
        "who'd've": "who would have",
        "who'll": "who will",
        "who're": "who are",
        "who's": "who is",
        "who've": "who have",
        "why'd": "why did",
        "why're": "why are",
        "why's": "why is",
        "won't": "will not",
        "wouldn't": "would not",
        "would've": "would have",
        "y'all": "you all",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
        "you've": "you have",
        "Whatcha": "What are you",
        "luv": "love",
        "sux": "sucks"
    }


def strip_accents(text: str) -> str:
    """
    Getting rid of accents from different languages than English.
    :param text: input text to process.
    :return: Text after processing.
    """
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def clean_digits(text: str) -> str:
    """

    :param text: input text to process.
    :return: Text after processing.
    """
    return ''.join([i for i in text if not i.isdigit()])


class tweet_handler:
    def __init__(self, check):
        self.abbreviations = load_dict_contractions()
        self.webs = re.compile(r'(https?://t\.co/[A-Za-z0-9]+)')  # websites.
        self.symbols = re.compile(pattern="["
                                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                          "]+", flags=re.UNICODE)
        self.ats = re.compile(r"@[a-zA-Z0-9-_]+")
        self.check = check

    def clean_tweet(self, text):
        """
        This function is for getting rid of characters that are not helpful for sentiment analysis, and
        translating emojis to their labels, which can reflect sentiments. Also if common abbreviations are used,
        we replace them with their base form.
        :param text: Input text to clean.
        :return: Cleaned text.
        """
        text = self.handle_abbreviations(text)
        text = self.ats.sub(r'', text)
        text = self.symbols.sub(r'', text)
        text = self.webs.sub(r'', text)
        text = strip_accents(text)
        text = clean_digits(text)
        return text

    def handle_abbreviations(self, text):
        text = text.replace("’", "'").lower()
        words = text.split()
        reformed = [self.abbreviations[word] if word in self.abbreviations else word for word in words]
        text = " ".join(reformed)
        return text

