with bitems(ItemID) as (
    SELECT DISTINCT ItemID
    FROM Items
    WHERE Currently >= 100
)
SELECT DISTINCT c.Category
FROM Categories c, bitems i
WHERE c.ItemID = i.ItemID