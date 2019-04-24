from TextDistance import TextDistance as textd
import pandas as pd

if __name__ == "__main__":
    answers = ["you are a horse.", "are you a horse", "  ", "we are horses.", "you are a rising sun", "house of a rising sun the"]
    ref = "a horse is a monkey"

    textd.constructTrainingData(answers, ref)