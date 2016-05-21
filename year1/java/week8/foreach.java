// Simple examples of the 'for each' loop, operating on arrays
// (NDE, 2015-02-16)

class ForEach
{
  public static void main(String[] args)
  {
    int[] data = { 1, 4, 9, 16, 25 };

    for (int value : data) {
      System.out.println(value);
    }

    String[] words = { "apple", "kiwi", "orange", "strawberry" };

    for (String word : words) {
      System.out.println(word);
    }
  }
}
