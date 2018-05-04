# -*- coding: utf-8 -*-
from collections import Counter
import csv
import string
import json
import pickle

def main(filename):
    f=open(filename)
    lines = f.readlines()
    all_words = []
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)
    counter = Counter()
    counter.update(all_words)

    with open('wordcount.csv','w',newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())
        csv_file.close()
    with open('wordcount.json','w') as json_file:
        json.dump(counter.most_common(),json_file)
        json_file.close()
    with open('wordcount.pkl','wb') as pkl_file:
        pickle.dump(counter,pkl_file)
        pkl_file.close()

if __name__ == '__main__':
    main("i_have_a_dream.txt")
