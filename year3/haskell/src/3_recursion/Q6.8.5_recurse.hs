length :: [a] -> Int
length [_] = 1
length (_:xs) = 1 + Main.length xs

drop :: Int -> [a] -> [a]
drop 0 xs     = xs
drop n (_:xs) = Main.drop (n-1) xs

init :: [a] -> [a] 
init [_]    = []
init (x:xs) = x : Main.init xs
