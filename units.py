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
        self.wordList.append(word)
        if word.getWord() in self.dict:
            self.dict[word.getWord()].addIndexes(wordID, sentID, graphID)
        else:
            self.dict[word.getWord()] = word

    def printText(self):
        for x in self.wordList:
            print x.getWord()
            print x.getWordIDs()