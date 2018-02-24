with bitems(ItemID) as (
    SELECT DISTINCT ItemID
    FROM Items
    WHERE Currently > 100 AND Number > 0
)
SELECT COUNT(DISTINCT Category)
FROM Categories c, bitems i
WHERE c.ItemID = i.ItemID