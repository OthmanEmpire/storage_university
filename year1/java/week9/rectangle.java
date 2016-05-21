class Rectangle
{
  private int x, y, width, height;

  public Rectangle(int x, int y, int w, int h)
  {
    if (w < 1 || h < 1) {
      throw new IllegalArgumentException("width & height must be >= 1");
    }

    this.x = x;
    this.y = y;
    width = w;
    height = h;
  }

  public int getX() { return x; }

  public int getY() { return y; }

  public int getWidth() { return width; }

  public int getHeight() { return height; }

  public int calculatePerimeter() { return 2*(width + height); }

  public int calculateArea() { return width*height; }
}
