from itertools import combinations,chain
import pandas as pd

df=pd.read_pickle("elementlist.pickle")
abbrs = list(df["abbreviation"])

userInput=str(input("Word to substitute elements for: "))

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def convertToElement(rawWord: str) -> str:
    '''
    Takes in a word and converts it into a combination of chemical elements\n
    Ex:

    convertToElement("Pog") -> Phosphorus Oganesson\n
    convertToElement("Bozo") -> no combination works
    '''
    words=rawWord.lower().split(' ')
    for word in words:
        possibleElements=[]
        for letter in word:
            matchFound=False
            for elem in abbrs:
                if letter in elem:
                    appending=True
                    for char in elem:
                        if char not in word:
                            appending=False
                            break
                    if appending and elem in word:
                        possibleElements.append(elem)
                        matchFound=True
            if not matchFound:
                return "no combination works"
            else:
                continue

        totalComb = "".join(possibleElements)

        if len(totalComb)<len(word):
            return "no combination works"
        
        combinations=list(powerset(possibleElements))
        correctCombination=[]
        for i in combinations:
            if "".join(i)==word:
                correctCombination=list(i)
                break
        
        if correctCombination==[]:
            return "no combination works"
        
        for counter,i in enumerate(correctCombination):
            correctCombination[counter]=df.loc[df["abbreviation"]==i]["name"].values[0]
        
        return " ".join(correctCombination)
                

print(convertToElement(userInput))
