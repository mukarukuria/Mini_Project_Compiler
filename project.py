# pip install nltk
import nltk

# Defining the CFG
cfg = nltk.CFG.fromstring("""
    S -> NP VP | Int NP VP | NP VP C S
    NP -> N | D N | D Adj N | NP PP | 'I'
    VP -> V | V NP | V NP PP | V Adv | VP C VP
    PP -> P NP
    Int -> 'Oh' | 'Well' | 'So'
    D -> 'A' | 'An' | 'The'
    N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park' | 'rat' | 'elephant'
    V -> 'saw' | 'ate' | 'walked' | 'run' | 'jumped'
    P -> 'in' | 'on' | 'by' | 'with' | 'under'
    Adj -> 'big' | 'lazy' | 'green' | 'quick'
    Adv -> 'quickly' | 'slowly' | 'lazily'
    C -> 'and' | 'or' | 'but'
""")

sentence = input("Please enter a sentence: ").split()
parser = nltk.ChartParser(cfg)
for tree in parser.parse(sentence):
    tree.pretty_print()