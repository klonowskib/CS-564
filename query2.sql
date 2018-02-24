SELECT COUNT(UserID), Location
FROM (
  SELECT UserID, Location FROM Bidders
  UNION
  SELECT UserID, Location FROM Sellers
)
WHERE Location = 'New York'