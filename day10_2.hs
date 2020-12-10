import Data.List as List

-- design notes: I'm taking a pass through the _prepare_d data, figuring out 
-- how many of the preceding values I care about and summing the paths to those
-- In the case where the sequence is just [ 0 ], there is only 1 way to get to
-- there, 
example1=[ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]

example2=[ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]

day10input = [115,134,121,184,78,84,77,159,133,90,71,185,152,165,39,64,85,
             50,20,75,2,120,137,164,101,56,153,63,70,10,72,37,
             86,27,166,186,154,131,1,122,95,14,119,3,99,172,111,
             142,26,82,8,31,53,28,139,110,138,175,108,145,58,76,
             7,23,83,49,132,57,40,48,102,11,105,146,149,66,38,155,
             109,128,181,43,44,94,4,169,89,96,60,69,9,163,116,45,
             59,15,178,34,114,17,16,79,91,100,162,125,156,65]

prepare input = List.sort ([0, 3 + maximum input] ++ input)

can_reach a b = ((a + 1) <= b) && (b <= (a + 3))

-- rangechecker accepts a range and returns a function that checks ordered lists
-- are within it
rangechecker range xs = last xs - head xs <= range

-- return a list that matches condition, removing elements from the head as 
-- necessary
beheadUntil condition (h:tail) | condition (h:tail) = (h:tail)
                               | otherwise          = beheadUntil condition tail

-- For each element in list, return the list ending in that element that 
-- satisfies condition.
conformingSubsequences condition [] _ = []
conformingSubsequences condition (h:tail) previous = let candidate = beheadUntil condition (previous ++ [h]) in candidate:conformingSubsequences condition tail candidate

-- design notes: we could pass through the subsequences, adding the last n items of our accumulator and appending to the accumulator where n is the length of the found subsequence. It seems wasteful but I think that's the right approach. Because working at the head is cheaper, I'll accumulate the totals in reverse order.

day10_2_rule = rangechecker 3

subsequenceLengths xs = map length (conformingSubsequences day10_2_rule (prepare xs) [])


routeCount [] (h:tail) = h
routeCount (h:tail) accumulator = routeCount tail ((sum (take h accumulator)):accumulator)


tests = [
    take 3 ['a','b','c','d'] == ['a','b','c'],
    conformingSubsequences (rangechecker 3) [0, 2, 3, 5, 8, 9] [] == [[0], [0,2],[0,2,3],[2,3,5],[5,8],[8,9]],
    routeCount (subsequenceLengths example1) [] == 8,
    routeCount (subsequenceLengths example2) [] == 19208
    ]

day10_2 = routeCount (subsequenceLengths day10input) []

