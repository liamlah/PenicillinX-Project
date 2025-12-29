# Title: PenicillinX-Project
# Author Dr Liam M Jones
# Date 29/12/25
# Python 3.12.8

# Todo
# 1. Write in python, export to CSV maybe for R visualisation
# 2. maybe separate funciton for each method
# 3. run all functions or select function to run
#	1. for loop over each abx. nil visualisation except for debugging
#	2. copy function from PenicillinX to start
#	3. spits out data for a cross reactivity matrix ?morgan
# 4. ? a way to numerically compare the matrix to the original without having to input the original by hand
# 5. ? Maybe Gemini could read the chart



import pandas as pd
from pathlib import Path


# RDKit imports
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import rdDepictor


abxData = pd.read_csv(Path(__file__).parent / "antibiotics_data.csv")

def start_choices():
    algochoice = int(input("select which algorithm to use\n1.Direct Matching\n2.Dice Similarity\n3.et al.\n#"))
    if algochoice == 1:
        direct_match()
    elif algochoice == 2:
        dice_similarity()
    else:
        print("Please enter a number between 1 and 5!\n")
        start_choices()


def direct_match():
    print("Direct Matching")





def dice_similarity():
    print("Dice Similarity")


start_choices()