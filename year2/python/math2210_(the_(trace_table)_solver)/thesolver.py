
import ast

def loadRegisterProgram(fileName):
    """
    Extracts the Register Program from a text file where the form of the
    program is for instance:
    1: (1,2,3)
    2: (1,1)
    3: Halt
    """
    registerProgram = {}

    with open(fileName, "r") as file:
        readData = file.read()

    # Pre-processing before entering data into dictionary
    readData = readData.split("\n")
    readData = [data for data in readData if data != ""]

    # Entering data into dictionary
    for data in readData:
        data = data.split(":")
        instructionNum = int(data[0])
        try:
            instruction = eval(data[1])
        except NameError:
            instruction = data[1].replace(" ", "")
        registerProgram[instructionNum] = instruction

    # Displays the program stored in dictionary to elevate confidence
    print("Register Program is as follows:")
    for key, value in registerProgram.items():
        print("{:<3} {}".format(key, value))
    print("END OF PROGRAM\n")

    return registerProgram

def loadInputRegister(fileName):
    """
    Reads all input registers from a file where the form of the input
    registers are for instance:
    [1,2,3]
    [2,4,8]
    [0,2,0]
    """
    with open(fileName, "r") as file:
        readData = file.read()

    # Pre-processing before entering data into dictionary
    inputRegisterList = readData.split("\n")
    inputRegisterList.remove("")

    # Converts the string representation of the list to a list
    inputRegisterList = [ast.literal_eval(inputRegister) for inputRegister in
                         inputRegisterList]

    # Displays the input register read to further elevate confidence
    print("Given input registers are:")
    for inputRegister in inputRegisterList:
        print(inputRegister)
    print("END OF INPUT\n")

    return inputRegisterList


def generateTraceTable(registerProgram, inputRegister,
                       fileName="theOutput.txt"):
    """
    Generates a trace table for the registerProgram on the given
    inputRegister and writes the data into a file with the filename
    "theOutput.txt" by default.
    """
    with open(fileName, "a") as file:

        file.write("The trace table generated on {} for the given "
                   "program in 'theProblem.txt' that contains {} "
                   "instructions:\n".format(inputRegister,
                                            len(registerProgram)))

        # Start the program from the first instruction
        instructionNum = 1
        file.write("{} -> {}\n".format(inputRegister, instructionNum))
        print("{} -> {}\n".format(inputRegister, instructionNum))

        while(registerProgram[instructionNum] != "Halt"):
            instruction = registerProgram[instructionNum]
            registerNum = instruction[0]

            # Instruction (n,j)
            if(len(instruction) == 2):
                inputRegister[registerNum - 1] += 1
                instructionNum = instruction[1]

            # Instruciton (n,j,k)
            elif(len(instruction) == 3):
                if(inputRegister[registerNum - 1] - 1 >= 0):
                    inputRegister[registerNum - 1] -= 1
                    instructionNum = instruction[1]
                else:
                    instructionNum = instruction[2]
            else:
                raise Exception
            file.write("{} -> {}\n".format(inputRegister, instructionNum))
            print("{} -> {}\n".format(inputRegister, instructionNum))

        file.write("THE END\n\n")


# def testTraceTable():
#     """
#     Runs the generateTraceTable function on a program which adds the entries
#     of it's registers. The trace table output matches to that of the lecture
#     notes (Last updated: November 22, 2015) on page 62.
#     """
#     testRegister = [3,2]
#     testProgram = {1:(2,2,3), 2:(1,1), 3:"Halt"}
#     generateTraceTable(testProgram, testRegister)

def theSolver():
    """
    The Solver.
    """
    registerProgram = loadRegisterProgram("theProblem.txt")
    inputRegisterList = loadInputRegister("theData.txt")

    for inputRegister in inputRegisterList:
        generateTraceTable(registerProgram, inputRegister)

def main():
    theSolver()

if __name__ == "__main__":
    main()