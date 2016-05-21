package comp1551.cwk4;

/**
 * A container for storing information about an earthquake.
 * 
 * @author Othman
 */
public class Quake 
{
	private double latitude;
	private double longitude;
	private double depth;
	private double magnitude;

	/**
	 * @param data which is a string read from the CSV data feed produced by USGS
	 * that contains the information about earthquakes and their attributes.
	 */
	public Quake(String data) 
	{
		// The string data follows a template hence relevant information
		// is extracted (namely: latitude, longitude, depth, and magnitude)
		
		String dataParts[] = data.split(",");
		
		latitude = Double.parseDouble(dataParts[1]);
		longitude = Double.parseDouble(dataParts[2]);
		depth = Double.parseDouble(dataParts[3]);
		magnitude = Double.parseDouble(dataParts[4]);
	}
	
	public double getLatitude() {return latitude;}
	public double getLongitude() {return longitude;}
	public double getMagnitude() {return magnitude;}
	public double getDepth() {return depth;}
	
	/* (non-Javadoc)
	 * Returns a string in a template form e.g. "M4.5, 23.23km, (1.123,-3.2222)"
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() 
	{		
		String template = "M%.1f, %.2fkm, (%.4f,%.4f)";
		return String.format(template, magnitude, depth, latitude, longitude);
	}
}
