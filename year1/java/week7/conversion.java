// Demonstration of Java's rules for converting numeric types.
// The key thing to remember is that the compiler won't permit a
// loss of precision to take place when assigning a value of
// one type to a variable of another, unless you have made the
// conversion explicit by means of a cast.

public class Conversion
{
  public static void main(String[] args)
  {
    double value = 2.7;

    float f1 = (float)value;      // implicit double -> float is not allowed
    int i1 = (int)value;        // implicit double -> int is not allowed

    int i2 = (int) value;  // explicit cast is OK
    float f2 = i2;         // implicit int -> float is OK
  }
}
