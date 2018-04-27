(||) :: Bool -> Bool -> Bool
(||) x y = if x == True then
              if y == True then True else True
           else 
              if y == True then True else False
