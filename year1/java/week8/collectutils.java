// Examples of using the collections utilities in java.util.Collections
// (NDE, 2010-05-05)

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

class CollectUtils
{
  public static String str(List<Integer> list)
  {
    return Arrays.toString(list.toArray());
  }

  public static void main(String[] args)
  {
    // Create and populate a list

    List<Integer> data = new LinkedList<>();

    for (int i = 1; i <= 10; ++i) {
      data.add(i);
    }

    System.out.printf("Initial:  %s%n", str(data));

    // Demonstrate reverse, shuffle, sort, rotate

    Collections.reverse(data);
    System.out.printf("Reversed: %s%n", str(data));

    Collections.shuffle(data);
    System.out.printf("Shuffled: %s%n", str(data));

    Collections.sort(data);
    System.out.printf("Sorted:   %s%n", str(data));

    Collections.rotate(data, 4);
    System.out.printf("Rotated:  %s%n", str(data));

    // Find min & max

    System.out.printf("%nMin = %d%n", Collections.min(data));
    System.out.printf("Max = %d%n", Collections.max(data));
  }
}
