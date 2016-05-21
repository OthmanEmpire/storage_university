// Calculate the area and perimeter of a circle

import java.util.Scanner;

class Circle
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);

		System.out.printf("Enter the radius of your circle: ");
		double radius = input.nextDouble();

		System.out.printf("%nArea: %.3f%n", computeArea(radius));
		System.out.printf("Perimeter: %.3f", 
				  computePerimeter(radius));
	}

	static double computeArea(double radius)
	{
		return Math.PI * Math.pow(radius, 2);
	}

	static double computePerimeter(double radius)
	{
		return 2 * Math.PI * radius;
	}
}
