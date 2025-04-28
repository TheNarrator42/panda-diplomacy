from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# positive sentiment: compound score >= 0.05
# neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
# negative sentiment: compound score <= -0.05

if __name__=="__main__":
    InputFile = "input/test.txt"
    OutputFile = "output/test.txt"

    with open(InputFile, "r") as f:
        sentences = f.read().split("\n")

    analyzer = SentimentIntensityAnalyzer()
    with open(OutputFile, "w") as f:
        for sentence in sentences:
            vs = analyzer.polarity_scores(sentence)
            print("{:-<65} {}".format(sentence, str(vs)))
            f.write("{:-<65} {}\n".format(sentence, str(vs)))