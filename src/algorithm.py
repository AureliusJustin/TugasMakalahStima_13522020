from abc import ABC, abstractmethod
import heapq, re
from copy import deepcopy, copy
from util import matrixToWordList

class State:
    def __init__(self, matrix, fx, parent, wordList, index, visited):
        self.matrix = matrix
        self.fx = fx
        self.parent = parent
        self.wordList = wordList
        self.index = index
        self.visited = visited

    def __lt__(self, other):
        return self.fx < other.fx

    def get_state(self):
        return self.matrix

    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current.get_state())
            current = current.parent
        return path[::-1]

    def distance_from_root(self):
        distance = 0
        current = self
        while current.parent:
            distance += 1
            current = current.parent
        return distance

    def distance_to_goal(self):
        return len(self.wordList)-self.index

    def get_next_words(self, possible_words):
        matches = []
        for word in possible_words:
            matches.extend(re.findall("\A" + self.wordList[self.index+1].word + "\Z", word))
        return matches

    def set_fx(self, fx):
        self.fx = fx

class Algorithm(ABC):
    def __init__(self, start_state, possible_words):
        self.pq = []
        self.start_state = start_state
        self.nodes_visited = 0
        self.possible_words = possible_words

    def add_next_moves(self):
        raise NotImplementedError

    def evaluate(self):
        while self.pq:
            self.nodes_visited += 1
            current_state = heapq.heappop(self.pq)
            if current_state.index == len(current_state.wordList)-1:
                return current_state.get_path()
            else:
                current_state.visited.add(current_state.wordList[current_state.index].word)
                self.add_next_moves(current_state)
        return None

class Astar(Algorithm):
    def __init__(self, start_state, possible_words):
        super().__init__(start_state, possible_words)
        heapq.heappush(self.pq,start_state)

    def add_next_moves(self, current_state: State):
        next_words = current_state.get_next_words(self.possible_words)
        next_fx = current_state.distance_from_root() + 1 + current_state.distance_to_goal() - 1
        for word in next_words:
            if word not in current_state.visited:
                index = current_state.index+1
                matrix = deepcopy(current_state.matrix)
                nextWord = deepcopy(current_state.wordList[index])
                nextWord.word = word
                if (nextWord.startIndex[0] == nextWord.endIndex[0]):
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0]][nextWord.startIndex[1] + i] = word[i]
                else:
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0] + i][nextWord.startIndex[1]] = word[i]

                heapq.heappush(self.pq, State(matrix, next_fx, current_state, matrixToWordList(matrix), current_state.index+1, current_state.visited.copy()))

class GBFS(Algorithm):
    def __init__(self, start_state, possible_words):
        super().__init__(start_state, possible_words)
        heapq.heappush(self.pq,start_state)

    def add_next_moves(self, current_state: State):
        next_words = current_state.get_next_words(self.possible_words)
        next_fx = current_state.distance_to_goal() - 1
        for word in next_words:
            if word not in current_state.visited:
                index = current_state.index+1
                matrix = deepcopy(current_state.matrix)
                nextWord = deepcopy(current_state.wordList[index])
                nextWord.word = word
                if (nextWord.startIndex[0] == nextWord.endIndex[0]):
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0]][nextWord.startIndex[1] + i] = word[i]
                else:
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0] + i][nextWord.startIndex[1]] = word[i]

                heapq.heappush(self.pq, State(matrix, next_fx, current_state, matrixToWordList(matrix), current_state.index+1, current_state.visited.copy()))

class UCS(Algorithm):
    def __init__(self, start_state, possible_words):
        super().__init__(start_state, possible_words)
        heapq.heappush(self.pq,start_state)

    def add_next_moves(self, current_state: State):
        next_words = current_state.get_next_words(self.possible_words)
        next_fx = current_state.fx + 1
        for word in next_words:
            if word not in current_state.visited:
                index = current_state.index+1
                matrix = deepcopy(current_state.matrix)
                nextWord = deepcopy(current_state.wordList[index])
                nextWord.word = word
                if (nextWord.startIndex[0] == nextWord.endIndex[0]):
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0]][nextWord.startIndex[1] + i] = word[i]
                else:
                    for i in range(len(word)):
                        matrix[nextWord.startIndex[0] + i][nextWord.startIndex[1]] = word[i]

                heapq.heappush(self.pq, State(matrix, next_fx, current_state, matrixToWordList(matrix), current_state.index+1, current_state.visited.copy()))
