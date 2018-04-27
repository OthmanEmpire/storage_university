repl :: Int -> a -> [a]
repl n v = [v | _ <- [1..n]]
