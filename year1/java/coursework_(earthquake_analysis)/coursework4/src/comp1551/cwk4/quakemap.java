package comp1551.cwk4;

import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * Draws a set of earthquakes onto a map.
 * 
 * @author Othman Alikhan
 */
public class QuakeMap 
{
	/**
	 * Draws a list of earthquake types specified by the command line onto a PNG
	 * image map and HTML document map where both are generated in the same directory.
	 * 
	 * @param args is the command line arguments where only two must be suppled:
	 * <level> <time> where <level> is either "1.0", "2.0", "3.0" or "4.5" and <time>
	 * is either "hour", "day", "week", or "month" where both are minimum thresholds.
	 * @throws IOException if either a QuakeList object could not be generated or
	 * PrintWriter object could not open a file.
	 */
	
	// Name of HTML template for generating the map
	
	private static final String MAP_TEMPLATE_FILE = "map-template.html";
	
	public static void main(String args[])
	{
		PrintWriter output = null;	
		try
		{	
			// Checks for command line arguments that specify earthquake type
			
			if(args.length != 2)
			{
				System.err.println("Error: <level> <time> need to be specified!");
				System.exit(1);
			}
			
			// Draws the earthquakes on an image and outputs it in same directory
			
			QuakeList quack = new QuakeList(args[0], args[1]);			
			quack.asImageMap();
			
			// Draws the earthquakes via an HTML document in the same directory and
			// displays the output by opening the HTML document
			
			File outputFile = new File(MAP_TEMPLATE_FILE);
			output = new PrintWriter(outputFile);	
			output.print(quack.asGoogleMap());
			
			Desktop.getDesktop().open(outputFile);
		}
		catch(IOException error)
		{
			System.err.println(error);
			System.exit(1);
		}
		finally
		{
			output.close();
		}
	}
}
