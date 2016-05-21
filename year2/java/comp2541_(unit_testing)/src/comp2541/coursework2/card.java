package comp2541.coursework2;

import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import javax.imageio.ImageIO;


/**
 * Simple representation of a playing card.
 *
 * <p>Provided for use in COMP2541 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class Card implements Comparable<Card>
{
  /*--------------------------- Class-level code ---------------------------*/


  private static final List<Character> RANKS = Arrays.asList(
   'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'
  );

  private static final List<Character> SUITS = Arrays.asList(
   'C', 'D', 'H', 'S'
  );

  private static Map<String,BufferedImage> images = new HashMap<>();

  static {
    try (ZipFile zip = new ZipFile("images.zip")) {
      for (char suit : Card.getSuits()) {
        for (char rank : Card.getRanks()) {
          String card = String.format("%c%c", rank, suit);
          String filename = card + ".png";
          ZipEntry entry = zip.getEntry(filename);
          BufferedImage image = ImageIO.read(zip.getInputStream(entry));
          images.put(card, image);
        }
      }
    }
    catch (IOException error) {
      // Do nothing if images cannot be loaded
    }
  }


  /**
   * @return An unmodifiable list of the characters representing card ranks
   */
  public static List<Character> getRanks()
  {
    return Collections.unmodifiableList(RANKS);
  }


  /**
   * @return An unmodifiable list of the characters representing card suits
   */
  public static List<Character> getSuits()
  {
    return Collections.unmodifiableList(SUITS);
  }


  /*------------------------- Instance-level code --------------------------*/


  private char rank;
  private char suit;


  /**
   * Creates a Card object.
   *
   * @param rank Rank of the card
   * @param suit Suit of the card
   * @throws IllegalArgumentException if rank or suit are invalid
   */
  public Card(char rank, char suit)
  {
    set(rank, suit);
  }


  /**
   * Creates a Card object.
   *
   * @param code Two-character code representing the card - e.g., "AC"
   * @throws IllegalArgumentException if code is invalid
   */
  public Card(String code)
  {
    if (code.length() != 2) {
      throw new IllegalArgumentException("card codes must be two characters");
    }

    set(code.charAt(0), code.charAt(1));
  }


  /**
   * @return Current value of rank
   */
  public char getRank()
  {
    return rank;
  }


  /**
   * @return Current value of suit
   */
  public char getSuit()
  {
    return suit;
  }
  

  /**
   * @return Image associated with this card
   */
  public BufferedImage getImage()
  {
    return images.get(String.format("%c%c", rank, suit));
  }


  /* (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override public int hashCode()
  {
    final int prime = 31;
    int result = 1;
    result = prime * result + rank;
    result = prime * result + suit;
    return result;
  }


  /* (non-Javadoc)
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @Override public boolean equals(Object thing)
  {
    boolean same = false;

    if (thing == this) {
      same = true;
    }
    else if (thing != null && thing instanceof Card) {
      final Card card = (Card) thing;
      if (rank == card.rank && suit == card.suit) {
        same = true;
      }
    }

    return same;
  }


  /* (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override public String toString()
  {
    return String.format("%c%c", rank, suit);
  }


  /* (non-Javadoc)
   * @see java.lang.Comparable#compareTo(java.lang.Object)
   */
  @Override public int compareTo(Card other)
  {
    int mySuit = SUITS.indexOf(suit);
    int otherSuit = SUITS.indexOf(other.suit);
    int difference = mySuit - otherSuit;

    if (difference == 0) {
      int myRank = RANKS.indexOf(rank);
      int otherRank = RANKS.indexOf(other.rank);
      difference = myRank - otherRank;
    }

    return difference;
  }


  /*------------------------ Private helper methods ------------------------*/


  private void set(char rank, char suit)
  {
    if (! RANKS.contains(rank)) {
      throw new IllegalArgumentException("invalid rank");
    }

    if (! SUITS.contains(suit)) {
      throw new IllegalArgumentException("invalid suit");
    }

    this.rank = rank;
    this.suit = suit;
  }
}
