# Title: PenicillinX-Project
# Author Dr Liam M Jones
# Date 29/12/25
# Python 3.12.8

# Todo
# 1. Write in python, export to CSV maybe for R visualisation
# 2. maybe separate function for each method
# 3. run all functions or select function to run
#	1. for loop over each abx. nil visualisation except for debugging
#	2. copy function from PenicillinX to start
#	3. spits out data for a cross reactivity matrix ?morgan
# 4. ? a way to numerically compare the matrix to the original without having to input the original by hand
# 5. ? Maybe Gemini could read the chart



import pandas as pd
#from pathlib import Path


# RDKit imports
from rdkit import Chem
#from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import rdDepictor


abxData = pd.read_csv("antibiotics_data.csv")
ABxList = abxData["Antibiotic"].tolist()

def start_choices():
    #algochoice = int(input("select which algorithm to use\n1.Direct Matching\n2.Dice Similarity\n3.et al.\n#"))
    algochoice = int(1) # Delete after troubleshooting
    if algochoice == 1:
        direct_match()
    elif algochoice == 2:
        dice_similarity()
    else:
        print("Please enter a number between 1 and 5!\n")
        start_choices()


def direct_match(): # Same algorithm currently used in PenicillinX
    print("Direct Matching")
    matrixData = []

    for firstABx in ABxList:
        rowSmiles = abxData.loc[abxData["Antibiotic"] == firstABx, "SMILESR1"].values[0]
        #print(firstABx)
        rowMol = Chem.MolFromSmiles(rowSmiles) if pd.notna(rowSmiles) else None
        resultsRow = []

        for secondABx in ABxList:
            colSmiles = abxData.loc[abxData["Antibiotic"] == secondABx, "SMILESR1"].values[0]
            colMol = Chem.MolFromSmiles(colSmiles) if pd.notna(colSmiles) else None

            if rowMol and colMol:
                if rowMol.HasSubstructMatch(colMol):
                    resultsRow.append(1) # For the match
                else:
                    resultsRow.append(0)

            else:
                resultsRow.append(0)
                print("you are missing data")

        matrixData.append(resultsRow)
        print(matrixData)





def dice_similarity():
    print("Dice Similarity")


start_choices()