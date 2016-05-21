// A simple program that displays the result of 100 coin flips 
// Author: Othman Alikhan

class Coins
{
	public static void main(String args[])
	{
		for(int i = 0; i < 100; ++i)
		{

				if(Math.random() >= 0.5)
				{
					System.out.println("Heads");	
				}
				else
				{
					System.out.println("Tails");
				}
		}
	}
}
