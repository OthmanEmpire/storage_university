// Example of how wrapper classes are used with collections
// (NDE, 2010-05-05)

import java.util.ArrayList;
import java.util.List;

class Wrapper
{
  public static void main(String[] args)
  {
    // This won't compile: lists contain objects, not primitive values

    List<int> bad = new ArrayList<>();

    // This will do what we need

    List<Integer> data = new ArrayList<>();

    data.add(1);    // value gets boxed as an Integer object automatically
    data.add(4);
    data.add(9);
    data.add(16);

    for (int value : data) {      // automatic unboxing happens here
      System.out.println(value);  
    }
  }
}
