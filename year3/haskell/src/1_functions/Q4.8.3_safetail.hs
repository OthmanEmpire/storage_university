safetail1 :: [a] -> [a]
safetail1 xs = if null xs then [] else tail xs

safetail2 :: [a] -> [a]
safetail2 xs | null xs == False   = tail xs
             | otherwise          = []

safetail3 :: [a] -> [a]
safetail3 (_:xs) = xs
safetail3 (_) = []
