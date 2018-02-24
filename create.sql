DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Bidders;
DROP TABLE IF EXISTS Bids;
DROP TABLE IF EXISTS Sellers;
DROP TABLE IF EXISTS Categories;
CREATE TABLE Sellers(
  UserID VARCHAR(255),
  Rating int,
  Location varchar(255),
  PRIMARY KEY (UserID)
   );
CREATE TABLE Items(
  ItemID int,
  Name VARCHAR(255),
  Currently REAL,
  Buy_Price REAL,
  First REAL,
  Number int,
  Seller VARCHAR(255),
  Location VARCHAR(255),
  Country VARCHAR(255),
  Started VARCHAR(255),
  Ends VARCHAR(255),
  Description VARCHAR(10000),
  PRIMARY KEY (ItemID),
  FOREIGN KEY (Seller) REFERENCES Sellers(UserID)
  );
CREATE TABLE Bids(
  Bidder VARCHAR(255),
  Time VARCHAR(255),
  Amount REAL,
  ItemID int,
  FOREIGN KEY (Bidder) REFERENCES Bidders(UserID),
  FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);
CREATE TABLE Bidders(
  Location varchar(255),
  Country varchar(255),
  UserID varchar(255),
  Rating int,
  PRIMARY KEY (UserID)
);
CREATE TABLE Categories(
  Category varchar(255),
  ItemID int
);