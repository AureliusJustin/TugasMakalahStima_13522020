from reader import readInput
from util import matrixToWordList
import re
from algorithm import UCS, GBFS, Astar, State
import util
import itertools
from time import time

def main():
    try:
        with open("dict/dictionary.txt", "r") as file:
            for word in file:
                util.dictionary.add(word.strip())
    except IOError as e:
        print("dictionary tidak berhasil dibuka!")
        exit()


    while True:
        testFile = input("File input: ")
        pattern = input("Pattern: ").lower()

        patternAnagram = set(["".join(perm) for perm in itertools.permutations(pattern)])
        substrings = set()
        for anagram in patternAnagram:
            length = len(anagram)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    substrings.add(anagram[i:j])

        possibleWords = list(substrings & util.dictionary)
        matrix = readInput("test/"+ testFile)
        startState = State(matrix, 0, None, matrixToWordList(matrix), -1, set())

        valid = False
        while (not valid):
            algorithm = input("Algorithm: ")
            if algorithm == "UCS":
                algo = UCS(startState, possibleWords)
                valid = True
            elif algorithm == "GBFS":
                algo = GBFS(startState, possibleWords)
                valid = True
            elif algorithm == "Astar":
                algo = Astar(startState, possibleWords)
                valid = True
        
        start = time()
        results = algo.evaluate()
        elapsed = time() - start

        if (results != None):
            i = 1
            for result in results:
                print("ITERASI " + str(i) + "\n")
                # Get the dimensions of the matrix
                rows = len(result)
                cols = len(result[0]) if result else 0
                
                # Find the maximum length of each column
                max_lengths = [max(len(result[i][j]) for i in range(rows)) for j in range(cols)]
                
                # Print each row of the matrix
                for row in result:
                    # Use string formatting to align the columns
                    row = [' ' if char == '0' else '\u2588' if char == '1' else char for char in row]
                    row = [char.upper() if not char.isupper() else char for char in row]
                    formatted_row = ' '.join('{:{}}'.format(row[i], max_lengths[i]) for i in range(cols))
                    print(formatted_row)
                
                print()
                i += 1
        else:
            print("Hasil tidak ditemukan!")

        print("Time elapsed: " + str(elapsed*1000) + " ms")
        print("Node Visited = " + str(algo.nodes_visited))
            
main()