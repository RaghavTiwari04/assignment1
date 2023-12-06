# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

1. Clone this template into a private repository.
2. Please add your partner and `oop-otoz` to the collaborators.
3. Create a new branch called `submission`.
4. Create your code in the `main` branch.
5. Once you are done with the assignment (or earlier), create a pull request from the `main` branch to your `submission` branch and add `oop-otoz` to the reviewers.

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report
Object-Oriented Programming: Assignment 1
Raghav Tiwari (S5085039) &
Rodrigo Sierra (S5111234)
December 6, 2023
MultipleLinearRegression class
This class aims to perform multiple linear regression and get the weights that given a feature matrix
X best predict the truth values of the labels y.
0.1 Constructor
This constructor has only one parameter, self. weights, which contains both the model weights and
the intercept, stored in the first element of the array. This format was chosen because we thought
carrying all the information in just one array was easier.
0.2 Train method
This method gets a numpy matrix X with the information about the features and a numpy array y with the ground truth labels. First of all X and y are checked (with the private method
check dimensions) to see if their dimensions match in which case the program continues to get the
final weights of the model. The exception aims to handle the case where the matrix is singular or
not invertible,
0.3 Predict method
Predicts a value for a new set of features with the previous weights. The exception aims to handle
the case where the dimension of the inputted array does not match the dimension of x, in which
case the programs ask for the array again until it is inputted correctly.
0.4 Get Params method
This is a simple function that transforms a NumPy array into an array that can be written into a
file of any format and returns the same array.
1 RegressionPlotter
This class aims to plot in 2 or 3 dimensions (depending on the user choice) the data points and the
regression line of each set of feature values of a matrix X concerning y.
1.1 Constructor
Gets a set of weights (which contain both the weights of each feature and the intercept) a matrix X
and an array y. There is also the parameter n which is computed with the private method get n()
and calculates the number of features of X. Also there is an exception to turn the program down if
the dimensions of weights, X or y does not match with each other.
1
1.2 Line
This is a private method that just computes a line in the form of m*x + c to calculate the regression
line of each feature. This method is private since the user does not interact with it.
1.3 Plot 2D
This public method plots n 2D plots with their respective regression line and the data points associated with that feature. Works with any value of n and plots the features one by one in a 2 * (n/2)
grid.
1.4 Plot 3D
It also a public method which function is to plot the regression plane of 2 features alongside with
the data points. It only works when the number of features of X is equal to 2.
2 ModelSaver
This class aims to save and load (depending on the user’s choice) the parameters of a previously
computed model on a file on the computer to posteriorly be used in another model. The class
supports three formats, pickle, JSON, and csv.
2.1 Constructor
it has only one parameter that specifies the file format. The default format is csv just because it is
the most commonly used.
2.2 Save parameters
This is a public method that identifies the format of the model and sends it to the private method
designed to handle that file format.
2.3 Load Parameters
It returns an object of the class MultipleLinearregression with the weights retrieved from the file
selected. It also connects with one private method per supported format to retrieve the data.
2.4 Save fileformat
These three private methods have different code implementations but their aim is the same: save
the file in the directory with the model parameters in the given format. There is an exception to
handle unsupported file formats (formats that are not either pickle, JSON or csv)
2.5 Load fileformat
These three private methods also have different but is function is the same: retrieve the model
parameters from the given file and return the method set params() with a list of the retrieved
parameters.
2
2.6 Set params()
This method receives an array and returns an object of the class MultipleLinearRegression with the
same model weights as the parameters received. It is also a private method since the user does not
interact with it
