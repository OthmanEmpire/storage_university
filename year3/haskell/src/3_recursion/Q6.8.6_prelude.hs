and :: [Bool] -> Bool
and [] = True 
and (x:xs) | x == True    = Main.and xs
           | otherwise    = False

concat :: [[a]] -> [a]
concat [x:xs] = x:xs
concat (xs:xss) = xs ++ (Main.concat xss)

replicate :: Int -> a -> [a]
replicate 0 _ = []
replicate n a = a : Main.replicate (n-1) a

(!!) :: [a] -> Int -> a
(!!) (x:xs) 1 = x
(!!) (x:xs) n | 0 < n, n < length(x:xs)+1    = (Main.!!) (xs) (n-1)

elem :: Eq a => a -> [a] -> Bool
elem n [] = False
elem n (x:xs) | n /= x    = Main.elem n xs
              | otherwise = True
