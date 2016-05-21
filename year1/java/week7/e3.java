// Temperature conversion from Celsius to Fahrenheit 

import java.util.Scanner;

class TempConverter
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);	

		System.out.printf("Please input your " +
				  "Celsius Temperature: ");
		double cel = input.nextDouble();	

		double fah = convertToFah(cel);
		System.out.printf("Converted to Fahrienheit: %.1f", 
			          fah);
	}

	static double convertToFah(double cel)
	{
		double fah = (9.0/5.0)*cel + 32.0;
		return fah;
	}
}
