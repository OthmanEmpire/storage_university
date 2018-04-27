{- Using the composition operator (which is associative so not bracketing
needed) along with some additional functions (very well haskelly named) -} 

encode :: String -> [Bit]
encode = concat . map (make8 . int2bin . ord)

channel :: [Bit] -> [Bit] 
channel = id

decode:: [Bit] -> String
decode = map (chr . bin2int) . chop8

transmit :: String -> String
transmit = decode . channel . encode

{- A lovely inefficient but clear implementation involving zip and iterate -}
bin2int :: [Bit] -> Int 
bin2int bits = sum [w*b | (w,b) <- zip weights bits]
               where weights = iterate (*2) 1

{- Derived through tracing the truth in the algebraic structure:
 
That is, given a 4-bit binary string represented in the form [a,b,c,d], we can re-write the binary number in decimal base as:

= a + 2b + 4c + 8d
= a + 2(b + 2c + 4d)
= a + 2(b + 2(c + 2(d + 0))

This form implies that the cons operator can be replaced by a function that takes two arguments and adds them together (the second argument is multiplied by 2 though).
 -}
bin2int :: [Bit] -> Int
bin2int foldr (\x y -> x + 2y) 0

int2bin :: Int -> [Bit 
int2bin 0 = []
in2bin n = n `mod` 2 : int2bin (n `div` 2)

{- Appends an infinite list of 0s ('repeat 0') then takes the first 8 bits. -}
make8 :: [Bit] -> [Bit]
make8 bits = take 8 (bits ++ repeat 0)

{- Good use of the very standard built-in haskell functions ('take', 'drop') -}
chop8 :: [Bit] -> [[Bit]]
chop8 [] = []
chop8 bits = take 8 bits : chop8 (drop 8 bits)
