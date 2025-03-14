from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),                                     # you can be one of them 
    Not(And(AKnight, AKnave)),                               # yet you cant be both 
    Implication(AKnight, (And(AKnight, AKnave)) ),           #  if A is a Knight then the statement will be true
    Implication(AKnight, Not(And(AKnight, AKnave)) ),        #  if A is a Knave then his statemnt will be false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),                                     # you can be one of them 
    Not(And(AKnight, AKnave)), 

    Or(BKnight, BKnave),                                     # you can be one of them 
    Not(And(BKnight, BKnave)), 

    Implication(AKnave, And(Or(AKnave, BKnave), Not(And(AKnave, BKnave))) ),
    Implication(AKnight,(And(AKnave, BKnave))),

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    Or(AKnight, AKnave),                                     # you can be one of them 
    Not(And(AKnight, AKnave)), 

    Or(BKnight, BKnave),                                    
    Not(And(BKnight, BKnave)), 


    Implication(AKnight, Or(And(AKnight, BKnight), And(BKnave, AKnave)) ),

    Implication(AKnave, Not( Or(And(AKnight, BKnight), And(BKnave, AKnave)))),


    Implication(BKnave, Or(And(AKnight, BKnight), And(BKnave, AKnave)) ),

    Implication(BKnight, Not( Or(And(AKnight, BKnight), And(BKnave, AKnave)))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(BKnight, BKnave),                                     # you can be one of them 
    Not(And(BKnight, BKnave)), 

    Implication(BKnight, CKnave),
    Implication(CKnight, AKnight),
    Implication(BKnight, BKnave),

    Implication(BKnave, CKnight)
    
)



def main():

    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
