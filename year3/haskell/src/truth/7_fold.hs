{- Suppose given a list,

	[x0,x1,...,xn] 

which is re-expressed as,

	x0 : (x1 : (x2 : ( ... (xn : ([]) ... )

We can re-express the above when applied to foldl or foldr as, 

	foldr (#) v [x0,x1,...,xn] = x0 # (x1 # (... (xn # v) ...))

	foldl (#) v [x0,x1,...,xn] = (... ((v # x0) # x1) ...) # xn

Where # is the function that replaces the cons operator. 

Both foldr and foldl are applied recursively starting from the head of the list.
Therefore the function (#) can be thought as (\x xs -> something). Although, the first evaluation of foldl is the left most element and of foldr is the right most element.
-}

{- SUM -}

sum' [] = 0
sum' (x:xs) = x + sum' xs

{- [1,2,3] = 1 + (2 + (3 + 0)) -}
sumr :: Num a => [a] -> a
sumr = foldr (+) 0

{- [1,2,3] = ((0+1)+2)+3 -}
suml :: Num a => [a] -> a
suml = foldl (+) 0

{- LENGTH -}

length' :: [a] -> Int
length' xs = 1 + length' (tail xs)

lengthr :: [a] -> Int 
lengthr = foldr (\_ n -> 1+n) 0

lengthl :: [a] -> Int
lengthl = foldl (\n _ -> n+1) 0

{- REVERSE -}

{- Using built-in haskell functions is easier to avoid compile time errors and understand code rather than pure explicit recursion. See the below two definitions for comparison. 
 
Note that it seems the cons operator cannot be used to reverse a list because of the empty list issue. Although, using the ++ concatenation operator works.-} 

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse'' xs ++ [x]

reverse'' :: [a] -> [a]
reverse'' [] = []
reverse'' xs = last xs : (reverse' (init xs))

reversel :: [a] -> [a]
reversel = foldl (\x xs -> xs : x) []

reverser :: [a] -> [a]
reverser = foldr (\x xs ->  xs ++ [x]) []
