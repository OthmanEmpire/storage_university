// Exhibiting DecimalFormatting (inspired by examples.javacodegeeks.com)

import java.text.DecimalFormat;

class Decimator
{
	private static final String PYTHONISBEST = "###,###.###";
	private static double number = 112358.1321;

	public static void main(String[] args)
	{
		DecimalFormat dF = new DecimalFormat(PYTHONISBEST);
		System.out.printf("Exhibiting the POWERS of Decimal" + 
				  "Format:%n%n");
		System.out.printf("Unformatted: %f%n", number);
		System.out.println("Formatted: " + dF.format(number));
	}
}
