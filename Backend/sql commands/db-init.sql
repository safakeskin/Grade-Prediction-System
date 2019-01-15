CREATE DATABASE GradePrediction;
USE GradePrediction;

CREATE USER 'GradePredictor'@'localhost' IDENTIFIED BY '456';
GRANT ALL PRIVILEGES ON * . * TO 'GradePredictor'@'localhost';
flush privileges;


CREATE TABLE Person (
id INT AUTO_INCREMENT NOT NULL,
firstName VARCHAR(15) NOT NULL,
lastName VARCHAR(15) NOT NULL,
studentId INT,
PRIMARY KEY (id),
UNIQUE (firstName, lastName, studentId)
)ENGINE=INNODB;


CREATE TABLE Semester(
id INT AUTO_INCREMENT NOT NULL,
term VARCHAR(10) NOT NULL UNIQUE,
PRIMARY KEY (id)
)ENGINE=INNODB;


CREATE TABLE Lecture (
id INT AUTO_INCREMENT NOT NULL,
crn INT NOT NULL,
lectureName VARCHAR(30) NOT NULL,
semester INT NOT NULL,
year YEAR(4) NOT NULL,

UNIQUE (crn, semester, year),
UNIQUE (lectureName, semester, year),

PRIMARY KEY (id),

FOREIGN KEY (semester) REFERENCES Semester (id)
ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=INNODB;


CREATE TABLE LectureStudent (
id INT AUTO_INCREMENT NOT NULL,
lecture INT NOT NULL,
student INT NOT NULL,

UNIQUE (lecture, student),

PRIMARY KEY (id),

FOREIGN KEY (lecture) REFERENCES Lecture (id) 
ON UPDATE CASCADE ON DELETE CASCADE,

FOREIGN KEY (student) REFERENCES Person (id)
ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=INNODB;


CREATE TABLE ExamType (
id INT AUTO_INCREMENT NOT NULL,
examType VARCHAR(15) NOT NULL UNIQUE,
PRIMARY KEY (id)
)ENGINE=INNODB;


CREATE TABLE Exam (
id INT AUTO_INCREMENT NOT NULL,
lecture INT NOT NULL,
examType INT NOT NULL,
isActive BOOLEAN NOT NULL,

UNIQUE (lecture, examType),

PRIMARY KEY (id),

FOREIGN KEY (lecture) REFERENCES Lecture (id) 
ON UPDATE CASCADE ON DELETE CASCADE,

FOREIGN KEY (examType) REFERENCES ExamType (id) 
ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=INNODB;


CREATE TABLE Question (
id INT AUTO_INCREMENT NOT NULL,
lecture INT NOT NULL,
exam INT NOT NULL,
questionNo INT,
question VARCHAR(300) NOT NULL,

UNIQUE (lecture, exam, questionNo),

PRIMARY KEY (id),

FOREIGN KEY (lecture) REFERENCES Lecture (id) 
ON UPDATE CASCADE ON DELETE CASCADE,

FOREIGN KEY (exam) REFERENCES Exam (id) 
ON UPDATE CASCADE ON DELETE CASCADE
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


INSERT INTO `GradePrediction`.`Person`
(`firstName`,
`lastName`,
`studentId`)
VALUES
("Tugba", "Ozkal", 150120053);

INSERT INTO `GradePrediction`.`Person`
(`firstName`,
`lastName`,
`studentId`)
VALUES
("Safa", "Keskin", 150140137);

INSERT INTO `GradePrediction`.`Person`
(`firstName`,
`lastName`,
`studentId`)
VALUES
("Aziz", "Cetin", 150160515);

INSERT INTO `GradePrediction`.`Semester`
(`term`)
VALUES
("Spring");

INSERT INTO `GradePrediction`.`Semester`
(`term`)
VALUES
("Summer");

INSERT INTO `GradePrediction`.`Semester`
(`term`)
VALUES
("Fall");

INSERT INTO `GradePrediction`.`Lecture`
(`crn`,
`lectureName`,
`semester`,
`year`)
VALUES
(10984, "Analysis of Algorithms I", "1", "2018");

INSERT INTO `GradePrediction`.`LectureStudent`
(`student`,
`lecture`)
VALUES
(1, 1);

INSERT INTO `GradePrediction`.`LectureStudent`
(`lecture`,
`student`)
VALUES
(1, 2);

INSERT INTO `GradePrediction`.`LectureStudent`
(`lecture`,
`student`)
VALUES
(1, 3);

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("quiz-1" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("quiz-2" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("quiz-3" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("quiz-4" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("quiz-5" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("homework-1" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("homework-2" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("homework-3" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("homework-4" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("homework-5" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("midterm-1" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("midterm-2" );

INSERT INTO `GradePrediction`.`ExamType`
(`examType`)
VALUES
("final");

INSERT INTO `GradePrediction`.`Exam`
(`lecture`,
`examType`,
`isActive`)
VALUES
(1, 1, 1);

INSERT INTO `GradePrediction`.`Exam`
(`lecture`,
`examType`,
`isActive`)
VALUES
(1, 2, 1);


INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1,1,1, "What is the difference between heap and stack? Explain it with at most 4 sentences.");


INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1,2,1, "What is the worst case, best case and average case of merge sort?");

INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1,2,2, "What is the worst case, best case and average case of quick sort?");

