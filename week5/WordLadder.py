"""

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Examples:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
output: 0


input: beginWord = "cot", endWord = "cog", wordList = ["hot","hol","dol","dog","cog"]
output: 0



Input: 
   beginWord = "hit"
   endWord   = "cog"
   wordList  = ["lot","hot","cog","dog","dot","log"]

   hit -> hot -> dot -> lot -> log -> cog

Output: 5


Understand: 

we need to get a squence of words that differ by 1 letter 

Match: 
It's a graph problem
represent as an ajecency-list (https://visualgo.net/en/dfsbfs)
use bfs (queue) to travese and return when we find the end word; if qwe do not find the end word return 0

Plan:

   beginWord = "hit"
   endWord   = "cog"
   wordList  = ["lot","hot","cog","dog","dot","log"]
   
{

"hit" -> [hot],
"lot" -> [hot , dot, log]
"hot" -> [dot, lot ,hit],
"cog" -> [dog , log ],
"dog" -> [cog ,dot , log]
"dot" -> [dog , hot , lot],
"log" -> [lot ,cog ,dog ]

}


Solution

LETTERS = set('abcdefghijklmnopqrstuvwxyz')

def word_ladder(start, end, words):
    words = set(words)
    visited = set()
    queue = [(start, 1)] # queue for BFS, which stores the word and distance

    while len(queue) > 0:
        word, length = queue.pop(0)
        if word == end:
            return length
        for i, char in enumerate(word):
            for letter in LETTERS:
                if char != letter:
                    candidate = word[:i] + letter + word[i + 1:]
                    if candidate in words and candidate not in visited:
                        queue.append([candidate, length + 1])
                        visited.add(candidate)
    return 0
    
"""




