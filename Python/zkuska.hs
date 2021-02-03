data Drive = Contents [Item]
           deriving (Show)

data Item = File String [Int]
          | Dir String Drive
          deriving (Show)


a = Contents [File "./tvoje_mama.hs" [420, 69]]

listFiles :: Drive -> [String]
listFiles (Contents a) = concat (map files a)
    where files (File name _) = [name]
          files (Dir _ driv) = listFiles driv


rotateL :: Int -> [a] -> [a]
rotateL a l =
    let
        i = a `mod` (length l)
    in
    (drop i l) ++ (take i l)



myList = [ s ++ t  | a <- [1..6], let s = take (a-1) (repeat 'a'), let t = take (6-a) (repeat 'b')]

testLex :: (Ord a, Ord b) => [a] -> [b] -> Bool
testLex xs ys = lexi xs ys 0

lexi :: (Ord a, Ord b) => [a] -> [b] -> Int -> Bool
lexi xs ys i
    | i >= (length xs) - 1 = True
    | compare (==) xs = compare (>=) ys
    | compare (>=) xs = True && (lexi xs ys (i+1))
    | otherwise = False
    where compare f lst = f (lst !! i) (lst !! (i+1))
    
data Ingredient = Mozzarella | Salami | Champ | Pepper | Pane | Puree | Cream
                deriving Eq

type Stocks = [InStock]
type InStock = (Ingredient, Int)

inStock :: Stocks -> Ingredient -> Int
inStock ls ing = foldl (+) 0 (map snd (filter ((==ing).fst) ls))

data AndOrTree a = AndNode [AndOrTree a]
                 | OrNode [AndOrTree a]
                 | Leaf a

andOrTreeFold :: ([b] -> b) -> ([b] -> b) -> (a -> b) -> AndOrTree a -> b
andOrTreeFold a o l = go
    where
        go (AndNode ts) = a (map go ts)
        go (OrNode ts)  = o (map go ts)
        go (Leaf x)     = l x

foo :: Eq a => [(a, Bool)] -> a -> Bool 
foo vars str = bar (lookup str vars)
    where bar Nothing = False
          bar (Just b) = b

evalVars :: Eq a => AndOrTree a -> [(a, Bool)] -> Bool     
evalVars tree vars = andOrTreeFold (and) (or) (foo vars) tree