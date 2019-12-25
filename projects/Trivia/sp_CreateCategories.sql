CREATE OR ALTER PROCEDURE sp_CreateCategories
	AS
		BEGIN	
		IF OBJECT_ID (N'Categories', N'U') IS NULL 
		BEGIN
			create table Categories(
				CategoryId int primary key,
				CategoryName varchar(40) not null
				)
		END      
	END
GO
