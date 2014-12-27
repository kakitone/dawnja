import matplotlib.pyplot as plt

def analyzeLen():
    #filename  = "RH_monkey_all_contigs.fasta"
    filename = "polished_assembly.fasta"  
    
    f = open("../clearSplit/" + filename, 'r')
    tmp = f.readline().rstrip()
    
    mystring = ""
    myContigList = []
    while len(tmp) > 0:
        if tmp[0] != '>':
            mystring = mystring + tmp
        else:
            myContigList.append(mystring)
            mystring = ""
        
        tmp = f.readline().rstrip()
    
    myContigList.append(mystring)
    
    myContigList.pop(0)
    
    lenDistList = []
    for eachitem in myContigList:
        lenDistList.append(len(eachitem))
        
    lenDistList.sort()
    plt.hist(lenDistList, bins=40)
    plt.show()
    
    print len(myContigList)
    
    f.close()



def printHello():
    for i in range(10):
        print "Hello world"


'''
Input : string_graph_3, improved3.fasta, raw_reads.fasta
Output : string_graph_4 with weights [need a data structure to store the weight on node]

Algorithm : 
1. Find your favorite mappers to map read back
    a. MUMmer, Bowtie, bbmap, any that works 
    b. And then write a short parser to parse the results 
2. Calculate count on the abundances 
    a. Aggregate by taking average [put weights on bin along contigs]
    b. Inheritance and a subclass 
3. Find your favorite graphical tool to display 
    a. Use a javascript library [halfviz should just work ! put weight on edge ]

'''

    
def generateAbundanceGraph(folderName, mummerPath):
    print "generateAbundanceGraph"
    
    
folderName, mummerPath = "EcoliTestRun/", "MUMmer3.23/"
generateAbundanceGraph(folderName, mummerPath)

