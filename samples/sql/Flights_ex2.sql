--drop table WaitingList
--drop table Bookings
--drop table Passengers
--drop table Departures
--drop table Flighs
--drop table Airlines
--drop table Cities






create table Airlines(
	airline_id int identity primary key,
	airline_name varchar(20) not null
	)

create table Cities(
	city_id int identity primary key,
	city_name varchar(20) not null
	)

create table Flighs(
	flight_number varchar(20) primary key,
	airline_id int not null,
	source_city_id int not null,
	dest_city_id int not null,
	depart_time time not null,
	arrive_time time not null,
	duration float(2) not null,
	seats int check (seats > 0 and seats <=500),
	constraint FK_airline_flight foreign key (airline_id) references Airlines(airline_id),
	constraint FK_srccity_flight foreign key (source_city_id) references Cities(city_id),
	constraint FK_dstcity_flight foreign key (dest_city_id) references Cities(city_id)
)

create table Departures(
	flight_number varchar(20) not null,
	depart_date datetime not null,
	price money not null,
	avail_seats int check (avail_seats > 0 and avail_seats <=500),
	constraint PK_Departure primary key (flight_number,depart_date),
	constraint PK_Departure_Flighs foreign key (flight_number) references Flighs(flight_number)
)
)

create table Passengers(
	pass_id int identity primary key,
	first_name varchar(40) not null,
	last_name varchar(40) not null,
	pass_address varchar(40) ,
	phone varchar(40) ,
	email varchar(40) unique not null
)

create table Bookings(
	pass_id int not null,
	flight_number varchar(20) not null,
	depart_date datetime not null,
	reservation_date datetime default getdate() not null,
	seat_number int check (seat_number > 0 and seat_number <=500),
	constraint PK_Bookings primary key (pass_id,flight_number,depart_date),
	constraint FK_pass_booking foreign key (pass_id) references Passengers(pass_id),
	constraint FK_departure_booking foreign key (flight_number,depart_date) references Departures(flight_number,depart_date)
)

create table WaitingList(
	pass_id int not null,
	flight_number varchar(20) not null,
	depart_date datetime not null,
	number_in_list int not null,
	constraint PK_WaitingList primary key (pass_id,flight_number,depart_date),
	constraint FK_pass_waitingList foreign key (pass_id) references Passengers(pass_id),
	constraint FK_departure_waitingList foreign key (flight_number,depart_date) references Departures(flight_number,depart_date)
)


	