
-- | An implementation of a game similar to Boggle (tm Parker Bros)
--   in Haskell.
--
-- Our version of the game has two players, one the human user, the
-- other the computer.  The game is consists of 16 cubes, with each
-- face of a cube showing a letter (a-z).  The cubes are arranged
-- in a 4x4 grid.
-- At the start of each round, the board containing the cubes is
-- "shaken" to randomise the letters shown in the grid.  The player
-- then has to try and construct words by starting from one
-- letter in the grid, and moving to adjacent (horizontal, vertical
-- or diagonal) letters to spell out the word.  The same cube
-- cannot be used more than once within a given word.
-- Play alternates between the two players (the human goes first)
-- for an agreed number of rounds.
-- Players are awarded points depending on the number of letters
-- in each word.  The legality of each word proposed is checked,
-- gainst the board (can the word be formed by moving between the
-- letters shown on the cubes), and secondly against an agreed
-- dictionary (it it a legal English word).  The same word cannot
-- be used twice; once the human player has used a word, it also
-- cannot be used by the computer.
--
-- The game, as implemented here, has some differences between
-- the commercial version, principally (a) the lack of a timer,
-- and (b) different rules for scoring words.


module Main where

import Prelude hiding (Word)
import System.Random
import System.IO (hFlush,stdout)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Data.List (intersperse, intercalate, sort, sortBy, groupBy, (\\))
import Data.Array.IO
import Control.Monad


-- | We are going to choose need random integers between 0 and n-1
--   for some value of n.  As each call to the function returns a
--   different value, random functions can't be pure - instead they
--   are implemented as IO actions.

randomInt :: Int -> IO Int
randomInt n = return . (`mod` n) =<< randomIO


-- | Some type definitions.  A "Letter" is an individual character
--   on a boggle square, a word is a sequence of letters, i.e. a
--   string.

type Letter = Char
type Word   = [Char]


-- | -----------------------------------------------------------------
--   GAME CUBES
-- | -----------------------------------------------------------------

-- | Each boggle cube has 6 faces each with one letter, represented
--   as a list.  One face is always up, i.e. the value of the 'ch'
--   field should always be one of the letters in the 'faces' field.

data Cube = Cube { ch :: Letter
                 , faces :: [Letter]
                 }

-- | To show a cube, we simply show the face that is 'up'.

instance Show Cube where
    show (Cube f _) = show f

-- | The following list of strings define the 6 faces for
--   each of the 16 cubes used in boggle.

cubeFaces = [ "aaeegn", "abbjoo", "achops", "affkps"
            , "aoottw", "cimotu", "deilrx", "delrvy"
            , "distty", "eeghnw", "eeinsu", "ehrtvw"
            , "eiosst", "elrtty", "himnqu", "hlnnrz"
            ]

-- | Given the faces of a cube, construct a Cube value by setting
--   the faces and arbitrarily choosing the first letter as the upmost.

makeCube :: [Letter] -> Cube
makeCube cs = Cube (head cs) cs


-- | Simulate 'rolling' a cube by choosing one of the 6 faces
--   at random.  As random choice is involved, this is an IO action.

roll :: Cube -> IO Cube
roll (Cube _ chars) = do { face <- randomInt 6
                         ; return $ Cube (chars!!face) chars
                         }


-- | -----------------------------------------------------------------
--   THE GAME GRID (BOARD)
-- | -----------------------------------------------------------------

-- | The Boggle game board is a 4x4 grid of cubes.  We implement the
--   board using a list of lists of cubes.  The type Square is used
--   to refer to specific positions on the grid.

type Square = (Int,Int)
type Grid   = [[Cube]]


-- | Represents the shown face of the cube which has 
--   a specific position on the grid and a letter 

data Face = Face { ch' :: Letter
                 , pos :: Square
                 }

instance Show Face where
    show (Face f pos) = show (f, pos)


-- | Convert a grid to a string for printing.

showGrid :: Grid -> String
showGrid g = intercalate "\n" [ intersperse ' ' (map ch r) | r <- g ]


-- | Extracts all the letters shown on the grid.

getLetters :: Grid -> [Letter]
getLetters g = [ch c | c <- concat $ g]


-- | Construct a grid from a list of cubes (it is assumed there are 16 cubes in the list.)

makeGrid :: [Cube] -> Grid
makeGrid [] = [] 
makeGrid cs = [row] ++ makeGrid rem
              where (row, rem) = splitAt 4 cs


-- | Convert a grid to another representation where only the shown faces are of concern. 

makeFaces :: Grid -> [Face]
makeFaces g = concat [[Face (ch c) (i,j)
                     | (c, i) <- zip cs [1..]] 
                     | (cs, j) <- zip g [1..]]


-- | For each letter in the given word, finds the positions of faces with the same letter.

matchFaces :: Word -> [Face] -> [Layer]
matchFaces w fs = [matchLetter c fs | c <- w] 
                 where matchLetter c fs = [pos f | f <- fs, ch' f == c]


-- | Check whether the word can be placed on the grid.
--   Words may not use a given cube more than once,
--   and the checking of words must respect the
--   requirement that each letter must be adjacent to
--   the previous one; boils down into a double graph theory problem.

checkWord :: Word -> Grid -> Bool
checkWord w g = hasNTree . makeLTrees . matchFaces (replaceQu w) . makeFaces $ g


-- | Simulate shaking the board, by randomly rearranging the
--   cubes on the board.  The orientation of each cube should
--   also be randomized using the "roll" function.

shake :: Grid -> IO Grid
shake g = do { cs <- sequence . map roll . concat $ g 
             ; cs' <- shuffle cs
             ; return . makeGrid $ cs'
             }


-- | Replaces a "qu" in the word by a single "q".

replaceQu :: Word -> Word
replaceQu [] = []
replaceQu (c:cs)
    | c == 'q'      = c : replaceQu (tail cs)
    | otherwise     = c : replaceQu cs


-- | Courtesy of https://wiki.haskell.org/Random_shuffle
-- | Randomly shuffle a list
--   /O(N)/
shuffle :: [a] -> IO [a]
shuffle xs = do
        ar <- newArray n xs
        forM [1..n] $ \i -> do
            j <- randomRIO (i,n)
            vi <- readArray ar i
            vj <- readArray ar j
            writeArray ar j vi
            return vj
  where
    n = length xs
    newArray :: Int -> [a] -> IO (IOArray Int a)
    newArray n xs =  newListArray (1,n) xs


-- | -----------------------------------------------------------------
--   GRAPH THEORY 
-- | -----------------------------------------------------------------

-- | There are two graphs of interest: 
--   * Type1: A tree where the nodes represent a letter and the value of 
--   the nodes have coordinates of the cube that has that letter. This tree
--   shows one permutation of cube choices for a given word.
--   * Type2: A tree where the nodes in it have the condition that the 
--   value of the nodes (coordinates) are neighbouring cubes on the grid. 

--   The node type represents a vertex of a graph where its value 
--   corresponds to the coordinate of a cube. The layer type represents a 
--   single layer within a tree. LTree is of Type1 tree and NTree is of
--   Type2 tree.

type Node = Square
type Layer = [Node]
type LTree = [Node]
type NTree = [Node]


-- | Generates all the possible trees from connecting only consecutive layers. 
--   This can be used to construct all possible cube choices for a given word
--   such that every letter in the word corresponds to a single cube.

makeLTrees :: [Layer] -> [LTree]
makeLTrees ls = sequence ls
                      

-- | Checks if there is atleast one valid NTree in the list of LTree. 

hasNTree :: [LTree] -> Bool
hasNTree ts = or [length (toNTree t) == length t | t <- ts]


-- | Attempts to converts between two types of trees.
--   valid ONLY if the amount of nodes in both trees are equal.

toNTree :: LTree -> NTree
toNTree [] = [] 
toNTree (n:ns) = addNode n (toNTree ns)


-- | Adds the given node to the tree if it is a neighbour.

addNode :: Node -> NTree -> NTree
addNode n t 
    | isConnect n t       = t ++ [n]
    | otherwise           = t 


-- | Checks whether the value of the node is a neighbour of the nodes in the tree.

isConnect :: Node -> NTree -> Bool
isConnect n [] = True
isConnect n t = or [isNeighbour n n' | n' <- t]


-- | Checks if the value (coordinates) of two nodes are neighbours. 
--   Neighbours are nodes that have coordinates of no more 
--   than 1 unit away in both axis.

isNeighbour :: Node -> Node -> Bool
isNeighbour n1 n2 
    | and [dx <= 1, dy <= 1]    = True
    | otherwise                 = False
        where
           (x1, y1) = n1
           (x2, y2) = n2
           [dx, dy] = map abs [x2-x1, y2-y1]


-- | -----------------------------------------------------------------
--   DICTIONARIES
-- | -----------------------------------------------------------------

-- | A forward dictionary is implemented as a Trie, providing fast
--   testing for whether a sequence of letters forms a word.
--   An inverse dictionary is a list of pairs.  Each pair consists
--   of a word, and the sorted list of letters that make up the word.
--   The inverse dictionary is structured into sublists of words of
--   the same length, in decreasing order of size.

data Trie a = Trie Bool (M.Map Letter (Trie a))
type Dictionary    = Trie Letter


-- | Build a singleton trie from a list of letters.

singleton :: [Letter] -> Trie Letter
singleton []     = Trie True M.empty
singleton (c:cs) = Trie False (M.insert c (singleton cs) M.empty)

-- | Merge two tries into one.

merge :: Trie Letter -> Trie Letter -> Trie Letter
merge (Trie fa as) (Trie fb bs)
    = Trie (fa||fb) (M.unionWith merge as bs)

-- | Test whether a trie contains a given word.
contains :: Trie Letter -> Word -> Bool
(Trie f _) `contains` [] = f
(Trie _ m) `contains` (c:cs)
    = case M.lookup c m of
        Nothing -> False
        Just t' -> t' `contains` cs


-- | Map a trie back to the list of legal words it contains.
flatten :: Trie Letter -> [Word]
flatten t = flat [] t
            where
               flat prefix (Trie valid rest)
                   | valid     = reverse prefix : (concatMap continue $ M.assocs rest)
                   | otherwise = concatMap continue $ M.assocs rest
                                 where continue (c,t) = flat (c:prefix) t


-- | Load a list of words from file, constructing both
--   the forward and inverse dictionary.  The forward
--   dictionary is built by converting each word to a
--   singleton trie and then merging the tries.  The
--   inverse dictionary takes the list of words, sorts
--   them by size, and then clusters to the words by length.

loadDictionary :: String -> IO Dictionary
loadDictionary fn
    = do { c <- readFile fn
         ; let wds = words c
         ; let trie = foldl (\ta wb -> merge ta (singleton wb)) (Trie False M.empty) wds
         ; return trie
         }


-- | Constructs the inverse dictionary.

invertDictionary :: Dictionary -> [([Letter], Word)]
invertDictionary dict = [(sort w, w) | w <- flatten dict]


-- | Possible results of playing a word:

data Result = AlreadyUsed   -- the word was already played (by another player, or more embarrassingly yourself!)
            | NotAWord      -- the word isn't a legal English word
            | NotOnGrid     -- the word can't be constructed from the given grid
            | Legal Int     -- its legal, and scores the value specified.

showResult :: Result -> String
showResult AlreadyUsed = " has already been used."
showResult NotAWord    = " is not a legal word."
showResult NotOnGrid   = " cannot be made using the grid."
showResult (Legal v)   = " scores " ++ show v ++ " points."


-- | Given a list of words generated by a player, a dictionary, and
--   the state of the board, determine the result for each word.

score :: Dictionary -> Grid -> [Word] -> [Word] -> [(Word, Result)]
score dict g _ ws = unis ++ dups  
                    where
                       unis = [(w, wordResult w dict g) | w <- ws] 
                       us = S.toList . S.fromList $ ws 
                       ds  = ws \\ us
                       dups =  zip ds . replicate (length ds) $ AlreadyUsed


-- | Computes the Result type of a single word.

wordResult :: Word -> Dictionary -> Grid -> Result
wordResult w dict g 
    | not $ contains dict w    = NotAWord
    | not $ checkWord w g      = NotOnGrid
    | otherwise                = Legal (wordPoints w)
    where
       wordPoints w
           | n < 4      = 0 
           | n == 4     = 1
           | n == 5     = 3
           | otherwise  = n
           where n = length w


-- | Write each word and the corresponding game result to the display.

showScore :: [(Word, Result)] -> IO ()
showScore turn = mapM_ showRes turn
                 where showRes (w,r) = putStrLn $ w ++ "\t" ++ showResult r


-- | -----------------------------------------------------------------
--   GAME STATE
-- | -----------------------------------------------------------------

data Game = Game { dict     :: Dictionary         -- fast lookup to determine if word is legal
                 , board    :: Grid               -- the state of the game grid
                 , played   :: [Word]             -- the words played within the current round
                 , rounds   :: Int                -- number of rounds left to play
                 , human    :: Int                -- the human player's score (i.e. yours!)
                 , computer :: Int                -- the computer player's score.  Probably >> human!
                 }


humanTurn :: Game -> IO Game
humanTurn (Game dict board _ rs h c)
    = do { putStrLn "Your turn. Enter words, newline when complete:"
         ; played <- interact []
         ; let value = score dict board [] played
         ; let total = sum [v | (_, Legal v) <- value]
         ; let used  = [w | (w, Legal _) <- value]
         ; putStrLn ""
         ; putStrLn $ "You score the following:"
         ; showScore value
         ; putStrLn $ "Your score is " ++ show total
         ; return $ Game dict board used rs (h + total) c
         }
      where
         interact ws = do { ln <- getLine
                          ; case ln of
                              "" -> return ws
                              wd -> interact (wd:ws)
                          }


-- | -----------------------------------------------------------------
--   THE COMPUTER OPPONENT
-- | -----------------------------------------------------------------


computerTurn :: Game -> IO Game
computerTurn (Game dict board _ rs h c)
    = do { 
         -- Computing words to play
           let ls = sort . getLetters $ board
         ; let iDict = invertDictionary dict
         ; let ws = [w | (ls', w) <- iDict, isSubstring ls ls']
         ; let play = [w | w <- ws, checkWord w board]

         -- Playing the words
         ; let value = score dict board [] play
         ; let total = sum [v | (_, Legal v) <- value]
         ; let used  = [w | (w, Legal _) <- value]

         -- Showing results
         ; putStrLn ""
         ; putStrLn $ "The computer scores the following:"
         ; showScore value
         ; putStrLn $ "The computer score is " ++ show total
         ; return $ Game dict board used rs h (c + total)
         }


-- | Checks whether the first list of letters contains the second list of letters.

isSubstring :: [Letter] -> [Letter] -> Bool
isSubstring ls1 ls2 
    | n1 == (n2 + n3)    = True
    | otherwise          = False
    where
       n1 = length ls1
       n2 = length ls2
       n3 = length ls3
       ls3 = ls1 \\ ls2


-- | -----------------------------------------------------------------
--   GAMEPLAY
-- | -----------------------------------------------------------------


-- | Play a single round of the game.  If there is still at least one
--   round to play, first the human player is invited to play, then the
--   computer player.  If all rounds are gone, the winner is declared.

playRound :: Game -> IO ()
playRound game
    | rounds game > 0 = do { grid <- shake (board game)
                           ; putStrLn ""
                           ; putStrLn "Next round beginning, here is the board:"
                           ; putStrLn ""
                           ; putStrLn $ showGrid grid
                           ; grid1 <- humanTurn (game {board = grid})
                           ; grid2 <- computerTurn grid1
                           ; playRound (grid2 {played = [], rounds = rounds game - 1})
                           }

    | otherwise = do { let hscore = human game
                     ; let cscore = computer game
                     ; putStrLn ""
                     ; putStrLn "GAME OVER! Final scores: "
                     ; putStrLn $ "  You: " ++ show hscore
                     ; putStrLn $ "  Me : " ++ show cscore
                     ; if hscore >= cscore
                       then putStrLn "Congratulations, you win!"
                       else putStrLn "I win!"
                     }


-- | Kick things off by creating the dictionaries and setting up the
--   game state.

main :: IO ()
main = do { dict <- loadDictionary "words.txt"
          ; let board = makeGrid $ map makeCube cubeFaces
          ; putStr "How many rounds to play? "
          ; hFlush stdout
          ; rounds <- return . read =<< getLine
          ; playRound $ Game dict board [] rounds 0 0
          ; putStrLn ""
          ; putStrLn "Goodbye, thank you for playing."
          }
