CREATE DATABASE GradePrediction;
USE GradePrediction;

CREATE TABLE Person (
id INT AUTO_INCREMENT NOT NULL,
firstName VARCHAR(15) NOT NULL,
lastName VARCHAR(15) NOT NULL,
studentId INT,
PRIMARY KEY (id),
UNIQUE (firstName, lastName, studentId)
)ENGINE=INNODB;

CREATE TABLE Lecture (
id INT AUTO_INCREMENT NOT NULL,
crn INT NOT NULL,
lectureName VARCHAR(30) NOT NULL,
semester DATETIME NOT NULL,
UNIQUE (crn, semester),
UNIQUE (lectureName, semester),
PRIMARY KEY (id)
)ENGINE=INNODB;

CREATE TABLE Exam (
id INT AUTO_INCREMENT NOT NULL,
lecture INT NOT NULL,
examType VARCHAR(10) NOT NULL,

UNIQUE (lecture, examType),

PRIMARY KEY (id),

FOREIGN KEY (lecture) REFERENCES Lecture (id) 
ON UPDATE CASCADE ON DELETE CASCADE

)ENGINE=INNODB;


CREATE TABLE Question (
id INT AUTO_INCREMENT NOT NULL,
lecture INT NOT NULL,
exam INT NOT NULL,
questionNo INT,
question VARCHAR(300) NOT NULL,

PRIMARY KEY (id),

FOREIGN KEY (lecture) REFERENCES Lecture (id) 
ON UPDATE CASCADE ON DELETE CASCADE,

FOREIGN KEY (exam) REFERENCES Exam (id) 
ON UPDATE CASCADE ON DELETE CASCADE,

UNIQUE (lecture, exam, questionNo)

)ENGINE=INNODB;

CREATE TABLE Answer (
id INT AUTO_INCREMENT NOT NULL,
question INT NOT NULL,
student INT NOT NULL,
content VARCHAR(500) NOT NULL,

PRIMARY KEY (id),

FOREIGN KEY (question) REFERENCES Question(id)
ON UPDATE CASCADE ON DELETE CASCADE,

FOREIGN KEY (student) REFERENCES Person(id)
ON UPDATE CASCADE ON DELETE CASCADE

)ENGINE=INNODB;