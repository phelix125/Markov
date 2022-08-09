import numpy
import re
import itertools
from Chain import Chain
class Markov():
    max_depth = 3
    corpus = []
    chain_map = {

    }
    def __init__(self,max_depth, filename) -> None:
        self.max_depth = max_depth
        self.loadCorpus(filename)
        pass

    def loadCorpus(self,filename):
        with open(filename) as f:
            self.corpus = f.readlines()
        self.tokenizeText()
        
    def tokenizeText(self):
        for idx,p in enumerate(self.corpus):
            self.corpus[idx] = re.sub(r'\W+', ' ', p.lower())

        self.mapWords()


            # The part connecting the chains past 1 layer do not work
    def mapWords(self):

        for sentence in self.corpus:
            sentence = sentence.split()
            
            idx = 0
            for word in sentence:
                idx+=1
                if word not in self.chain_map:
                    chain = Chain(word)
                    self.chain_map[word] = chain
                chain = self.chain_map[word]
                #here
                for l in range(self.max_depth):
                    
                    if(l+ idx+1 >= len(sentence)-1): break

                    word = word +" "+ sentence[idx+l]
                    
                    if word not in self.chain_map:
                        chain = Chain(word)
                        self.chain_map[word] = chain
                    
                    chain = self.chain_map[word]
                    
                    chain2 = Chain(sentence[idx+l+1])
                    #print(word)
                    
                   
                    chain.add(chain2)
                    #chain = chain2
                    

    def getTest(self,word):
        c = self.chain_map[word]
        c.calculateProbabilities()
        #c.printFullMap(1)
        c.printMap()

        #for i in range(10):
            #d = c.stochasticGuess()
       
        #for key, value in self.chain_map.items():
            #print(key, ' : ', value.token)
        #d = c.bestGuess()


    def generateSentence(self,og):
        for i in len(5):
            print("hello")

    def printAll(self):
        for key, value in self.chain_map.items():
            print(key, ': ', value , " : ", value.stochasticGuess())

    def listToString(self,list):
        s = ""
        for i in list:
            s = s + i + " "
        return s

    def predict(self,sentence):
        sentence = sentence.split()
        
        idx= 0
        for idx, word in enumerate(sentence):
             sentence = sentence[-self.max_depth+idx:]
             check = self.listToString(sentence)
             print(check)
             if(check in self.chain_map):
                 print("ENTERED " + check)
                 chain = self.chain_map[sentence]
                 d = chain.stochasticGuess()
                 print("PRED" + d.text)

            

    def propagate(self,sentence, word,idx):
        chain = self.chain_map[word]
        #print(chain.text)
        
            




    

m = Markov(3,"Corpus.txt")
#m.getTest("dog")
#m.printAll()

m.predict("found to")
