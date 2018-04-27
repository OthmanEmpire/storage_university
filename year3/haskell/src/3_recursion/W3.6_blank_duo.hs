type Grid = [[Char]]
type Square = (Int, Int)
type Puzzle = [(Square, Char)]

blank :: Int -> Int -> Puzzle
blank x y = [((i,j),' ') | i <- [1..x], j <- [1..y]]

update :: Puzzle -> Square -> Char -> Puzzle
update p s c = [(s', c') | (s', c') <- p, s /= s'] ++ [(s, c)]

updateStr :: Puzzle -> [(Square, Char)] -> Puzzle
updateStr p [] = p
updateStr p (u:us) = updateStr (update p (fst u) (snd u)) us

placeH :: Puzzle -> Square -> String -> Puzzle
placeH p s ws = updateStr p [(s,c) | (s,c) <- zip ss ws]
                  where
                    ss = zip [h..(h+n)] (replicate n v)
                    n = length ws
                    (h,v) = s

placeV :: Puzzle -> Square -> String -> Puzzle
placeV p s ws = updateStr p [(s,c) | (s,c) <- zip ss ws]
                  where
                    ss = zip (replicate n h) [v..(v+n)]
                    n = length ws
                    (h,v) = s

toGrid :: (Int, Int) -> Puzzle -> Grid 
toGrid (x,y) p = [[c | (s,c) <- [findS p (i,j) | i <- [1..x]]] | j <- [1..y]]

findS :: Puzzle -> Square -> (Square, Char)
findS p s = head [(s,c) | (s',c) <- p, s == s']
