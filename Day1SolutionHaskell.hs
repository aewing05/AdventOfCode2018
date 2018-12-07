module AdventDay1 where

import qualified Data.Set as S

frequencyPartOne :: [Int] -> Int
frequencyPartOne = sum

frequencyPartTwo :: [Int] -> Int
frequencyPartTwo = getDuplicate S.empty . scanl (+) 0 . cycle
  where
    getDuplicate frequencyLog (x:xs) = if x `S.member` frequencyLog
      then x
      else getDuplicate (S.insert x frequencyLog) xs

main :: IO ()
main = do
  input <- readFile "AdventDay1Input.txt"
  let
    frequencyData = map (read::String->Int) $
      map (dropWhile (== '+')) (lines input)
  print $ frequencyPartOne frequencyData
  print $ frequencyPartTwo frequencyData
