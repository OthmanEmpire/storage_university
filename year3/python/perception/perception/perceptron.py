"""
Name: Othman Alikhan
SID: 200684094

COMP3611: Machine Learning
Coursework 1: Supervised Learning and Neural Networks

The script implements three main sections:

1. Generation of the machine learning class instances (i.e. the data).
2. Implementation of a single-layer perceptron that linearly classifies.
3. Implementation of a multi-layer perceptron that non-linearly classifies.

The output of sections above are shown visually using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


__author__ = "Othman Alikhan"
__email__ = "sc14omsa@leeds.ac.uk"


class SingleNeuralNetwork:
    """
    Represents a single-layer perceptron in machine learning.

    That is, this class is responsible for implementing a single-layer neural
    network that can be used to classify data that is linearly separable
    under the context of supervised learning.
    """

    def __init__(self, numWeights, eta, targetClassNum):
        """
        A simple constructor.

        :param numWeights: The total number of weights excluding the bias.
        :param eta: The learning rate which should be between 0 to 1.
        :param targetClassNum: The class that the perceptron is attempting to
        classify.
        """
        self.w = np.random.rand(numWeights+1)
        self.w -= 0.5     # Weights within [-0.5, 0.5]
        self.w[0] = -1    # The bias

        self.eta = eta
        self.targetClassNum = targetClassNum

    def train(self, v):
        """
        Trains the single-layer perceptron on the given class instance which
        then updates the weights of the perceptron.

        :param v: The input vector to the neural network system which is a
        0x3 numpy array of the form [x, y, <class_num>].
        """
        v = self.addBiasTerm(v)
        update = self.eta * self.computeError(v) * v[:3]
        self.w += update

    def evaluate(self, D):
        """
        Evaluates the cumulative error (sum of error squared) for all vectors
        (class instances) in matrix D for classifying using the perceptron.

        :param D: A matrix containing entries that represent class
        instances (i.e. Nx3 numpy array of the form [x, y, <class_num>]).
        :return error: A number representing the error.
        """
        error = sum([self.computeError(self.addBiasTerm(v))**2 for v in D])
        return error

    def computeAccuracy(self, D):
        """
        Calculates the accuracy of the perceptron for the given matrix D
        which contains vector inputs.

        :param D: A matrix containing entries that represent class
        instances (i.e. Nx3 numpy array of the form [x, y, <class_num>]).
        :return: The accuracy as a number.
        """
        hit = 0

        for i, v in enumerate(D):
            v, c = self.addBiasTerm(v[:2]), int(v[2])

            predicted = self.activationFunction(np.dot(self.w, v))
            expected = self.binarizeClassNum(c)

            if abs(predicted - expected) == 0:
                hit += 1

        accuracy = hit / len(D)
        return accuracy

    def activationFunction(self, x):
        """
        The activation function for a node in the neural system. In this
        case, the function is the Heaviside step function.

        :param x: A number as input.
        :return: 1 if the input is above the threshold 0 otherwise 0.
        """
        if x > 0:
            return 1
        else:
            return 0

    def computeError(self, v):
        """
        Calculates the classification error for the given class instance.

        :param v: The input vector to the neural network system which is a
        0x3 numpy array of the form [x, y, <class_num>].
        :return: A number representing the classification error.
        """
        # Splitting class data and class number for clarity
        v, c = v[:3], v[3]

        predicted = self.activationFunction(np.dot(self.w, v))
        expected = self.binarizeClassNum(c)
        error = expected - predicted
        return error

    def addBiasTerm(self, v):
        """
        Adds an extra column to the start of the 2D numpy array which
        represents the corresponding element to be multiplied by the bias
        term in the vector w.

        The reason for doing so is to simplify calculations (namely the dot
        product between v and w).

        :param v: The input vector to the neural network system which is a
        0x3 numpy array of the form [x, y, <class_num>].
        :return: The input vector with an added bias term at the start (i.e. A
        0x4 numpy array of the form [1, x, y, <class_num>]
        """
        return np.hstack([np.array([1]), v])

    def binarizeClassNum(self, classNum):
        """
        Defining a function that binarizes the class number. That is, if the
        given class matches the perceptron's target class a 1 is returned
        otherwise 0>

        :param classNum: The class number to classify.
        :return: 1 if the given class number matches the percepton's target
        class number otherwise 0.
        """
        if classNum == self.targetClassNum:
            return 1
        else:
            return 0

    def computeBoundaryCoordY(self, x):
        """
        Calculates the y-coordinate associated with the given x-coordinate.
        The pair of coordinates lie on the hyperplane (a 2D line in this case).

        :param x: The x-coordinate that lies on the boundary of the perceptron.
        :return: The corresponding y-coordinate on the boundary of the
        perceptron.
        """
        return (-self.w[0] - self.w[1] * x) / self.w[2]


class RectClass:
    """
    Represents a machine learning class where each instance is a 2D point
    bounded within a rectangle.
    """

    def __init__(self, xMin, xMax, yMin, yMax, classNum):
        """
        A simple constructor.

        :param xMin: The minimum x coordinate of the geometric rectangle.
        :param xMax: The maximum x coordinate of the geometric rectangle.
        :param yMin: The minimum y coordinate of the geometric rectangle.
        :param yMax: The maximum y coordinate of the geometric rectangle.
        :param classNum: The number associated with the machine class.
        """
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.width = xMax - xMin
        self.height = yMax - yMin
        self.classNum = classNum
        self.instances = None

    def generateInstances(self, amount):
        """
        Generates instances of the machine learning class. In this case,
        these instances are 2D points that are bound within a rectangle.

        :param amount: The number of machine learning class instances to
        generate.
        """
        # The x-coordinates, y-coordinates, and class number respectively
        X = np.random.rand(amount, 1)
        Y = np.random.rand(amount, 1)
        C = np.full((amount, 1), self.classNum, dtype="float")

        # Shifting and scaling the coordinates to fall within the rectangle
        # boundaries
        X = self.xMin + self.width * X
        Y = self.yMin + self.height * Y

        # The instances are stored in a numpy array of form (x, y, <class_num>)
        self.instances = np.hstack((X, Y, C))

    def rotateInstancesBy(self, angle):
        """
        Rotates every machine learning class instance x and y coordinates
        about the origin by the specified angle counter-clockwise.

        Since the instances first two columns correspond to an x and y value,
        they can be treated as vectors. As such, we can rotate all
        these vectors by using matrix multiplication (which this
        method does)

        :param angle: The angle of rotation from the positive x-axis
        counter-clockwise in degrees.
        """
        # Defining rotation matrix
        angle = np.radians(angle)
        c, s = np.cos(angle), np.sin(angle)
        R = np.array([[c, -s], [s, c]])

        # Slicing the first two columns that contain the 2D coordinates
        v = self.instances[:, :2]

        # Applying a matrix transformation to the vectors (rotation)
        v = np.dot(R, v.T).T

        # Overriding the original instances data
        self.instances = np.hstack([v, self.instances[:, 2:]])


class NormClass:
    """
    Represents a machine learning class where each instance is a 2D point
    sampled from a multi-variate normal distribution.
    """

    def __init__(self, mean, cov, classNum):
        """
        A simple constructor.

        :param mean: A list that contains two numbers representing the
        2D coordinate of the mean.
        :param cov: A 2x2 list that represents the covariance matrix. An
        entry C_(i,j) represents the covariance of variables x_i and x_j.
        The covariance must be symmetric and positive-semidefinite otherwise
        generating samples from the normal distribution becomes funny.
        :param classNum: The number associated with the machine class.
        """
        self.mean = mean
        self.cov = cov
        self.classNum = classNum
        self.instances = None

    def generateInstances(self, amount):
        """
        Generates instances of the machine learning class. In this case,
        these instances are 2D points that are sampled from a multi-variate
        normal distribution (2D Gaussian).

        :param amount: The number of machine learning class instances to
        generate.
        """
        # The x and y coordinates
        v = np.random.multivariate_normal(self.mean, self.cov, amount)

        # The class number respectively
        C = np.full((amount, 1), self.classNum, dtype="float")

        # The instances are stored in a numpy array of form (x, y, <class_num>)
        self.instances = np.hstack((v, C))


class MultiNeuralNetwork:
    """
    Represents a multi-layer perceptron in machine learning.

    That is, this class is responsible for implementing a multi-layer neural
    network that can be used to classify data that are not linearly separable
    under the context of supervised learning.
    """

    def __init__(self, eta, nodesInput, nodesHidden, nodesOutput):
        """
        A simple constructor.

        :param eta: The learning rate which should be between 0 to 1.
        :param nodesInput: Number of nodes in input layer in the network.
        :param nodesHidden: Number of nodes in hidden layer in the network.
        :param nodesOutput: Number of nodes in output layer in the network.
        """
        self.eta = eta
        self.inputValues = None
        self.inputClass = None

        # The +1 corresponds to a bias node
        self.layerI = Layer(nodesInput, 0)
        self.layerH = Layer(nodesHidden, nodesInput+1)
        self.layerO = Layer(nodesOutput, nodesHidden+1)

    def train(self, D):
        """
        Trains the multi-layer perceptron on the given matrix which
        contains class instances. This involves a forward phase followed by
        updating the weights through the backward phase.

        :param D: The inputs to the neural network where each entry in the
        Nx3 numpy array contains a class instance of the form
        (x, y, <class_num>)
        """
        for v in D:
            self.inputValues, self.inputClass = v[:2], v[2]

            # Forward pass
            self.layerI.output = self.inputValues
            self.layerH.updateOutput(self.layerI.output)
            self.layerO.updateOutput(self.layerH.output)

            # Backward pass
            self.updateOutputError()
            self.updateHiddenError()
            self.updateOutputWeights()
            self.updateHiddenWeights()

    def evaluate(self, D):
        """
        Evaluates the cumulative total error of the output nodes for all
        vectors (class instances) in matrix D for classifying using the
        perceptron.

        :param D: A matrix containing entries that represent class
        instances (i.e. Nx3 numpy array of the form [x, y, <class_num>]).
        :return error: A number representing the average error over D.
        """
        errorAvg = 0

        for v in D:
            self.inputValues, self.inputClass = v[:2], int(v[2])

            # Forward pass
            self.layerI.output = self.inputValues
            self.layerH.updateOutput(self.layerI.output)
            self.layerO.updateOutput(self.layerH.output)

            # Computing mis-classification error
            errorAvg += self.computeError()

        errorAvg /= len(D)
        return errorAvg

    def classify(self, D):
        """
        Classifies the given vectors (class instances) in the matrix D based
        on the passing it through the neural network.

        :param D: A matrix containing entries that represent class
        instances (i.e. Nx3 numpy array of the form [x, y, <class_num>]).
        :return: A matrix containing entries that represent class
        instances (i.e. Nx3 numpy array of the form [x, y, <class_num>])
        where the class number is predicted by the neural network.
        """
        classifications = np.copy(D)

        for i, v in enumerate(D):
            self.inputValues, self.inputClass = v[:2], int(v[2])

            # Forward pass
            self.layerI.output = self.inputValues
            self.layerH.updateOutput(self.layerI.output)
            self.layerO.updateOutput(self.layerH.output)

            # Stores predicted classification of the vector
            classified = np.argmax(self.layerO.output)+1
            classifications[i, 2] = classified

        return classifications

    def computeError(self):
        """
        Calculates the total error for mis-classification by the neural
        network.

        :return: A number representing the classification error.
        """
        predicted = self.layerO.output
        expected = self.binarizeClassNum(self.inputClass)
        error = 0.5 * sum(predicted - expected)**2
        return error

    def updateOutputError(self):
        """
        Updates the errors of the nodes in the 2nd layer, the output layer.
        """
        y = self.layerO.output
        t = self.binarizeClassNum(self.inputClass)
        self.layerO.errors = y * (1 - y) * (y - t)

    def updateOutputWeights(self):
        """
        Updates the weights of the nodes in the 2nd layer, the output layer.
        """
        for i in range(self.layerO.numNodes):
            a = self.layerH.addBiasTerm(self.layerH.output)
            d = self.layerO.errors[i]
            self.layerO.weights[i] -= self.eta * d * a

    def updateHiddenError(self):
        """
        Updates the errors of the nodes in the 1st layer, the hidden layer.
        """
        for i in range(self.layerI.numNodes):
            y = self.layerH.output[i]
            d = self.layerO.errors
            w = self.layerO.weights[:, i]
            self.layerH.errors[i] = y * (1 - y) * np.dot(w, d)

    def updateHiddenWeights(self):
        """
        Updates the weights of the nodes in the 1st layer, the hidden layer.
        """
        for i in range(self.layerH.numNodes):
            a = self.layerI.addBiasTerm(self.layerI.output)
            d = self.layerH.errors[i]
            self.layerH.weights[i] -= self.eta * d * a

    def binarizeClassNum(self, classNum):
        """
        Generates an array that contains all zeros except the index
        corresponding to the relevant class number.

        :param classNum: The class number to classify.
        :return: A outputNodes x 0 numpy array that contains all zeroes
        except at the corresponding index of the class number.
        """
        binarized = np.zeros(self.layerO.numNodes)
        binarized[int(classNum-1)] = 1
        return binarized


class Layer:
    """
    Represents a single-layer of a multi-layer perceptron in machine learning.
    """

    def __init__(self, numNodes, numWeights):
        """
        A simple constructor.

        :param numNodes: The number of nodes in the layer.
        :param numWeights: The number of weights on a node from the previous
        layer to the current.
        """
        self.numNodes = numNodes
        self.numWeights = numWeights

        self.output = np.zeros(numNodes)
        self.errors = np.zeros(numNodes)
        self.targets = None

        # Settings weights within [-0.5, 0.5]
        self.weights = np.random.rand(numNodes, numWeights)
        self.weights -= 0.5

    def updateOutput(self, v):
        """
        Updates the values of the all the nodes in the current layer.

        Computes the weighted sum of the input (from the previous layer,
        the input layer) and passes the output through the activation
        function. The final output is then stored in the corresponding node.

        :param v: The vector input from the previous layer as a numpy array.
        """
        h = np.dot(self.weights, self.addBiasTerm(v))
        a = self.activationFunction(h)
        self.output = a

    def activationFunction(self, x):
        """
        The activation function for a node in the neural system. In this
        case, the function is the output of the sigmoid function.

        :param x: A number as input.
        :return: The output of the sigmoid function.
        """
        sigmoid = 1 / (1 + np.exp(-x))
        return sigmoid

    def addBiasTerm(self, v):
        """
        Adds an extra column to the start of a 2D numpy array which
        represents the corresponding element to be multiplied by the bias
        weight.

        The reason for doing so is to simplify calculations (namely the dot
        product between v and w).

        :param v: A 0x3 numpy array of the form [x, y, <class_num>].
        :return: A 0x4 numpy array of the form [1, x, y, <class_num>]
        """
        return np.hstack([np.array([1]), v])


def generateDataSet():
    """
    Generates instances of the four machine learning classes and returns
    the results.

    Specifically, 500 instances are generated for each class. Class1 and
    class2 instances are sampled 2D points bounded by a geometric rectangle
    while class3 and class4 and sampled 2D points from a multi-variate
    normal distribution.

    The total of 2000 instances are randomly shuffled and sorted into a
    training, validation and test set in proportions of 50:25:25.

    :return: A tuple containing the training, validation, and test sets as
    numpy arrays.
    """
    rotationAngle = 75
    instanceSize = 500

    c1 = RectClass(2, 5, 1, 4, classNum=1)
    c1.generateInstances(instanceSize)
    c1.rotateInstancesBy(rotationAngle)

    c2 = RectClass(1, 3, -5, -1, classNum=2)
    c2.generateInstances(instanceSize)
    c2.rotateInstancesBy(rotationAngle)

    c3 = NormClass([-2, -3], [[0.5, 0], [0, 3]], classNum=3)
    c3.generateInstances(instanceSize)

    c4 = NormClass([-4, -1], [[3, 0.5], [0.5, 0.5]], classNum=4)
    c4.generateInstances(instanceSize)

    data = np.vstack([c1.instances, c2.instances, c3.instances, c4.instances])
    np.random.shuffle(data)

    n = len(data)
    percentile0 = 0
    percentile50 = int(n/2)
    percentile75 = int(3*n/4)
    percentile100 = n

    training = data[percentile0: percentile50]
    validate = data[percentile50: percentile75]
    test = data[percentile75: percentile100]
    return training, validate, test


def sPlot(data, errors, sPerceptron):
    """
    Plots the all the instances in the data, the hyperplane generated by the
    single-layer perceptron, and the errors associated with training that
    perceptron after an epoch.

    :param data: A N x 3 numpy array of the form (x, y, <class_num>)
    :param errors: A list containing tuple of the form (<run_number>,
    <cumulative_error>)
    errors.
    :param sPerceptron: A SinglePerceptron object.
    """
    fig = plt.figure(figsize=(10, 10))
    fig.subplots_adjust(hspace=.5)

    # Creating first axis
    ax1 = fig.add_subplot(212)
    ax1.set_title("Data and Boundary Plot")
    ax1.set_xlabel("x1")
    ax1.set_ylabel("x2")

    # Plotting the data (class instances)
    classColour = {1: "r", 2: "b", 3: "g", 4: "c"}
    for v in data:
        ax1.scatter(v[0], v[1], color=classColour[v[2]])

    # Plotting the sPerceptron boundary
    X1 = np.arange(-3.0, 3.0, 1.0)
    ax1.plot(X1, sPerceptron.computeBoundaryCoordY(X1), color="y",
             linewidth=3.0, label="boundary")
    ax1.legend(loc="upper left")

    # Creating second axis
    ax2 = fig.add_subplot(211)
    ax2.set_title("Classification Error vs Epoch Number (Test Set)")
    ax2.set_xlabel("Epoch Number")
    ax2.set_ylabel("Classification Error")

    # Plotting the cumulative error against epoch
    X2, Y2 = zip(*errors)
    ax2.plot(X2, Y2)
    ax2.set_xlim(1, ax2.get_xlim()[1])
    ax2.set_ylim(0, ax2.get_ylim()[1])

    plt.show()


def mPlot(data, errorsTraining, errorsValidate):
    """
    Plots all the classified instances of the data, and the errors associated
    with training that perceptron after an epoch.

    :param data: A N x 3 numpy array of the form (x, y, <class_num>)
    :param errorsTraining: A list containing tuple of the form (<run_number>,
    <cumulative_error>) errors.
    :param errorsValidate: A list containing tuple of the form (<run_number>,
    <cumulative_error>)
    """
    fig = plt.figure(figsize=(10, 10))
    fig.subplots_adjust(hspace=.5)

    # Creating first axis
    ax1 = fig.add_subplot(212)
    ax1.set_title("Classification Plot")
    ax1.set_xlabel("x1")
    ax1.set_ylabel("x2")

    # Plotting the data (class instances)
    classColour = {1: "r", 2: "b", 3: "g", 4: "c"}
    for v in data:
        ax1.scatter(v[0], v[1], color=classColour[v[2]])

    # Creating second axis
    ax2 = fig.add_subplot(211)
    ax2.set_title("Classification Error vs Epoch Number (Test Set)")
    ax2.set_xlabel("Epoch Number")
    ax2.set_ylabel("Classification Error")

    # Plotting the cumulative error against epoch
    X2, Y2 = zip(*errorsTraining)
    X3, Y3 = zip(*errorsValidate)
    ax2.plot(X2, Y2, label="training")
    ax2.plot(X3, Y3, label="validation")
    ax2.set_xlim(1, ax2.get_xlim()[1])
    ax2.set_ylim(0, ax2.get_ylim()[1])
    ax2.legend(loc="upper left")

    plt.show()


def main():
    """
    Runs the script.
    """
    #[training, validation, test] = generateDataSet()

    #np.savetxt("training.txt", training)
    #np.savetxt("validation.txt", validation)
    #np.savetxt("test.txt", test)

    training = np.loadtxt("training.txt")
    validation = np.loadtxt("validation.txt")
    test = np.loadtxt("test.txt")

    sPerceptron = SingleNeuralNetwork(numWeights=2,
                                      eta=0.2,
                                      targetClassNum=2)
    mPerceptron = MultiNeuralNetwork(eta=0.1,
                                     nodesInput=2,
                                     nodesHidden=20,
                                     nodesOutput=4)

    batch = 5
    epoch = 200
    sErrors = []
    mErrorsTraining = []
    mErrorsValidate = []

    for i in range(1, epoch):
        # Training
        trainSubset = training[(i-1)*batch: i*batch]
        [sPerceptron.train(v) for v in trainSubset]
        mPerceptron.train(trainSubset)

        # Computing errors
        sErrors.append((i, sPerceptron.evaluate(test)))
        mErrorsTraining.append((i, mPerceptron.evaluate(training)))
        mErrorsValidate.append((i, mPerceptron.evaluate(test)))

    # Calculate accuracy for single neural network
    sAcc = sPerceptron.computeAccuracy(validation)
    print("Accuracy of single perceptron: {}".format(sAcc))

    # Generate confusion matrix for multiple neural network
    classified = mPerceptron.classify(test)
    confusion = metrics.confusion_matrix(test[:, 2], classified[:, 2])
    print("Confusion matrix of multi perceptron:\n {}".format(confusion))

    # Plotting
    sPlot(test, sErrors, sPerceptron)
    mPlot(classified, mErrorsTraining, mErrorsValidate)


if __name__ == "__main__":
    main()
