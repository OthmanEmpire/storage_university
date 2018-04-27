import Data.List

m = [ [0,2,4], [1,3,5] ]
n = [ [1,0,3], [2,1,-1] ]
p = [ [1,0], [-1,1], [2,-2] ]

scalarMulti :: Num a => a -> [[a]] -> [[a]]
scalarMulti d mss = [ (\ms -> [d*m | m <- ms]) ms | ms <- mss]

matrixAdd :: Num a => [[a]] -> [[a]] -> [[a]]
matrixAdd mss nss = [ f ms ns | (ms, ns) <- zip mss nss]
                    where f ms ns = [m+n | (m, n) <- zip ms ns]

matrixSet :: Num a => a -> [[a]] -> [[a]]
matrixSet x nss = [ (\ns -> [x | n <- ns]) ns | ns <- nss]

scalarproduct :: Num a => [a] -> [a] -> a
scalarproduct xs ys = sum [x*y | (x,y) <- zip xs ys]

times :: Num a => [[a]] -> [[a]] -> [[a]]
times mss nss = [[f ns' ms | ns' <- nss'] | ms <- mss]
                where nss' = transpose nss
                      f xs ys = scalarproduct xs ys
