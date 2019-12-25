CREATE OR ALTER PROCEDURE sp_CreateAnswers
	AS
		BEGIN	
		IF OBJECT_ID (N'Answers', N'U') IS NULL 
		BEGIN
			create table Answers(
				AnswerId int identity primary key,
				Answer varchar(100) not null,
				QuestionId int not null,
				AnswerType bit not null
				constraint FK_Questions_Answers foreign key (QuestionId) references Questions(QuestionId),
			)	
		END      
	END
GO
