// A simple program that reads from standard input and stores data in 
// an array 
// Author: Othman Alikhan

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Storage
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		List<Double> arr = new ArrayList<>();
		try {
				// Stores user inputed doubles into an array

				while(true)
				{
					System.out.printf("%nPlease enter a value: ");

					if(input.hasNextDouble())
					{
						double value = input.nextDouble();
						arr.add(value);
					}
					else
					{
						break;
					}
				}

				// Loops over the array, sums and prints the values
				// then calculates the mean and prints it

				double sum = 0.0;
				double mean = 0.0;

				System.out.printf("%nThe arrayList contains:");

				for(int i = 0; i < arr.size(); ++i)
				{
					sum += arr.get(i);
					System.out.print(" " + arr.get(i));
				}
				
				mean = sum / arr.size();
				System.out.printf("%n%nThe mean: " + mean + "%n%n");

			}
		catch(Exception error)
			{
				System.err.print("UNKOWN ERROR!");
			}
	}	
}
