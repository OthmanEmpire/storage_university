// Integer division in Java

class Division
{
	public static void main(String[] args)
	{
		int x = 1;
		int y = 7;
		float quotient, remainder;

		quotient = x/y;	
		remainder = x%y;

		System.out.printf("DIVISION%n");
		System.out.printf("x: %d%n", x);
		System.out.printf("Y: %d%n", y);
		System.out.printf("%n%nDividing X by Y yields:%n");
		System.out.printf("Quotient: %.1f%n", quotient);
		System.out.printf("Remainder: %.1f%n", remainder);
	}
}
