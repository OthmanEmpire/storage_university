merge :: Ord a => [a] -> [a] -> [a]
merge [] (y:ys) = y:ys
merge (x:xs) [] = x:xs
merge (x:xs) (y:ys) | x < y        =  x : (merge xs (y:ys))
                    | x >= y       =  y : (merge (x:xs) ys)

halve :: [a] -> ([a],[a])
halve xs = (take h xs, drop h xs) 
               where h = length xs `div` 2

msort :: Ord a => [a] -> [a]
msort [] = []
msort [x] = [x]
msort xs = merge (msort ns) (msort ms)
                   where (ns, ms) = halve xs
