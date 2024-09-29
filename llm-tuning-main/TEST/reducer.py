#!/usr/bin/env python3

import sys
import string


def reducer():
    product_sentiments = {}
    
    for line in sys.stdin:
        product_id, sentiment = line.strip().split(':')

        if product_id not in product_sentiments :
            product_sentiments[product_id] = {"positive": 0, "negative": 0, "total": 0}

        if sentiment == 'none' :
            # product_sentiments[product_id]["total"] += 1
            continue
        product_sentiments[product_id][sentiment] += 1
        product_sentiments[product_id]["total"] += 1

    output = []

    for product_id, counts in product_sentiments.items():
        determined_sentiment = 'positive' if counts['positive'] >= counts['negative'] else 'negative'
        output.append(f"{product_id} {determined_sentiment} {counts['positive']}/{counts['total']} {counts['negative']}/{counts['total']}")
            
        
        
    for result in output:
        print(result)


if __name__ == '__main__':
    reducer()
