// Example of maps with different implementations
// (NDE, 2015-03-12)

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;
import java.util.Map;

class MapTypes
{
  public static void main(String[] args)
  {
    // Create maps with three different implementations

    Map<String,Integer> hashMap = new HashMap<>();
    Map<String,Integer> linkedHashMap = new LinkedHashMap<>();
    Map<String,Integer> treeMap = new TreeMap<>();

    // Put identical key-value pairs in them

    hashMap.put("apple",  42);
    hashMap.put("orange", 34);
    hashMap.put("mango",  100);
    hashMap.put("banana", 17);
    hashMap.put("kiwi",   8);

    linkedHashMap.put("apple",  42);
    linkedHashMap.put("orange", 34);
    linkedHashMap.put("mango",  100);
    linkedHashMap.put("banana", 17);
    linkedHashMap.put("kiwi",   8);

    treeMap.put("apple",  42);
    treeMap.put("orange", 34);
    treeMap.put("mango",  100);
    treeMap.put("banana", 17);
    treeMap.put("kiwi",   8);

    // Retrieve and print keys, to see effect of implementation on ordering

    System.out.print("HashMap       :");

    for (String key : hashMap.keySet()) {
      System.out.print(" " + key);
    }

    System.out.printf("%nLinkedHashMap :");

    for (String key : linkedHashMap.keySet()) {
      System.out.print(" " + key);
    }

    System.out.printf("%nTreeMap       :");

    for (String key : treeMap.keySet()) {
      System.out.print(" " + key);
    }

    System.out.println();
  }
}
