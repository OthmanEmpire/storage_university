pset :: [a] -> [[a]]
pset [] = [[]]
pset (x:xs) = [x:ps | ps <- pset xs] ++ pset xs
