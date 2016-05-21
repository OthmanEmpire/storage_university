# A class that contains a list of sorting algorithms of varying worst case
# scenario time complexities (ranging from O(n^2) to O(n))


# Contains the set of all the algorithms that sort a list of numbers into
# ascending order
class Algorithm():

    # At all times, the algorithm splits the array into two groups, a sorted
    # and unsorted group. After each outer-loop iteration, an element from the
    # unsorted array is placed correctly into the sorted array. Continues this
    # procedure until all is but faded.
    def selectionSort(self, arr):
        """
        A sorting algorithm of class of O(n^2) for the worst case scenario
        """

        for i in range(0, len(arr)-1):
            minIndex = i

            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j

            tmp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = tmp

        return arr

    # Same logic as the selectionSort algorithm but terminates earlier and returns the kth smallest value
    def modifiedSelectionSort(self, arr, k):
        """
        A sorting algorithm of class of O(n^2) for the worst case scenario
        """

        iterComplexity = 0  # Counting the number of iterations to find the time complexity

        for i in range(0, k):
            minIndex = i

            for j in range(i+1, len(arr)):

                iterComplexity += 1

                if arr[j] < arr[minIndex]:
                    minIndex = j

            tmp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = tmp

        print("modifiedSelectionSort:", arr,)
        print("kth min value:", arr[k-1])
        print("Inner iterations performed:", iterComplexity)
        print()
        return arr[k-1]


# Testing unit for an algorithm
def main():

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    algae = Algorithm()

    print(int(0.5*len(arr)))

    algae.modifiedSelectionSort(arr, int(0.5*len(arr)))
    print("selectionSort:", algae.selectionSort(arr))


if __name__ == "__main__":
    main()