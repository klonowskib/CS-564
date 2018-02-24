WITH stupid(catcount) AS
(
  SELECT COUNT(Category)
  FROM Categories
  GROUP BY ItemID
)

SELECT COUNT(catcount)
FROM stupid
WHERE catcount = 4
