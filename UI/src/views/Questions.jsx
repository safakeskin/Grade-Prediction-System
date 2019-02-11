import React from "react";

// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import IconButton from "@material-ui/core/IconButton";

// @material-ui/icons
import LeftArrow from "@material-ui/icons/KeyboardArrowLeft";
import RightArrow from "@material-ui/icons/KeyboardArrowRight";

// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import CustomInput from "components/CustomInput/CustomInput.jsx";
import Button from "components/CustomButtons/Button.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Muted from "components/Typography/Muted.jsx";

import {BACKEND_HOST} from "variables/general"


const styles = {
	cardCategoryWhite: {
		color: "rgba(255,255,255,.62)",
		margin: "0",
		fontSize: "14px",
		marginTop: "0",
		marginBottom: "0"
	},
	cardTitleWhite: {
		color: "#FFFFFF",
		marginTop: "0px",
		minHeight: "auto",
		fontWeight: "300",
		fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
		marginBottom: "3px",
		textDecoration: "none"
	}
};

class Question extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			redirect: false,
			alert: null,
			question: null,
			crn: null,
			lecture: null,
			lectureName: null,
			exam: null,
			examName: null,
			questionNumber: null,
			maxQuestionNumber: null
		};

		this.SubmitAnswer = this.SubmitAnswer.bind(this);
		this.ChangeQuestion = this.ChangeQuestion.bind(this);

	}

	componentDidMount() {
		this.setState({lecture: 1, exam: 2, questionNumber: 1})
		this.GetLectureName(1)
		this.GetExamName(2)
		this.FindQuestionNumber(1,2);
		this.SelectQuestion(1,2,1);
	}

	GetLectureName(lecture) {
		fetch(BACKEND_HOST + "/lecture/" + lecture, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' },
		}).then((response) => response.json()
		).then(data => {
            if (data.success) {
				this.setState({lectureName: data.lecture, crn: data.crn})
				// console.log("lecture is ", data.lecture);
                return data.lecture;
			}
			else {
                console.log("Error (GetLectureName)", data.message)
            }
        }).catch(err => {
            console.log(String(err));
        });
	}

	GetExamName(exam) {
		fetch(BACKEND_HOST + "/exam/" + exam, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' },
		}).then((response) => response.json()
		).then(data => {
            if (data.success) {
				this.setState({examName: data.exam})
				// console.log("exam is ", data.exam);
                return data.exam;
			}
			else {
                console.log("Error (GetExamName)", data.message)
            }
        }).catch(err => {
            console.log(String(err));
        });
	}

	FindQuestionNumber(lecture, exam) {
		fetch(BACKEND_HOST + "/question/count/" + lecture + "/" + exam, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' },
		}).then((response) => response.json()
		).then(data => {
            if (data.success) {
				this.setState({maxQuestionNumber: data.count});
                return data.count;
			}
			else {
                console.log("Error (FindQuestionNumber)", data.message)
            }
        }).catch(err => {
            console.log(String(err));
        });

	}

	SelectQuestion(lecture, exam, questionNo) {
		fetch(BACKEND_HOST + "/question/select/" + lecture + "/" + exam + "/" + questionNo, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' },
		}).then((response) => response.json()
		).then(data => {
            if (data.success) {
				this.setState({question: data.question})
				// console.log("question is ", data.question);
			}
			else {
                console.log("Error (SelectQuestion)", data.message)
            }
        }).catch(err => {
            console.log(String(err));
        });
	}

	SubmitAnswer() {
		console.log(this.state);
		const question_id = this.state.question_id || 2;
		const student_id = this.state.student_id || 1;
		const content = this.state.content || "hfdkjhkdsfjlsj";
		fetch(BACKEND_HOST + "/answer/submit/" + question_id + "/" + student_id + "/" + content, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
		}).then((response) => response.json()
		).then(data => {
            if (data.success) {
				console.log("sdkjashk");
			}
			else {
                console.log("Error (SubmitAnswer)", data.message)
            }
        }).catch(err => {
            console.log(String(err));
        });
	}

	ChangeQuestion(num) {
		var lecture = this.state.lecture;
		var exam = this.state.exam;
		var questionNo = this.state.questionNumber;
		// var max = this.FindQuestionNumber(lecture, exam);
		var max = this.state.maxQuestionNumber;
		var qNo = questionNo + num;

		if (qNo >= 1 && qNo <= max){
			this.SelectQuestion(lecture, exam, qNo);
			this.setState({questionNumber: qNo});
		}
	}

	handleInput = (event) => {
		console.log(event);
	}

	render() {
		const { classes } = this.props;
		let prevButtonShow, nextButtonShow;
		// prevButtonShow = true, nextButtonShow = true;
		if (this.state.questionNumber > 1){
			prevButtonShow = true;
		}
		else{
			prevButtonShow = false;
		}

		if (this.state.questionNumber < this.state.maxQuestionNumber){
			nextButtonShow = true;
		}
		else{
			nextButtonShow = false;
		}

		return (
			<div>
				<GridContainer>
					<GridItem xs={12} sm={12} md={8}>
						<Card>
							<CardHeader color="primary">
								<h4 className={classes.cardTitleWhite}>{this.state.lectureName} {this.state.examName} </h4>
								<p className={classes.cardCategoryWhite}>Fill in the blanks</p>
							</CardHeader>
							<CardBody>
								<GridContainer>
									<GridItem xs={12} sm={12} md={6}>
										<CustomInput
											labelText="First Name"
											id="first-name"
											formControlProps={{
												fullWidth: true
											}}
											inputProps= {{
												onChange: this.handleInput
												
											}}
										/>
									</GridItem>
									<GridItem xs={12} sm={12} md={6}>
										<CustomInput
											labelText="Last Name"
											id="last-name"
											formControlProps={{
												fullWidth: true
											}}
										/>
									</GridItem>
								</GridContainer>
								<GridContainer>
									<GridItem xs={12} sm={12} md={6}>
										<CustomInput
											labelText="Student ID"
											id="student-id"
											formControlProps={{
												fullWidth: true
											}}
										/>
									</GridItem>
									<GridItem xs={12} sm={12} md={6}>
										<CustomInput
											labelText="CRN"
											id="crn"
											formControlProps={{
												fullWidth: true
											}}
										/>
									</GridItem>
								</GridContainer>
								<GridContainer>
									<GridItem xs={12} sm={12} md={12}>
										<Muted className={classes.cardCategory}>Question {this.state.questionNumber}</Muted>
										<p className={classes.description}>
											{this.state.question}
										</p>
									</GridItem>
								</GridContainer>
								<GridContainer>
									<GridItem xs={12} sm={12} md={12}>
										<CustomInput
											labelText="Write your answer here."
											id="answer"
											formControlProps={{
												fullWidth: true
											}}
											inputProps={{
												multiline: true,
												rows: 8
											}}
										/>
									</GridItem>
								</GridContainer>
							</CardBody>
							<CardFooter>
								<GridItem xs={12} sm={12} md={4}>
									{prevButtonShow ?
									<IconButton
										className={classes.button}
										aria-label="Previous Question"
										onClick={() => this.ChangeQuestion(-1)}
									>
										< LeftArrow />
									</IconButton>
									: null }
								</GridItem>
								<GridItem xs={12} sm={12} md={4}>
									<Button
										color="primary"
										onClick={() => this.SubmitAnswer()}
									>
									Submit Answer
                					</Button>
								</GridItem>
								
								<GridItem xs={12} sm={12} md={4}>
									{nextButtonShow ?
									<IconButton
										className={classes.button}
										aria-label="Next Question"
										onClick={() => this.ChangeQuestion(1)}
									>
										< RightArrow />
									</IconButton>
									: null }
								</GridItem>

							</CardFooter>
						</Card>
					</GridItem>
				</GridContainer>
			</div>
		);
	}
}

export default withStyles(styles)(Question);
