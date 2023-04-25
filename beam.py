import numpy as np
import math

vocab = {"A":[0.12, 0.09, 0.82], "B":[0.21, 0.37, 0.92], "C":[0.11, 0.9, 0.01] , "<EOS>": [0.01, 0.11, 0.94]}

def beamSearch(vocab, beam_width, size):
    
    arr = [[1, []]]

    for i in range(size):
        helper = []
        while arr:
            p, sentence = arr.pop()
            for x in vocab.keys():
                if sentence and sentence[-1] == "<EOS>":
                    helper.append([p,sentence])
                else:
                    helper.append([p*vocab[x][i],sentence+[x]])

        helper.sort()
        helper = helper[-beam_width:]
        arr = helper

    return arr[-1]


print(beamSearch(vocab, 2, 3))


    
