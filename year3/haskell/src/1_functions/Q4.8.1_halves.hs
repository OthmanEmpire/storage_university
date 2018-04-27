halve :: [a] -> ([a], [a])
halve xs = splitAt n xs
             where n = length xs `div` 2
