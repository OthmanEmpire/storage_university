sum :: Num a => [a] -> a
sum [] = 0
sum (x:xs) = x + Main.sum xs

take :: Int -> [a] -> [a]
take 1 (x:xs) = [x]
take n (x:xs) = x : Main.take (n-1) xs

last :: [a] -> a
last [x] = x
last (x:xs) = Main.last xs
