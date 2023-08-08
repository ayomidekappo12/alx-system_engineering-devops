#!/usr/bin/python3
""" Module for storing the count_words function. """
import requests


def fetch_hot_articles(subreddit, page_after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'HolbertonSchool'}
    params = {'after': page_after} if page_after else {}
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)
    
    if response.status_code == 200:
        data = response.json()['data']
        return data['children'], data['after']
    
    return None, None

def count_words(subreddit, word_list):
    word_list = [word.lower() for word in word_list]
    word_count = {word: 0 for word in word_list}

    page_after = None
    while True:
        articles, page_after = fetch_hot_articles(subreddit, page_after)
        if not articles:
            break
        
        for article in articles:
            title_words = article['data']['title'].lower().split()
            for word in word_list:
                word_count[word] += title_words.count(word)

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        if count > 0:
            print(f'{word}: {count * word_list.count(word)}')

subreddit = "programming"
word_list = ["python", "java", "javascript"]
count_words(subreddit, word_list)
