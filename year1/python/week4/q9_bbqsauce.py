### This function would work well with chips... Perhaps... ###



def sumGrades():

    with open("Q5_friend", "r") as file:
        total = 0
        for grade in file:

            total += int(grade)          # Since one grade per line
                    
        return total



def numberofGrades():

    with open("Q5_friend", "r") as file:
        lines = 0
        for grade in file:

            lines += 1          # Since one grade per line
                    
        return lines



    count('\n')
    pass


def mean(total, n):

    avg = total/n

    return avg
    



total = sumGrades()
n = numberofGrades()
avg = mean(total,n)

print("The sumofGrades are: {}, the numberofGrades are: {}, the mean is: {}".format(total,n,avg))
