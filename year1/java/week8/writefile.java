// Example of writing formatted text to a file
// (NDE, 2015-03-30)

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

class WriteFile
{
  public static void main(String[] args)
  {
    // Check for a filename on command line

    if (args.length == 0) {
      System.err.println("Usage: java WriteFile <filename>");
      System.exit(1);
    }

    // Create a PrintWriter stream for the file

    File outputFile = new File(args[0]);

    try (PrintWriter output = new PrintWriter(outputFile)) {
      
      // Print formatted values to stream

      for (int i = 0; i < 100; ++i) {
        output.printf("%.3f%n", Math.random());
      }

    }
    catch (IOException error) {
      System.err.println(error);
      System.exit(2);
    }
  }
}
