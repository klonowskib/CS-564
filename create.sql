DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Bidders;
DROP TABLE IF EXISTS Bids;
DROP TABLE IF EXISTS Sellers;
CREATE TABLE Sellers (
  Rating int,
  UserID VARCHAR(255)
   );
CREATE TABLE Items (
  ItemID VARCHAR(255),
  Name VARCHAR(255),
  Category VARCHAR(255),
  Currently VARCHAR(255),
  Buy_Price VARCHAR(255),
  First VARCHAR(255),
  Number int,
  Seller VARCHAR(255),
  Location VARCHAR(255),
  Country VARCHAR(255),
  Started VARCHAR(255),
  Ends VARCHAR(255)
  );
.separator |
.import /Users/benklonowski/PycharmProjects/PP1/sellers.dat Sellers
DELETE  FROM Sellers WHERE Rating = 10;
SELECT * FROM Sellers;

