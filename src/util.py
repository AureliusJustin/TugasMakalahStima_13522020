from reader import readInput

dictionary = set()

class word:
    def __init__(self, word, startIndex, endIndex):
        self.word = word
        self.startIndex = startIndex
        self.endIndex = endIndex

def matrixToWordList(matrix):
    WordList = []
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        j = 0
        while j < width:
            while j < width:
                if matrix[i][j] == '0':
                    j += 1
                else:
                    break
            
            if j == width:
                continue
            else:
                temp = ""
                startIndex = j
                while j < width:
                    if matrix[i][j] != '0':
                        if (matrix[i][j] == '1'):
                            temp += '.'
                        else:
                            temp += matrix[i][j]
                        j += 1
                    else:
                        break
                if (len(temp) > 1):
                    WordList.append(word(temp, (i, startIndex), (i, j-1)))

    for j in range(width):
        i = 0
        while i < height:
            while i < height:
                if (matrix[i][j] == '0'):
                    i += 1
                else:
                    break
            
            if i == height:
                continue
            else:
                temp = ""
                startIndex = i
                while (i < height):
                    if (matrix[i][j] != '0'):
                        if (matrix[i][j] == '1'):
                            temp += '.'
                        else:
                            temp += matrix[i][j]
                        i += 1
                    else:
                        break
                if (len(temp) > 1):
                    WordList.append(word(temp, (startIndex, j), (i-1, j)))

    return WordList                
