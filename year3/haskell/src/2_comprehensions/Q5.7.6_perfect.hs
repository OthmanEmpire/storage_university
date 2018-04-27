factors :: Int -> [Int]
factors n = [y | y <- [1..n], n `mod` y == 0]

perfect :: Int -> [Int]
perfect n = [x | x <- [1..n], sum (init (factors x)) == x]
