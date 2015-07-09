# example of program that calculates the total number of times each word has been tweeted.
from collections import Counter
import sys
import os

def main():
    try:
        with open(str(sys.argv[1]),"r") as fr:
            if os.stat(str(sys.argv[1])).st_size == 0:
                with open(str(sys.argv[2]),"w") as fw:
                    fw.write("The input file is empty")
                    sys.exit()
            else:
                content = fr.read()
                word_freq = Counter(content.split())
                with open(str(sys.argv[2]),"w") as fw:
                    for key in sorted(word_freq.iterkeys()):
                        value = '{:<25} {:<5}'.format(key,word_freq[key])
                        fw.write(str(value)+'\n')
    except IOError:
        with open(str(sys.argv[2]),"w") as fw:
            fw.write("The input file does not exist")
            sys.exit()
    
if __name__ == '__main__':main()
