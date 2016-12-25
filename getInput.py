import nltk

class Word():
    def __init__(self, word, wordID, sentenceID, graphID):
        self.word = word
        self.ids = [[],[],[]]
        self.ids[0].append(wordID)
        self.ids[1].append(sentenceID)
        self.ids[2].append(graphID)

    def addInstance(self, wordID, sentenceID, graphID):
        self.ids[0].append(wordID)
        self.ids[1].append(sentenceID)
        self.ids[2].append(graphID)

    def getWord(self):
        return self.word

    def getInstanceWords(self):
        return self.ids[0]

    def getInstanceSentences(self):
        return self.ids[1]

    def getInstanceGraphs(self):
        return self.ids[2]

if __name__=="__main__":
    #Opens file to be read and creates variable of text
    text = open('texts/test_story.txt', 'r').read()

    newWord = Word("hello",1,2,3)
    print newWord.getWord()
    newWord.addInstance(4,5,6)
    for x in newWord.getInstanceWords():
        print x
    # goes through text and splits and analyzes words