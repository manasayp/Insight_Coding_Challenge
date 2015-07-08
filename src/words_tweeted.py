# example of program that calculates the total number of times each word has been tweeted.
from collections import Counter
import sys

def main():
    with open(str(sys.argv[1]),"r") as f:
        content = f.read()
    word_freq = Counter(content.split())
    with open(str(sys.argv[2]),"w") as f:
        for key in sorted(word_freq.iterkeys()):
            value = "%s : %d" %(key,word_freq[key])
            f.write(str(value)+'\n')

if __name__ == '__main__':main()
