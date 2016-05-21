// Calculates the gravity of the matter between two objects


import java.util.Scanner;

class Gravity
{
	static public void main(String[] args)
	{
		Scanner input = new Scanner(System.in);		

		System.out.printf("Distance between A & B: ");
		double distance = input.nextDouble();

		System.out.printf("Mass of A: ");
		double massA = input.nextDouble();

		System.out.printf("Mass of B: ");
		double massB = input.nextDouble();

		computeGravityOfMatter(distance, massA, massB);
	}

	static void computeGravityOfMatter(double distance, 
					   double massA, 
					   double massB)
	{
		final double G = 6.673 * Math.pow(10, -11);	
		
		double force = G * (massA * massB) / Math.pow(distance, 2);

		System.out.printf("%nForce: %.1e N", force);
	}
}
