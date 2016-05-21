// Examples of manipulating a list via its Collection interface
// (NDE, 2010-01-05)

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;

class ListAsCollection
{
  public static void main(String[] args)
  {
    // Create collection and add command line arguments to it

    Collection<String> words = new ArrayList<>();
    //Collection<String> words = new LinkedList<>();

    for (String word : args) {
      words.add(word);
    }

    // Demonstrate iteration over collection

    System.out.print("List:");

    for (String word : words) {
      System.out.printf(" %s", word);
    }

    // Call various other methods of the collection

    System.out.printf("%n%nSize = %d%n", words.size());
    System.out.printf("Empty? %s%n", words.isEmpty());
    System.out.printf("Contains \"apple\"? %s%n", words.contains("apple"));

    // Demonstrate attempted removal of an item

    System.out.printf("%nAttempting to remove \"apple\"...%n");
    boolean removed = words.remove("apple");
    System.out.printf("Removed? %s%n", removed);

    System.out.printf("Size = %d%n", words.size());
    System.out.printf("Empty? %s%n", words.isEmpty());
    System.out.printf("Contains \"apple\"? %s%n", words.contains("apple"));

    // Demonstrate effect of calling the clear method

    System.out.printf("%nClearing collection...%n");
    words.clear();
    System.out.printf("Size = %d%n", words.size());
    System.out.printf("Empty? %s%n", words.isEmpty());
  }
}
