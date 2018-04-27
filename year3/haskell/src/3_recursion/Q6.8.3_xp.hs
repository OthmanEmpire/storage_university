(^) :: Int -> Int -> Int
x ^ 0 = 1
x ^ y = x * x Main.^ (y-1)
