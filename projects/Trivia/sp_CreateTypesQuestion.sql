CREATE OR ALTER PROCEDURE sp_CreateTypesQuestion
	AS
		BEGIN	
		IF OBJECT_ID (N'TypesQuestion', N'U') IS NULL 
		BEGIN
			CREATE table TypesQuestion(
				TypeId int primary key,
				TypeDesc varchar(20) not null unique
			)	
	
			INSERT INTO [dbo].TypesQuestion
				(TypeId
				,TypeDesc)
			VALUES (0,'Multiple Choice')
    
			INSERT INTO [dbo].TypesQuestion
				(TypeId
				,TypeDesc)
			VALUES (1,'True/False')
		END
	END
GO

--exec sp_CreateTypesQuestion