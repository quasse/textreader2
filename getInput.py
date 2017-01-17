import nltk
import re
import units

def splitSents(graph):
    # This code is copied from http://stackoverflow.com/questions/4576077/python-split-text-on-sentences
    caps = "([A-Z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"

    text = " " + graph + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    # I added a.m. and p.m.
    if "a.m." in text: text = text.replace("a.m.", "a<prd>m<prd>")
    if "p.m." in text: text = text.replace("p.m.", "p<prd>m<prd>")
    if "..." in text: text = text.replace("...", "<prd><prd><prd>")
    text = re.sub("\s" + caps + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + caps + "[.]", " \\1<prd>", text)
    if "\"" in text: text = text.replace(".\"", "\".")
    if "!" in text: text = text.replace("!\"", "\"!")
    if "?" in text: text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


if __name__=="__main__":
    index = units.Index()
    wordNum = sentNum = graphNum = 0
    #Opens file to be read and creates variable of text
    text = open('texts/test_story.txt', 'r').read()

    # Splits text into paragraph
    graphs = text.split("\n")

    for x in graphs:
        if x != "":
            sentences = splitSents(x)
        for y in sentences:
            tokens = nltk.word_tokenize(y)
            tagged = nltk.pos_tag(tokens)
            for z in tagged:
                newWord = units.Word(z, wordNum, sentNum, graphNum)
                index.addWord(newWord, wordNum, sentNum, graphNum)
                wordNum += 1
            sentNum += 1
        graphNum += 1

    index.printText()