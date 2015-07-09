# example of program that calculates the median number of unique words per tweet.
import sys

#function to compute median of incoming tweets
def compute_median(uniques):
    uniques = sorted(uniques)
    length = len(uniques)
    if length < 1:
        return None
    if not length % 2:
        return float("{0:.2f}".format((sum(uniques[(length/2)-1 : (length/2)+1]))/2.0))
    else:
        return float("{0:.2f}".format(uniques[((length+1)/2)- 1]))
    
def main():
    uniques = list()
    with open(str(sys.argv[1]),"r") as fr,open(str(sys.argv[2]),"w") as fw:
        for line in fr:
            length = len(set(line.split()))
            uniques.append(length)
            median = compute_median(uniques)
            fw.write(str(median)+"\n")
            

if __name__ == '__main__':main()
