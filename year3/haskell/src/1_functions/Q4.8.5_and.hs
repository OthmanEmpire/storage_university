(&&) :: Bool -> Bool -> Bool
(&&) x y = if x == True then
              if y == True then True else False
           else 
              if y == True then False else False
