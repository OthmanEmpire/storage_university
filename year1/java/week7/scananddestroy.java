// Example of using Scanner to parse input text
// (NDE, 2010-04-21)

import java.util.Scanner;

class ScannerExample
{
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter an integer: ");
    int n = input.nextInt();

    System.out.print("Enter a floating-point number: ");
    double x = input.nextDouble();

    System.out.println();
    System.out.println("You entered the integer " + n);
    System.out.println("You entered the floating-point number " + x);
  }
}
