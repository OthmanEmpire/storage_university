// Examples of array initialisation
// (NDE, 2015-02-26)

class ArrayInit
{
  public static void main(String[] args)
  {
    /*********************** One-Dimensional Arrays ***********************/

    // Legal initialisations

    int[] p = null;

    int[] q = new int[5];

    int[] r = { 2, 4, 6, 8 };

    // Print array sizes

    System.out.println("Size of q = " + q.length);
    System.out.println("Size of r = " + r.length);
    System.out.println(r);

    // This won't work (type mismatch):

    //int[] bad = { 0.1, 0.3, 0.5, 0.7 };

    /*********************** Two-Dimensional Arrays ***********************/

    // Legal initialisations

    int[][] w = null;

    int[][] x = new int[3][4];

    int[][] y = { { 1, 2, 3, 4 },
                  { 2, 4, 6, 8 },
                  { 7, 5, 3, 1 } };

    System.out.println(y[2][1]);   // what does this print?
  }
}
