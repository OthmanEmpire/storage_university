euclid :: Int -> Int -> Int
euclid x y | x > y        = euclid (x - y) y
           | x < y         = euclid x (y - x)
           | x == y       = x
