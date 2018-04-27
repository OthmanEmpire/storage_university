import Data.Char

star :: String -> String 
star x = [f x' | x' <- x]
         where f :: Char -> Char
               f c | elem c vowels    = '*'
                   | otherwise        = c 
                   where vowels = ['a', 'e', 'i', 'o', 'u']
