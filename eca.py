##############################################################################
#                                                                            #
#                           CSI344 ECA PROJECT                               #
#                                                                            #
##############################################################################
#                                           #
#       NAME: OSOTATANEKEENI ETHELBERT KARI #
#       ID: 201700108                       #
#############################################

import random

# VectorAdd() performs vector addition on two vectors and returns a 
# vector
def VectorAdd(a,b):
    ##initialize an empty list called newVector
    ##then use range(len(a)) to iterate through the indices
    ##of the vectors and add them up
    ##then return the newVector list
    assert len(a)==len(b)
    newVector = []
    for i in range(len(a)):
        newVector.append(a[i]+b[i])
    return newVector

# VectorSub() performs vector subtraction on two vectors and returns a 
# vector
def VectorSub(a,b):
    ##initialize an empty list called newVector
    ##then use range(len(a)) to iterate through the indices
    ##of the vectors and subtract them
    ##then return the newVector list
    assert len(a)==len(b)
    newVector = []
    for i in range(len(a)):
        newVector.append(a[i]-b[i])
    return newVector

# VectorMult() performs vector multiplication and returns a scalar 
# (number)
def VectorMult(a,b):
    ##initialize an empty list called newVector and a variable total to store the sum of the multiplied values
    ##then use range(len(a)) to iterate through the indices
    ##of the vectors and multiply them
    ##then add them to the total variable
    assert len(a)==len(b)  ##Check to make sure a and b are of the same length
    newVector = []
    total = 0
    for i in range(len(a)):
        newVector.append(a[i]*b[i])
        total = total + newVector[i]
    return total

# DO NOT MODIFY THIS FUNCTION
def argMax(scores):
        """
        Returns the key with the highest value.
        """
        if len(scores) == 0: return None
        all = scores.items()
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

def MulticlassPerceptronLearning(trainingvectors):
    
    #Initial weight vectors
    weights={'A':[0,0,0],'B':[0,0,0],'C':[0,0,0]}

    #score of class a, b and c
    aScore, bScore, cScore = 0,0,0

    #Iteration number
    iteration = 0
    
    #Keep track of incorrectly classified apples
    incorrectApple = True

    #Current feature vector of the apple
    currentClass = ""

    #To keep track of correct and incorrect classifications
    badApple, goodApple = 0,0

    ##Repeat until all apples are correctly classified
    ##or until a maximum of 1000 iterations has been executed
    while (incorrectApple == True and iteration < 1000):

        ##List of all classified apples
        classified = []

        ##increment the tracker
        iteration+=1

        ##Print iteration number
        print "------------------------ Iteration " + str(iteration) + " ------------------------"

        ##Iterate through all the apples in the training vector
        for feature in trainingvectors:
            #Extract the features (size and color) of the apples
            appleFeatures = [feature[0], feature[1]]

            #Extract the current class of the feature vector
            currentClass = feature[2]

            #Append the threshold to the feature vector
            appleFeatures.append(1)

            ##Multiply the feature vectors with each weight vector
            ##in the 'weights' dictionary

            aScore = VectorMult(appleFeatures, weights['A'])
            bScore = VectorMult(appleFeatures, weights['B'])
            cScore = VectorMult(appleFeatures, weights['C'])

            ##Another dictionary to store the scores in order to
            ##find the class with the highest product
            scores = {'A': aScore,'B': bScore,'C': cScore}

            ##Determine the class with the highest score using
            ##the argMax function

            maxClass = argMax(scores)

            ##Check to make sure the value is correct i.e.
            ##matches with the actual category to which the data belongs

            ##If this is not the case, then correct the weight vectors as follows:
            ##Subtract the feature vector from the predicted weight vector
            ##and add it to the actual (correct) weight vector

            if (maxClass != currentClass):

                print "Bad Apple Found: ", feature

                ##Subtract the feature vector from the predicted weight vector
                subt = VectorSub(weights[maxClass], appleFeatures)

                ##Update the incorrect weight class
                weights[maxClass] = subt

                ##Next, add to the actual weight vector
                addition = VectorAdd(weights[currentClass], appleFeatures)

                ##Update the correct weight class
                weights[currentClass] = addition

                ##Update the 'classified' list to show bad apple
                classified.append("BAD")
                badApple = badApple+1
            else:
                classified.append("GOOD")
                goodApple = goodApple+1

        if "BAD" in classified:
            incorrectApple = True
            
        else:
            incorrectApple = False
            
            
        print "-> Weight Vectors after Iteration ",iteration
        print weights
        print "-->Number of bad apples: ",badApple
        print "-->Number of good apples: ",goodApple

        

    print "Final W:",weights
    return weights
 
def LoadFile(fileName):
    dataFile=open(fileName,"r")

    #List for all the apples
    allApples  = []

    ##First List(Training Data)
    ##Second List (Tessting Data)
    firstList = []
    secondList = []

    #Skip the first line
    next(dataFile)

    #Go through the file line by line
    for line in dataFile:

        #Split the line into a list of items
        linesplit = line.split()

        #Convert and extract the first feature (Color) and store in feature1
        feature1 = float(linesplit[0])
        #Convert and extract the second feature (Size) and store in feature2
        feature2 = float(linesplit[1])

        feature3 = linesplit[2]

        #Add each apple to the list of all apples
        allApples.append([feature1, feature2, feature3])

    #Seed random number generator
    random.seed(2)

    #Randomly shuffle the list
    random.shuffle(allApples)
        
    #Since there arer 120 apples,
    #70% of 120 = 84
    #Therefore, 84 apples in the first list (Training list)
    firstList = allApples[:84]

    ##30% of 120 = 36
    ##Therefore, 36 apples in the second list (Test List)
    secondList = allApples[84:]

    
    #Return both lists
    return firstList,secondList

def Evaluate(weights,appleVectors):
    numapples=len(appleVectors)
    numcorrect=0

    aScore, bScore, cScore = 0,0,0

    print "-------------------- TESTING SET --------------------"
    raw_input("Click Enter to Evalute the training apples...")
    
    #For each apple in the test set
    for apple in appleVectors:
            #Extract the features (size and color) of the apples
            appleFeatures = [apple[0], apple[1]]

            #Extract the current class of the feature vector
            currentClass = apple[2]

            #Append the threshold to the feature vector
            appleFeatures.append(1)

            print "--> Apple being classified: ", apple
            
            ##Multiply the feature vectors with each weight vector
            ##in the 'weights' dictionary
            aScore = VectorMult(appleFeatures, weights['A'])
            bScore = VectorMult(appleFeatures, weights['B'])
            cScore = VectorMult(appleFeatures, weights['C'])

            ##Another dictionary to store the scores in order to
            ##find the class with the highest product
            scores = {
                'A': aScore,
                'B': bScore,
                'C': cScore }

            ##Determine the class with the highest score using
            ##the argMax function
            maxClass = argMax(scores)
            print "     -Highest scoring class: ", maxClass

            ##If the predicted class is the right class
            ##count it as a correctly classified apple
            ##Else
            ##Don't increase the count of correctly classified apples

            if (maxClass == currentClass):
                numcorrect+=1
                
    return round(float(numcorrect)/numapples*100,2)

# DO NOT MODIFY THIS FUNCTION    
def RunExperiment():
    training,testing=LoadFile("data.txt")
    w=MulticlassPerceptronLearning(training)
    score=Evaluate(w,testing)
    
    print "Evaluation Score:",score

RunExperiment()

##############################################################################
#                                                                            #
#                               PERFORMANCE                                  #
#                                                                            #
##############################################################################

#For each iteration, there were correctly classified apples than there were
#incorrectly classified

##After training, only one apple was incorrectly classified
