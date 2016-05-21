import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;

/**
 * A GUI component within which a Picture can be drawn.
 *
 * @author Nick Efford
 * @version 1.3 (2013-09-17)
 */
public class PictureCanvas extends JComponent
{
  private static final long serialVersionUID = 1L;
  private static final int CANVAS_WIDTH = 400;
  private static final int CANVAS_HEIGHT = 400;

  private Picture picture;

  /**
   * Creates a PictureCanvas.
   */
  public PictureCanvas(Picture pic)
  {
    setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));
    picture = pic;
  }

  @Override public void paintComponent(Graphics context)
  {
    super.paintComponent(context);
    picture.draw((Graphics2D) context);
  }
}