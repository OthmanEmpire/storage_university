// Examples of array indexing
// (NDE, 2015-02-26)

class ArrayIndex
{
  public static void main(String[] args)
  {
    int[] data = { 2, 4, 6, 8, 10 };

    // Valid indexing

    System.out.println(data[0]);
    System.out.println(data[1]);
    System.out.println(data[4]);

    // Invalid indexing

    // System.out.println(data[5]);
    System.out.println(data[-1]);
  }
}
