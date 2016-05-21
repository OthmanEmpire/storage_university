// A program to compute square roots
// (NDE, 2010-04-29)

import java.util.Scanner;
import javax.swing.JOptionPane;

class Sqrt
{
  public static void main(String[] args)
  {
//    Scanner input = new Scanner(System.in);
	String input = JOptionPane.showInputDialog("Enter a number: ");

    // Obtain floating-point number from user and compute its square root

	double number = Double.parseDouble(input);

    double result = Math.sqrt(number);

    // Display result of the calculation

    System.out.printf("The square-root of %f is %f%n", number, result);
	JOptionPane.showMessageDialog(null, "GG: " + number);
  }
}
