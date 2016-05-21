// Examples of iterating over an array
// (NDE, 2010-05-04)

class ArrayLoops
{
  public static void main(String[] args)
  {
    int[] data = { 2, 4, 6, 8, 10 };

    // Traditional for loop

    for (int i = 0; i < data.length; ++i) {
      System.out.println(data[i]);
    }

    // 'For each' loop - similar to Python's for
 
    for (int value : data) {
      System.out.println(value);
    }
  }
}
