INSERT INTO `GradePrediction`.`Exam`
(`lecture`,
`examType`)
VALUES
(1, "quiz-1");

INSERT INTO `GradePrediction`.`Exam`
(`lecture`,
`examType`)
VALUES
(1, "quiz-2");


INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1, 1, 1,
"What is the difference between heap and stack? Explain it with at most 4 sentences.");

INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1, 2, 1,
"What is the worst case, best case and average case of merge sort?");

INSERT INTO `GradePrediction`.`Question`
(`lecture`,
`exam`,
`questionNo`,
`question`)
VALUES
(1, 2, 2,
"What is the worst case, best case and average case of quick sort?");