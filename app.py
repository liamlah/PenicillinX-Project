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
from pandas.core.interchange.dataframe_protocol import DataFrame
#from pathlib import Path


# RDKit imports
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

#from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import rdDepictor


abxData = pd.read_csv("antibiotics_data.csv")
ABxList = abxData["Antibiotic"].tolist()

def start_choices():
    #algochoice = int(input("select which algorithm to use\n1.Direct Matching\n2.Dice Similarity\n3.et al.\n#"))
    algochoice = int(1) # Delete after troubleshooting
    if algochoice == 1:
        direct_match3()
    elif algochoice == 2:
        dice_similarity()
    else:
        print("Please enter a number between 1 and 5!\n")
        start_choices()


def direct_match3():
    print("Direct Matching...")

    mol_series = abxData.set_index("Antibiotic")["SMILESR1"].apply(
        lambda x: Chem.MolFromSmiles(x) if pd.notna(x) else None
    )

    names = ABxList
    matrix_df = pd.DataFrame(0, index=names, columns=names)

    for row_name in names:
        row_mol = mol_series[row_name]
        if row_mol is None:
            continue

        # Check both directions: A contains B OR B contains A
        matrix_df.loc[row_name] = mol_series.apply(
            lambda col_mol: 1 if (col_mol and row_mol and (
                row_mol.HasSubstructMatch(col_mol) or
                col_mol.HasSubstructMatch(row_mol)
            )) else 0
        )

    matrix_df.to_csv('direct_match3.csv', sep=',', index_label='Antibiotic')
    return matrix_df



def RDKit_Dice():
    print("RPxProjectDocumentDKit Fingerpring with Dice Similarity")

    mol_series = abxData.set_index("Antibiotic")["SMILESR1"].apply(
        lambda x: Chem.MolFromSmiles(x) if pd.notna(x) else None

    )

    names = ABxList
    matrix_df = pd.DataFrame(0, index=names, columns=names)

    for row_name in names:
        row_mol = mol_series[row_name]
        if row_mol is None:
            continue

        # Check both directions: A contains B OR B contains A
        matrix_df.loc[row_name] = mol_series.apply(
            lambda col_mol: 1 if (col_mol and row_mol and (
                row_mol.HasSubstructMatch(col_mol) or
                col_mol.HasSubstructMatch(row_mol)
            )) else 0
        )

    matrix_df.to_csv('RdKitDice.csv', sep=',', index_label='Antibiotic')
    fpgen.GetCountFingerprint(m)
    rdkit.Chem.AtomPairs.Utils.DiceSimilarity(v1, v2, bounds=None)





    start_choices()