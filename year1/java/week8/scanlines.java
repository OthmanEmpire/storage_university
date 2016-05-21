// Example of scanning a text file line by line
// (NDE, 2015-03-30)

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class ScanLines
{
  public static void main(String[] args)
  {
    // Check for a filename on command line

    if (args.length == 0) {
      System.err.println("Usage: java ScanLines <filename>");
      System.exit(1);
    }
 
    // Create a Scanner for the specified file

    File inputFile = new File(args[0]);

    try (Scanner input = new Scanner(inputFile)) {

      // Fetch lines for as long as we can...

      while (input.hasNextLine()) {
        String line = input.nextLine();
        System.out.println(line);        // just print the line in this case
      }

    }
    catch (FileNotFoundException error) {
      System.err.println(error);
      System.exit(2);
    }
  }
}
