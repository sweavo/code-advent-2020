import Data.List as List

example1=[ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]

example2=[ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 
    11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]

day10input = [ 38, 23, 31, 16, 141, 2, 124, 25, 37, 147, 86, 150, 99, 75, 81, 
    121, 93, 120, 96, 55, 48, 58, 108, 22, 132, 62, 107, 54, 69, 51, 7, 134, 
    143, 122, 28, 60, 123, 82, 95, 14, 6, 106, 41, 131, 109, 90, 112, 1, 103, 
    44, 127, 9, 83, 59, 117, 8, 140, 151, 89, 35, 148, 76, 100, 114, 130, 19, 
    72, 36, 133, 12, 34, 46, 15, 45, 87, 144, 80, 13, 142, 149, 88, 94, 61, 
    154, 24, 66, 113, 5, 73, 79, 74, 65, 137, 47 ]

-- thanks, Jack.
prepare input = List.sort ([0, 3 + maximum input] ++ input)

-- Design notes: we want to make a single pass through the input. Because of
-- lazy evaluation we can regard list expressions as iterators.  First we find
-- for each element of the input the number of preceding elements that were 
-- within the constraint of 3 jolts.  Then we run a stack machine over those
-- numbers that sums x[i] numbers from the stack and pushes the result.

-- stack machine that consumes input, applying the given function to transform
-- the stack each time. The return value is the eventual head of the stack. 
stack_machine fn stack []       = head stack
stack_machine fn stack (h:tail) = stack_machine fn (fn h stack) tail 

-- range_check accepts a range and returns a function that tests whether an 
-- ordered list is within it.
range_check range xs = last xs - head xs <= range

-- return a list that matches condition, removing elements from the head as 
-- necessary.
behead_until cond items | cond items = items
                        | otherwise  = behead_until cond (drop 1 items)

-- For each element in list, return the list ending at that element that 
-- satisfies condition cond.
conformingSubsequences cond _ [] = [] -- no more input
conformingSubsequences cond previous (h:tail) = 
    let candidate = behead_until cond (previous ++ [h])
    in candidate:conformingSubsequences cond candidate tail


length_minus_one xs = length xs - 1
subsequenceLengths xs = map length_minus_one (conformingSubsequences day10_2_rule [] xs )

day10_2_fn h stack | 0 == length stack = [1] -- first item has one route to it.
                   | otherwise         = (sum (take h stack)):stack

day10_2_rule = range_check 3
day10_2_machine = (stack_machine day10_2_fn []).subsequenceLengths.prepare

tests = [
    behead_until (range_check 4) [0, 2, 3, 5, 7] == [3, 5, 7],
    behead_until (range_check 5) [0, 2, 3, 5, 7] == [2, 3, 5, 7],
    take 3 ['a','b','c','d'] == ['a','b','c'],
    conformingSubsequences (range_check 3) [] [0, 2, 3, 5, 8, 9] == [[0], [0,2],[0,2,3],[2,3,5],[5,8],[8,9]],
    conformingSubsequences (\x -> 3 > length x) [] [0, 2, 3, 5, 8, 9] == [[0], [0,2],[2,3],[3,5],[5,8],[8,9]],
    day10_2_machine example1 == 8,
    day10_2_machine example2 == 19208,
    day10_2_machine day10input == 3543369523456
    ]

