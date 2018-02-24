SELECT COUNT(s.UserID)
FROM Sellers s, Bidders b
WHERE s.UserID = b.UserID