// Exhibiting the behaviour of the overloaded Scanner

import java.util.Scanner;

class OverLord
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);	

		System.out.printf("Please input your BASE: ");
		int base = input.nextInt();

		System.out.printf("Please input your value: ");
		int decimal = input.nextInt(base);

		System.out.printf("%nYour value: %d", decimal);
	}
}
