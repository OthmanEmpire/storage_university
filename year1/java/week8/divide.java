// Example of a program that can generate exceptions, either when
// parsing numbers input by the user or doing arithmetic with them
// (NDE, 2013-03-30)

import java.util.Scanner;
import java.util.InputMismatchException;

public class Divide
{
	public static void main(String[] args)
	{
		try{		
			Scanner input = new Scanner(System.in);

			System.out.print("Enter numerator: ");
			int num = input.nextInt();

			System.out.print("Enter denominator: ");
			int denom = input.nextInt();

			int result = num / denom;

			System.out.println(result);
			}
		catch(ArithmeticException error){
				System.err.println("GG");
				System.exit(1);
			}
		catch(InputMismatchException error){
						System.err.println("GG");
						System.exit(2);
			}
	}
}
