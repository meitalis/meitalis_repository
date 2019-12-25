CREATE OR ALTER PROCEDURE sp_CreateDifficulties 
	AS
		BEGIN	
		IF OBJECT_ID (N'Difficulties', N'U') IS NULL 
		BEGIN
			CREATE table Difficulties(
				DifficultyId int primary key,
				DifficultyName varchar(20) not null unique
			)
	
			 INSERT INTO [dbo].[Difficulties]
				   ([DifficultyId]
				   ,[DifficultyName])
			 VALUES (0,'Easy')
    
			 INSERT INTO [dbo].[Difficulties]
				   ([DifficultyId]
				   ,[DifficultyName])
			 VALUES (1,'Medium')
	 
			 INSERT INTO [dbo].[Difficulties]
				   ([DifficultyId]
				   ,[DifficultyName])
			 VALUES (2,'Hard') 
		END      
	END
GO

--exec sp_CreateTypesQuestion