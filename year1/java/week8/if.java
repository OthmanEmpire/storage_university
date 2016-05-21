// Example of an if statement with an error - compare with if.cpp
// (NDE, 2015-02-15)

import java.util.Scanner;

class If
{
  public static void main(String[] args)
  {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter a non-zero integer: ");
    int n = input.nextInt();

    if (n == 0) {
      System.out.println("Error - zero is not allowed!");
    }
    else {
      System.out.println("You entered " + n);
    }
  }
}
