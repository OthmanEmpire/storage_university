// Example of using a map
// (NDE, 2010-05-05)

import java.util.TreeMap;
import java.util.Map;

class MapExample
{
  public static void main(String[] args)
  {
    // Create a map containing some keys & values

    Map<String,Integer> map = new TreeMap<>();

    map.put("apple",  42);
    map.put("orange", 34);
    map.put("mango",  100);
    map.put("banana", 17);

    // Call various map methods

    System.out.printf("Size = %d%n", map.size());
    System.out.printf("Empty? %s%n", map.isEmpty());

    System.out.printf(
      "Contains key \"mango\"? %s%n", map.containsKey("mango"));
    System.out.printf(
      "Contains key \"kiwi\"?  %s%n", map.containsKey("kiwi"));

    System.out.printf("Value for mango = %d%n", map.get("mango"));
    System.out.printf("Value for kiwi  = %d%n", map.get("kiwi"));

    // Demonstrate removal of a key-value pair

    System.out.printf("%nRemoving \"mango\"...%n");
    map.remove("mango");
    System.out.printf("Size = %d%n", map.size());
    System.out.printf(
      "Contains key \"mango\"? %s%n", map.containsKey("mango"));
    System.out.printf("Value for mango = %d%n", map.get("mango"));

    // Demonstrate effect of calling clear method

    System.out.printf("%nClearing map...%n");
    map.clear();
    System.out.printf("Size = %d%n", map.size());
    System.out.printf("Empty? %s%n", map.isEmpty());
  }
}
