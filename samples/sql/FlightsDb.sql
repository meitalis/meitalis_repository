CREATE TABLE Flights(
	FlightNum CHAR(5) PRIMARY KEY
)

CREATE TABLE Departures(
	FlightNum CHAR(5) REFERENCES Flights(FlightNum),
	DepartureDate DATETIME,
	Price MONEY,
	Seats INT,
	PRIMARY KEY (FlightNum, DepartureDate)
)

CREATE TABLE Passengers(
	PassengerId INT PRIMARY KEY,
	FirstName NVARCHAR(20) NOT NULL,
	LastName NVARCHAR(20) NOT NULL
)

CREATE TABLE Bookings(
	PassengerId INT REFERENCES Passengers(PassengerId),
	FlightNum CHAR(5),
	DepartureDate DATETIME,	
	CONSTRAINT FK_Bookings_Departures FOREIGN KEY (FlightNum, DepartureDate) 
		REFERENCES Departures(FlightNum, DepartureDate),
	PRIMARY KEY (PassengerId, FlightNum, DepartureDate)
)

