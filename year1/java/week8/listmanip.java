// Examples of manipulating lists in Java
// (NDE, 2010-01-05)

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class ListManip
{
  public static void main(String[] args)
  {
    // Create list and add command line arguments to it

    ArrayList<String> words = new ArrayList<>();
    //LinkedList<String> words = new LinkedList<>();

    for (String word : args) {
      words.add(word);
    }

    // Demonstrate iteration over list

    System.out.print("List:");

    for (String word : words) {
      System.out.printf(" %s", word);
    }

    // Demonstrate item retrieval

    System.out.printf("%n%nSize = %d%n", words.size());
    System.out.printf("Item at index 0: %s%n", words.get(0));
    System.out.printf("Item at index 1: %s%n", words.get(1));

    // Demonstrate searching for an item

    int index = words.indexOf("apple");
    int lastIndex = words.lastIndexOf("apple");
    if (index != -1) {
      System.out.printf("First occurrence of \"apple\" at %d%n", index);
      System.out.printf("Last occurrence of \"apple\" at %d%n", lastIndex);
    }

    // Demonstrate removal of an item

    System.out.printf("%nAttempting to remove item at index 1...%n");
    words.remove(1);

    System.out.printf("Size = %d%n", words.size());
    System.out.printf("Item at index 0: %s%n", words.get(0));
    System.out.printf("Item at index 1: %s%n", words.get(1));
  }
}
