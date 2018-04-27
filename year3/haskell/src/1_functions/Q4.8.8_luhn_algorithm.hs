luhnDoub :: Int -> Int
luhnDoub x | 2*x > 9         = 2*x - 9
             | otherwise       = 2*x

luhn :: Int -> Int -> Int -> Int -> Bool
luhn d0 d1 d2 d3 | f d0 d1 d2 `mod` 10 == 0    = True
                 | otherwise                   = False 
                 where f d0 d1 d2 = luhnDoub d0 + luhnDoub d1 + luhnDoub d2
