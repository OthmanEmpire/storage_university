// Program to display ranges for Java's primitive numeric types
// (NDE, 2010-04-22)

class Ranges
{
  public static void main(String[] args)
  {
    java.io.PrintStream out = System.out;

    // Integer types

    out.printf("byte       : %d to %d%n", Byte.MIN_VALUE, Byte.MAX_VALUE);
    out.printf("short      : %d to %d%n", Short.MIN_VALUE, Short.MAX_VALUE);
    out.printf("int        : %d to %d%n", Integer.MIN_VALUE, Integer.MAX_VALUE);
    out.printf("long       : %d to %d%n", Long.MIN_VALUE, Long.MAX_VALUE);

    // Floating-point types

    out.printf("+ve float  : %g to %g%n", Float.MIN_VALUE, Float.MAX_VALUE);
    out.printf("+ve double : %g to %g%n", Double.MIN_VALUE, Double.MAX_VALUE);
  }
}
