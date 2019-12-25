--DROP PROCEDURE SP_CreateTypesQuestion
--DROP PROCEDURE SP_CreateDifficulties
--drop table Answers
--drop table Questions
--drop table TypesQuestion
--drop table Difficulties
--drop table Categories


--create table Difficulties(
--	DifficultyId int primary key,
--	DifficultyName varchar(20) not null unique
--)


--create table TypesQuestion(
--	TypeId int primary key,
--	TypeDesc varchar(20) not null unique
--)	


--create table Categories(
--	CategoryId int primary key,
--	CategoryName varchar(20) not null
--	)
--
--
--
--create table Questions(
--	QuestionId int identity primary key,
--	Question varchar(100) not null unique,
--	CategoryId int not null,
--	DifficultyId int not null,
--	TypeId int not null
--	constraint FK_Categories_Questions foreign key (CategoryId) references Categories(CategoryId),
--	constraint FK_Difficulties_Questions foreign key (DifficultyId) references Difficulties(DifficultyId),
--	constraint FK_Types_Questions foreign key (TypeId) references TypesQuestion(TypeId)
--)
--
--create table Answers(
--	AnswerId int identity primary key,
--	Answer varchar(100) not null,
--	QuestionId int not null,
--	AnswerType bit not null
--	constraint FK_Questions_Answers foreign key (QuestionId) references Questions(QuestionId),
--)



--insert ques + ans in transaction
--select from data base 
--index - needed?
--views - help?
--store proc