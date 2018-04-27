import Data.Char

type Bit = Int

encode :: String -> [Bit]
encode xs = concat [parity (byte (base 2 (ord x))) | x <- xs]

channel :: [Bit] -> [Bit]
channel (x:xs) | length xs          == 0    = [x]
               | length xs `mod` 20 /= 0    = x : channel xs
               | length xs `mod` 20 == 0    = flipbit x : channel xs

decode :: [Bit] -> String 
decode xs | length ms > 0  =  (chr (denary (check ms))) : decode ns
          | otherwise      = []
          where
            (ms,ns) = splitAt 9 xs

{- Flips a bit -}
flipbit :: Bit -> Bit
flipbit x | x == 0 = 1
       | x == 1 = 0

{- Adds a parity bit -}
parity :: [Bit] -> [Bit]
parity xs | sum xs `mod` 2 == 0    = xs ++ [0]
          | otherwise              = xs ++ [1]

{- Checks and removes the parity bit -}
check :: [Bit] -> [Bit]
check xs | parity (init xs) == xs = init xs
         | otherwise              = error "Transmission Error!"

{- Converts a base 2 number to base 10 
 - The last element is treated as the MSB -}
denary :: [Bit] -> Int
denary xs = sum [x * 2^i | (x,i) <- zip xs ([0..length xs])]

{- Converts a base 10 number to the supplied base.
 - The last element is treated as the MSB -}
base :: Int -> Int -> [Int]
base b x | x > 0     = (x `rem` b) : base b (x `div` b)
              | otherwise = []

{- Converts a list containing 8 or less bits into a list of 8 bits
- The last element is treated as the MSB -}
byte :: [Bit] -> [Bit]
byte xs | n == 8          = xs
        | otherwise       = xs ++ replicate (8-n) 0
        where
          n = length xs
