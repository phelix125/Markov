from lib2to3.pgen2 import token
import random


class Chain():
    text = ""
    neighbors ={

    }
    def __init__(self, text) -> None:
        self.neighbors = {}
        self.text = text
        pass

    def add(self, word):
        if word in self.neighbors:
            self.neighbors[word] = self.neighbors[word]+1
        else:
            self.neighbors[word] = 1

    def printMap(self):
        for key, value in self.neighbors.items():
            print(key.text, ' : ', value)

    def printFullMap(self,layer):
        self.printMap()
        for key, value in self.neighbors.items():
            print("Next Key: " + key.text +" Layer: " +str(layer))
            c = key
            c.printFullMap(layer+1)
            c.printMap()
        


    def bestGuess(self):
        best = ""
        max = 0
        for key, value in self.neighbors.items():
            if(value > max): 
                max = value
                best = key
        print(best.text)
        return best
    
    
    def stochasticGuess(self):
        num = random.uniform(0, 1)
        
        for key, value in self.neighbors.items():
            num -= value
            if(num <= 0):
                print(key.text)
                return key.text

    
    def calculateProbabilities(self):
        sum = 0
        for key,value in self.neighbors.items():
            sum += value
        for key,value in self.neighbors.items():
            self.neighbors[key] = value/sum

        

    
