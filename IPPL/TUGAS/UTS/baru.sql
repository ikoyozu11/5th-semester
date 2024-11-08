CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Driver (
    DriverID INT PRIMARY KEY,
    DriverName VARCHAR(100) NOT NULL,
    DOB DATE,
    LicenseNumber VARCHAR(50),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Car (
    RegNumber VARCHAR(15) PRIMARY KEY,
    Make VARCHAR(50),
    Color VARCHAR(20),
    Year INT
);

CREATE TABLE Ride (
    RideID INT PRIMARY KEY,
    RideDate DATE,
    RideTime TIME,
    Kilometres FLOAT,
    Status VARCHAR(20),
    CustomerID INT,
    DriverID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (DriverID) REFERENCES Driver(DriverID)
);