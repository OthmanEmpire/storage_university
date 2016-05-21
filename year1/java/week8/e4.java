// Reads words from a file, stores them in a list, sorts them, and 
// writes the sorted list into a new file.
// Author: Othman Alikhan

import java.util.Scanner;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;

class Spaghetti
{
	public static void main(String args[])
		{
			// Checks for file name on command line

			if(args.length == 0)
			{
				System.err.println("Usage: java Spaghetti <filename>");
				System.exit(1);
			}
			
			// Creates a file stream then tries to read from file and
			// stores the results into a list

			File inputFile = new File(args[0]);
			List<String> arr = new ArrayList<>();

			try(Scanner input = new Scanner(inputFile))
			{
				while(input.hasNextLine())
				{
					String line = input.nextLine();
					arr.add(line);
				}
			}
			catch(FileNotFoundException error)
			{
				System.err.println(error);
				System.exit(2);
			}	

			// Sorts the list out 
			
			Collections.sort(arr);

			// Outputs the sorted list into another file

			File outputFile = new File("Delicious.txt");

			try(PrintWriter output = new PrintWriter(outputFile))
			{

					for(int i = 0; i < arr.size(); ++i)
					{
						output.println(arr.get(i));
					}
			}
			catch(IOException error)
			{
				System.err.println(error);
				System.exit(3);
			}
		}
}
