from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


if __name__=="__main__":
    InputFile = "input/test.txt"
    OutputFile = "output/test.txt"

    with open(InputFile, "r") as f:
        print(f.read())

    sentences = ["VADER is smart, handsome, and funny."]

    analyzer = SentimentIntensityAnalyzer()
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        #print("{:-<65} {}".format(sentence, str(vs)))