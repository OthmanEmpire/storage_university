// Some simple examples of formatted output - compare with
// the equivalent Python code in Formatting.py
// (NDE, 2010-04-21)

class Formatting
{
  public static void main(String[] args)
  {
    System.out.printf("Default: %f%n", Math.PI);
    System.out.printf("8 dp: %.8f%n", Math.PI);
    System.out.printf("4 dp: %.4f%n", Math.PI);
    System.out.printf("2 dp, six-char field: |%6.2f|%n", Math.PI);
    System.out.printf("5 dp, ten-char field: |%10.5f|%n", Math.PI);
  }
}
