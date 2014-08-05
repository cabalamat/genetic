# ts.py

# travelling salesman problem

import random
#random.seed(1,2,3)
whrandom = random

import math

import tsguifun

#---------------------------------------------------------------------
# parameters:

locations = 26
xmax = 100
ymax = 100

az = "abcdefghijklmnopqrstuvwxyz"

minRandDnaLen = 1
maxRandDnaLen = 50
dnaChars = az + "-"

def createLocations():
   result = [ ]
   for i in range(0, locations):
      result.append((random.randint(0,xmax),
                     random.randint(0,ymax)))
   return result   
      
#---------------------------------------------------------------------
# various constants 
 
locs = createLocations()  
  
locs =  [(47, 51), (20, 59), (28, 6), (59, 6), (88, 75), 
   (95, 22), (27, 50), (59, 43), (34, 60), (42, 17), (60, 37), 
   (93, 41), (13, 49), (31, 60), (90, 6), (42, 0), (15, 85), 
   (85, 87), (83, 77), (35, 44), (38, 56), (0, 62), (59, 25), 
   (79, 41), (13, 85), (73, 85)]

      
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# class for a solution to the problem



class TSSolution:
   def __init__(self, locs, solutionStr):
      self.locs = locs
      self.solution = solutionStr
      self.dist = -9999
      
   def cost(self):
      if self.dist == -9999: self.calcCost()
      return self.dist
      
   def calcCost(self):
      total = 0.0
      startAt = self.solution[0]
      for i in range(0, len(self.solution)-1):
         f = self.solution[i]
         t = self.solution[i+1]
         total += self.calcDistanceAB(f, t)
      total += self.calcDistanceAB(t, startAt)
      self.dist = int(total)
         
   def calcDistanceAB(self, f, t):
      p1 = self.getCoords(f)      
      p2 = self.getCoords(t)
      #print "p1 = %s; p2 = %s self.locs = %s" % (p1, p2, self.locs)
      dist2 = pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2)
      return math.sqrt(dist2)     
         
   def getCoords(self, letter): 
      ix = ord(letter) - ord('a') 
      #print "$$ letter = %s ; ix = %s" % (letter, ix)
      result = self.locs[ix] 
      #print "$$ result = %s ; self.locs = %s" % (result, self.locs)
      return result   
   
   def __str__(self):
      return "<TSSolution: %s %d>" % (self.solution, self.cost()) 
    
  
def display(tss):
   g = tsguifun.TSSGuiFun()
   g.writeSolution(tss)
   g.mainloop()
   
    
#---------------------------------------------------------------------
# operations on dna strings

def makeDna(charSet, minlength, maxLength):
   length = whrandom.randint(minlength, maxLength)
   result = ""
   for i in xrange(0, length):
      result += whrandom.choice(charSet)
   return result
   
def mutate(dna):
   result = dna
   if whrandom.randint(1,4) == 1:
      # add new random char
      oldLen = len(result)
      newPosn = whrandom.randint(0, oldLen+1)
      newChar = whrandom.choice(dnaChars)
      result = result[:newPosn] + newChar + result[newPosn:]
      
   if whrandom.randint(1,4) == 1:
      # remove character, if length >= 2
      if len(result) >= 2:
         posn = whrandom.randint(0, len(result)-1)
         result = result[:posn] + result[posn+1:]
      
   if whrandom.randint(1,4) == 1:
      # change randon character
      posn = whrandom.randint(0, len(result)-1)
      newChar = whrandom.choice(dnaChars)
      result = result[:posn] + newChar + result[posn+1:]
      
   return result   
      
def breed(dna1, dna2):
   cutoff = int((whrandom.randint(0, len(dna1))
                  + whrandom.randint(0, len(dna2))) / 2)
   result = dna1[:cutoff] + dna2[cutoff:]
   return result
              


#---------------------------------------------------------------------
# class for an organism that may have a solution   

"""***
Instance variables:
dna - [string] the organisms genotype
sol - [string] the a...z solution, from (dna)
solc - [TSSolution] containing data in (sol); 
   phenotypic representation of (dna)

born - generation when born
par1 - id of parent1
id - id of self

***"""

nextId = 1

class Organism:
   def __init__(self):
      self.dna = ""
      self.sol = None
      self.solc = None
   
   def birth(self, generationNumber, parent1=None, parent2=None):
      global nextId
      self.born = generationNumber
      self.id = nextId
      nextId += 1
      if not parent1:
         # has no parents
         self.dna = makeDna(dnaChars, minRandDnaLen, maxRandDnaLen)
         self.par1 = 0
         self.par2 = 0

      elif parent1 and not parent2:
         # has 1 parent
         self.dna = mutate(parent1.dna)
         self.par1 = parent1.id
         self.par2 = 0
         
      else:
         # has 2 parents
         self.dna = mutate(breed(parent1.dna, parent2.dna))
         self.par1 = parent1.id
         self.par2 = parent2.id
         
   def getCost(self):
      if not self.solc: 
         self.calcSol() 
      return self.solc.cost()     
         
   def calcSol(self):
      """ calculates (sol) and (solc) from (dna) """
      visited = "" # nodes visited, in order
      for ch in self.dna:
         if ch not in visited and ch in az:
            visited = visited + ch
            
      # get nodes not yet visited
      notVisited = ""
      for ch in az:
         if ch not in visited:
            notVisited = notVisited + ch 
            
      # add unvisited nodes to end
      self.sol = visited + notVisited
      
      self.solc = TSSolution(locs, self.sol)
                 
   def __cmp__(self, other):
      return self.getCost() - other.getCost()
   
   def __str__(self):
      parentStr = ""
      if self.par1:
         parentStr = "(#%s)" % self.par1
      s = "<Organism: %s %s\n   #%s%s %s %s >" % (self.solc.solution,
         self.solc.cost(), 
         self.id, parentStr, self.born, self.dna) 
      return s                
                 
            

#---------------------------------------------------------------------

class Habitat:
   pass
   
   
"""***
In an AsexualHabitat, the population reproduces asexually, using the
mutate() function.

Instance Variables:
popSize - size of population
popBreed - the number who breed each generation
scorePolarity - if this is 1, larger scores are better; if it is
   -1, smaller scores are better
pop - list containing the population
gen - generation number   

***"""   
class AsexualHabitat(Habitat):
   
   def __init__(self, popSize =100, popBreed =50, scorePolarity =1):
      self.pop = None
      self.popSize = popSize
      self.popBreed = popBreed
      self.scorePolarity = scorePolarity
      self.gen = 0
      
   def populate(self):
      self.pop = [ ]
      self.gen = 0
      for i in xrange(0, self.popSize):
         org = Organism()
         org.birth(self.gen)
         self.pop.append(org) 
      
   def newGeneration(self):
      self.gen += 1
      self.pop = self.getSortedPopulation()  
      for i in xrange(self.popSize-self.popBreed, self.popSize):
         self.pop[i] = self.makeNewIndividual()
         
   def makeNewIndividual(self):
      # get parent
      parentIx = whrandom.randint(0, self.popBreed-1)
      parent = self.pop[parentIx]
      baby = Organism()
      baby.birth(self.gen, parent)
      return baby      
      
   def getSortedPopulation(self):
      sortedPop = self.pop
      sortedPop.sort()
      if self.scorePolarity > 0: sortedPop.reverse()
      return sortedPop 
      
     

#---------------------------------------------------------------------
# normal main

def main():
   hab = AsexualHabitat(popSize=200, popBreed=100, scorePolarity=-1)
   hab.populate()
   print "********** Initial population **********"
   for org in hab.getSortedPopulation():
      print org
   
   while 1:
      hab.newGeneration()
      print "********** Generation %d **********" % hab.gen
      #for org in hab.getSortedPopulation():
      #   print org
      print hab.getSortedPopulation()[0]
      raw_input()  
  
  
def pr_locs():
   print locs
  

#---------------------------------------------------------------------
# testing

# test TSSolution class

def test_tss():
   tss = TSSolution(locs, "abcdefghijklmnopqrstuvwxyz")
   print tss
   tss2 = TSSolution(locs, "ijkopqrestumvwxyzfghlndcba")
   print tss2
   display(tss)
   
def test_mutate():
   m = "1234567890"
   print m
   for i in range(0,10):
      print mutate(m)
   n = "abcdefghij"
   for i in range(0,10):
      print breed(m,n)
      
 
   

#---------------------------------------------------------------------

if __name__=="__main__": 
   #print createLocations()
   #test_tss()
   #test_mutate()
   pr_locs()
   main()

#end
