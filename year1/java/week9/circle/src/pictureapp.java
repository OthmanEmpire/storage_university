import java.awt.BorderLayout;
import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JScrollPane;

/**
 * A simple picture drawing application.
 *
 * @author Nick Efford
 * @version 1.3 (2013-09-17)
 */
public class PictureApp implements Runnable
{
  private Picture picture;

  /**
   * Creates a PictureApp with an associated picture.
   */
  public PictureApp()
  {
    picture = new Picture();
  }

  /**
   * Creates GUI for this application.
   */
  public void run()
  {
    JFrame frame = new JFrame("Picture");
    PictureCanvas canvas = new PictureCanvas(picture);
    frame.add(new JScrollPane(canvas), BorderLayout.CENTER);
    frame.pack();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);    
  }

  /**
   * Application entry point.
   *
   * @param args Command-line arguments (unused)
   */
  public static void main(String[] args)
  {
    EventQueue.invokeLater(new PictureApp());
  }
}