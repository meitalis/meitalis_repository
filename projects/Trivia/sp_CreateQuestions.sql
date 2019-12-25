CREATE OR ALTER PROCEDURE sp_CreateQuestions
	AS
		BEGIN	
		IF OBJECT_ID (N'Questions', N'U') IS NULL 
		BEGIN
			create table Questions(
				QuestionId int identity primary key,
				Question varchar(100) not null unique,
				CategoryId int not null,
				DifficultyId int not null,
				TypeId int not null
				constraint FK_Categories_Questions foreign key (CategoryId) references Categories(CategoryId),
				constraint FK_Difficulties_Questions foreign key (DifficultyId) references Difficulties(DifficultyId),
				constraint FK_Types_Questions foreign key (TypeId) references TypesQuestion(TypeId)
				)	
		END      
	END
GO
