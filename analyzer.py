import numpy as np
import statistics
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer


class Analyzer:

    def __init__(self, task='sentiment'):
        """
        Initialization of the model for text analysis..
        :param model_name: Model used to perform the sentiment analysis.
        :param : task: can be either 'sentiment' for sentiment analysis or 'hate' for hate detection.
        """
        self.scores = []
        self.model_name = 'roberta'
        self.task = task
        MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        self.sentiment_model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    def get_sentiment(self, text):
        """
        Perform the sentiment analysis on a specific text.
        :param task: sentiment analysis or hate detection
        :param text: Text to be analyzed.
        :return: Score ∈ [-1.0, 1.0] measuring the 'positivity' of a text.
        """
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.sentiment_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = np.exp(scores - np.max(scores)) / np.exp(scores - np.max(scores)).sum()  # softmax
        if self.task == 'sentiment':
            score = scores[2] * 2 - 1  # the positive normalized to [-1 1]
        else:  #
            score = scores[0] * 2 - 1  # the no-hate is in the first place
        self.scores.append(score)
        return score

    def get_positivity(self, tolerance):
        """
        Function to get some more notion regarding the results.
        :param tolerance: minimum difference between positive and negative to set as positive or negative.
        :return: bolean results of positivity/negativity, the difference between the count of
        positive and the negative tweets. normalized_count_pos is how many positives out of all tweets. lastly
        median of the scores.
        """
        count_positive = np.sum(np.asarray(self.scores) > 0)
        count_negative = len(self.scores) - count_positive
        difference = count_positive - count_negative
        normalized_count_pos = count_positive / len(self.scores) * 2 - 1
        if count_positive >= count_negative + tolerance:
            return True, difference, normalized_count_pos, statistics.median(self.scores)
        else:
            return False, difference, normalized_count_pos, statistics.median(self.scores)
