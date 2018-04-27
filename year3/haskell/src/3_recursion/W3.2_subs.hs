{- Assuming lists are NOT sorted -}
subset1 :: Ord a => [a] -> [a] -> Bool
subset1 [] ys = True
subset1 (x:xs) ys | elem x ys     = subset1 xs ys
                  | otherwise     = False

{- Assuming lists are sorted -}
subset2 :: Ord a => [a] -> [a] -> Bool
subset2 _ [] = False
subset2 [] _ = True
subset2 (x:xs) (y:ys) | x /= y     = subset2 [x] ys
                      | x == y     = subset2 xs ys
