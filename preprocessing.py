import re
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from sacremoses

def file_slicer(input, output, n=100, temp=2.0):
    
    count = 0
    random.seed(42)

    p = temp / n

    indices = []

    with open(input, "r", encoding="utf-8") as in_file:
        with open(output, "w", encoding="utf-8") as out_file:

            for i, line in enumerate(in_file):
                
                r = random.random()
                if r <= p:
                    count += 1
                    out_file.write(line)
                    print(count, line)

                    #print(tokenize(line))

                if count >= n:
                    break

                indices.append(i)
    #print("INDICES: ", indices)
    return indices


def tokenize(in_txt):
    tokens = word_tokenize(in_txt)
    return tokens

if __name__ == "__main__":

    dir = "data/"

    tag = "en-it"
    post_tag = "_sub"

    suffixes = [".en",".it"]
    prefixes = ["dev.", "test.", "train."]

    paths = [dir+pf+tag+sf for pf in prefixes for sf in suffixes]
    out_paths = [dir+pf+tag+post_tag+sf for pf in prefixes for sf in suffixes]
    
    print(paths)
    print(out_paths)

    print(tokenize("this is a sentence."))

    out_indices = []

    for in_p, out_p in zip(paths, out_paths):
        ind = file_slicer(in_p, out_p, n=100000, temp=100000.0)

        if out_indices == []:
            out_indices = ind

        for x,y in zip(ind, out_indices):
            
            if x != y:
                print(x, "_", y)
                print("MISMATCH IN INDICES")

