// Program demonstrating overflow prevention in Java
// (NDE, 2013-12-28)

class Overflow
{
  public static void main(String[] args)
  {
    short value = 30000;
    value += 20000;

    System.out.println(value);
  }
}
