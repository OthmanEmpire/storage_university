package comp2541.coursework2;

import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.image.BufferedImage;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.Border;


/**
 * Simple Swing program to display a set of playing cards.
 *
 * <p>Provided for use in COMP2541 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class DisplayCards implements Runnable
{
  @Override public void run()
  {
    // Create a panel to hold the displayed cards

    JPanel panel = new JPanel();
    panel.setLayout(new GridLayout(4, 13, 5, 10));
    Border border = BorderFactory.createEmptyBorder(10, 10, 10, 10);
    panel.setBorder(border);

    // Fill the panel's grid with labels, one for each card in the deck

    for (char suit: Card.getSuits()) {
      for (char rank: Card.getRanks()) {
        Card card = new Card(rank, suit);
        BufferedImage image = card.getImage();
        if (image != null) {
          ImageIcon icon = new ImageIcon(image);
          panel.add(new JLabel(icon));
        }
        else {
          panel.add(new JLabel("?"));
        }
      }
    }

    // Create a window containing the panel and make it visible

    JFrame frame = new JFrame("Playing Cards");
    frame.add(panel);
    frame.pack();

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);
  }

  public static void main(String[] args)
  {
    EventQueue.invokeLater(new DisplayCards());
  }
}
