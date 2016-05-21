package comp1551.cwk4;

import java.awt.Color;
import java.awt.Graphics2D;
// import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Template;


/**
 * A list of earthquakes acquired from a USGS data feed.
 *
 * (See http://earthquake.usgs.gov/eathquakes/feed/v1.0/csv.php)
 *
 * @author Nick Efford
 * @author Othman Alikhan
 */
class QuakeList
{
  // Template for data feed URLs

  private static final String URL_TEMPLATE =
   "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/%s_%s.csv";

  // Names of base image and HTML template used for map generation

  private static final String MAP_IMAGE_FILE = "map-base.png";
  private static final String MAP_TEMPLATE_FILE = "map-template.html";

  // HTML map template - static, so shared by all QuakeList objects

  private static Template mapTemplate;

  // Fields

  private String level;
  private String period;
  private ArrayList<Quake> data;

  /**
   * Creates a QuakeList from a data feed specified by the given parameters.
   *
   * @param level Minimum level of quake to consider
   * @param period Time period to consider
   * @throws IOException If data could not be acquired for some reason
   */
  public QuakeList(String level, String period) throws IOException
  {
    this.level = level;
    this.period = period;
    data = new ArrayList<Quake>();

    acquireData();
    loadMapTemplate();
  }

  /**
 * Extracts data from the UGSG website and stores it into a QuakeList container.
 * 
 * @throws IOException if the URL connection fails
 * @throws InputMismatchException if the data being read does not follow the 
 * pattern for generating a Quake object (i.e. there is a mistake in the CSV file)
 */
  private void acquireData() throws IOException
  {
    // Connect to the relevant USGS data feed

    URL url = new URL(String.format(URL_TEMPLATE, level, period));
    URLConnection connection = url.openConnection();
    
    // Create a Scanner for the connection input stream
    
    try 
    {
    	Scanner input = new Scanner(connection.getInputStream());
    	
    	// Extracts data from the input stream and stores into an array
    	
    	input.nextLine();    // Ignores first line (which is just the header)
    	
        while(input.hasNextLine())
        {
        	data.add(new Quake(input.nextLine()));
        }
    }
    catch(IOException error) 
    {
    	System.err.println(error);
    	System.exit(1);
    }
    catch(InputMismatchException error)
    {
    	System.err.println(error);
    	System.exit(2);
    }
  }

  /**
 * Loads the map template. 
 * 
 * @throws IOException if FileReader object could not be created
 */
  private void loadMapTemplate() throws IOException
  {
    if (mapTemplate == null) {
      // First QuakeList object to be created will
      // take care of loading the HTML template

      FileReader source = new FileReader(MAP_TEMPLATE_FILE);
      mapTemplate = Mustache.compiler().compile(source);
    }
  }

  /**
 * @return size which is the number of earthquakes being analyzed.
 */
  int size() {return data.size();}
  
  /**
 * Prints out all the earthquakes stored in the class.
 */
  void print() 
  {
	  for(int i = 0; i < data.size(); ++i)
	  {
		  System.out.println(data.get(i));
	  }
  }
  
  /**
 * @return strongestQuake which is the earthquake with the greatest magnitude.
 */
  Quake strongest()
  {
	  Quake strongestQuake = data.get(0);	// Initialization
	  
	  // Loops over data set and compares magnitudes until greatest is found
	  
	  for(int i = 0; i < data.size(); ++i)
	  {
		Quake quack = data.get(i);
		
		  if(quack.getMagnitude() > strongestQuake.getMagnitude())
		  {
			  strongestQuake = quack;
		  }  
	  }
	  return strongestQuake;
  }
  
   /**
 * @return shallowestQuake which is the earthquake with the shallowest depth.
 */
  Quake shallowest()
   {  
	  Quake shallowestQuake = data.get(0);		// Initialization
	
	  // Loops over data set and compares depths until shallowest is found
	  
	  for(int i = 0; i < data.size(); ++i)
	  {
		Quake quack = data.get(i);
		
		  if(quack.getDepth() < shallowestQuake.getDepth())
		  {
			  shallowestQuake = quack;
		  }  
	  }
	  return shallowestQuake;
  }
  
   /**
 * @return  deepestQuake which is the earthquake with the deepest depth.
 */
  Quake deepest(){
	  
	  Quake deepestQuake = data.get(0);		// Initialization
	  
	  // Loops over data set and compares depth until deepest is found
	  
	  for(int i = 0; i < data.size(); ++i)
	  {
		Quake quack = data.get(i);
		
		  if(quack.getDepth() > deepestQuake.getDepth())
		  {
			  deepestQuake = quack;
		  }  
	  }
	  return deepestQuake;
  }  
  
  /**
 * Retrieves a list of earthquakes with magnitudes greater than 4.5 that occurred a
 * week ago and prints them onto the screen.
 * 
 * @param args which is the command line arguments. In this case, none are supplied.
 * @throws IOException if the QuakeList object could not be generated.
 */
  public static void main(String args[]) 
  {
	  try
	  {
		  // Prints the list of earthquakes that occurred last week with 
		  // magnitudes 4.5 
		  
		  QuakeList quack = new QuakeList("4.5", "week");
		  quack.print();
	  }
	  catch(IOException error)
	  {
		  System.out.println(error);
		  System.exit(3);
	  }
  }
  
  /**
 * Returns the HTML text required to generated a document to view earthquakes on a
 * browser through GoogleMaps.
 * 
 * @return mapTemplate.execute(map) which is an HTML string of the earthquake maps
 */
  String asGoogleMap()
  {
	  // Bundles up data in a required format then uses it to return an HTML based 
	  // map
	  
	  HashMap<String, Object> map = new HashMap<String, Object>();
	  
	 map.put("quakes", data);
	 map.put("level", level);
	 map.put("period", period);
	  
	 return mapTemplate.execute(map);
  }
  
  /**
  * Draws the earthquakes on a given image of the world map.
  * 
  * @throws IOException if outputFile or input image could not be saved or read.
  */
  void asImageMap()
  {
	  BufferedImage img = null;
	  try
	  {
		  // Opens the image and converts it into a Graphics2D object
		  
		  img = ImageIO.read(new File(MAP_IMAGE_FILE));
		  
		  Graphics2D quakeMap = img.createGraphics();
		  quakeMap.setColor(Color.RED);
		  
		  for(int i = 0; i < data.size(); ++i)
		  {			  
			  // Conversion of coordinates from (latitude, longitude) --> (x,-y)
			  // for the given image of 1080 x 540. The "+180" and "+90" calibration
			  // below are due to the -180 to 180 degree and -90 to 90 degree 
			  // latitude and longitude range respectively.
			  
			  int X =  (int) (3*(data.get(i).getLongitude() + 180));	  
			  int Y =  (int) (540 - (3*(data.get(i).getLatitude() + 90)));
			  
			  // Draws the earthquake as a small rectangle
			  
			  quakeMap.fillRect(X, Y, 5, 5);  	
		  }
		  
		  // Outputs the image as a PNG in the same directory
		  
		  File outputFile = new File("SaveTheWorld.png");
		  ImageIO.write(img, "png", outputFile);
	  } 
	  catch (IOException error) 
	  {
		System.err.println(error);
		System.exit(4);
	  }
  }
}
