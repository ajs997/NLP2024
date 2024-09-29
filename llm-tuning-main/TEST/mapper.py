#!/usr/bin/env python3

import sys
import string

positive_words = [
    "excellent", "outstanding", "reliable", "impressive", "durable",
    "user-friendly", "high-quality", "affordable", "satisfied", "superb"
]

negative_words = [
    "disappointing", "poor", "unreliable", "defective", "complicated",
    "expensive", "frustrating", "cheap", "unusable", "awful"
]


def determine_review_sentiment(review_text):
    review_text = review_text.lower().translate(str.maketrans('', '', string.punctuation))
    positive_count = sum(1 for word in review_text.split() if word in positive_words)
    negative_count = sum(1 for word in review_text.split() if word in negative_words)
    
    if positive_count > negative_count:
        return 'positive'
    elif positive_count < negative_count:
        return 'negative'
    else:
        return 'none'

def mapper():
    product_reviews = {}
    
    for line in sys.stdin:
        review_id, product_id, review_text = line.strip().split('|')
        
        sentiment = determine_review_sentiment(review_text)
        
        print(product_id + ":"+ sentiment)


if __name__ == '__main__':
    mapper()
