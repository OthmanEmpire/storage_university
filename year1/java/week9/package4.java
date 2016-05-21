// Example of how injudicious use of the '*' form of an
// import statement can lead to problems
// (NDE, 2010-05-24)

import java.sql.*;
import java.util.*;

class Package4
{
  public static void main(String[] args)
  {
    long now = System.currentTimeMillis();
    Date date = new Date(now);   // which Date class is intended here?
  }
}
