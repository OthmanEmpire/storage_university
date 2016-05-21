package comp1551.cwk4;

import java.io.IOException;

/**
 * Prints information about some types of earthquakes onto the screen.
 * 
 * @author Othman Alikhan
 */
public class QuakeInfo 
{
	/**
	 * Prints out the quantity of earthquakes being analyzed, the strongest, 
	 * shallowest, and deepest earthquakes along with their coordinates and 
	 * variables of interest.
	 * 
	 * @param args is the command line arguments where only two must be suppled:
	 * <level> <time> where <level> is either "1.0", "2.0", "3.0" or "4.5" and <time>
	 * is either "hour", "day", "week", or "month" where both are minimum thresholds.
	 * @throws IOException if the QuakeList object could not be generated.
	 */
	public static void main(String args[])
	{
		// Checks for command line arguments that specify earthquake type
		
		if(args.length != 2)
		{
			System.err.println("Error: <level> <time> need to be specified!");
			System.exit(1);
		}
		
		try
		{
			// From a list of earthquakes, prints the strongest, shallowest, and
			// deepest earthquakes
			
			QuakeList quack = new QuakeList(args[0], args[1]);
			
			System.out.printf("%d quakes analyzed%n", quack.size());

			System.out.printf("%nStrongest: M%.1f at (%.4f,%.4f)%n", 
								quack.strongest().getMagnitude(), 
								quack.strongest().getLatitude(), 
								quack.strongest().getLongitude());	
			
			System.out.printf("Shallowest: %.2fkm at (%.4f,%.4f)%n", 
					quack.shallowest().getDepth(), 
					quack.shallowest().getLatitude(), 
					quack.shallowest().getLongitude());	
			
			System.out.printf("Deepest: %.2fkm at (%.4f,%.4f)%n", 
					quack.deepest().getDepth(), 
					quack.deepest().getLatitude(), 
					quack.deepest().getLongitude());			
		}
		catch(IOException error)
		{
			System.out.print(error);
			System.exit(2);
		}
	}
}
