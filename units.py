class Word():
    def __init__(self, word, wordID, sentenceID, graphID):
        self.word = word[0]
        self.type = word[1]
        self.number = 1
        self.ids = [[],[],[]]
        self.ids[0].append(wordID)
        self.ids[1].append(sentenceID)
        self.ids[2].append(graphID)

    def addIndexes(self, wordID, sentID, graphID):
        self.ids[0].append(wordID)
        self.ids[1].append(sentID)
        self.ids[2].append(graphID)

    def getWord(self):
        return self.word

    def getType(self):
        return self.type

    def getWordIDs(self):
        return self.ids[0]

    def getSentenceIDs(self):
        return self.ids[1]

    def getGraphIDs(self):
        return self.ids[2]

class Index():
    def __init__(self):
        self.wordNum = 0
        self.dict = {}
        self.wordList = []

    def addWord(self, word, wordID, sentID, graphID):
        print "adding word"
        self.wordList.append(word.getWord())
        if word.getWord() in self.dict:
            self.dict[word.getWord()].addIndexes(wordID, sentID, graphID)
        else:
            print word.getWord()
            self.dict[word.getWord()] = word

    def printText(self):
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for x in self.wordList:
            print x
            print self.dict[x].getWordIDs()

        print "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
        for y in self.dict:
            print y
            print self.dict[y].getWordIDs()