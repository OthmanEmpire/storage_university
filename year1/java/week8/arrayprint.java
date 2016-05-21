// Examples of how to print arrays conveniently (e.g., for debugging)
// (NDE, 2010-05-03)

import java.util.Arrays;

class ArrayPrint
{
  public static void main(String[] args)
  {
    // One-dimensional array

    int[] data = { 1, 2, 3, 4 };

    System.out.println("1D array:");
    System.out.println(data);
    System.out.println(Arrays.toString(data));

    // Two-dimensional array

    int[][] data2 = { { 1,  2,  3,  4 },
                      { 2,  4,  6,  8 },
                      { 1,  3,  5,  7 } };

    System.out.println("\n2D array:");
    System.out.println(data2);
    System.out.println(Arrays.toString(data2));
    System.out.println(Arrays.deepToString(data2));
  }  
}
