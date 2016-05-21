package comp2541.coursework2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


/**
 * A class to represent a collection of playing cards.
 *
 * <p>The intent is that this should form the basis for new classes
 * useful in card games.  It isn't meant to be instantiated itself and
 * is therefore declared as abstract.</p>
 *
 * <p>Provided for use in COMP2541 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public abstract class CardCollection
{
  protected List<Card> cards = new ArrayList<Card>();


  /**
   * Indicates whether a particular card is present in this collection.
   *
   * @param card Card we are looking for
   * @return True if the card is present, false otherwise
   */
  public boolean contains(Card card)
  {
    return cards.contains(card);
  }


  /**
   * @return True if this collection is empty, false otherwise
   */
  public boolean isEmpty()
  {
    return cards.isEmpty();
  }


  /**
   * @return Number of cards in this collection
   */
  public int size()
  {
    return cards.size();
  }


  /**
   * Puts the specified card in this collection.
   *
   * @param card Card to be added
   * @throws IllegalArgumentException if the card is already present
   */
  public void add(Card card)
  {
    if (contains(card)) {
      throw new IllegalArgumentException("card already present");
    }

    cards.add(card);
  }


  /**
   * Sorts this collection's cards into order.
   */
  public void sort()
  {
    Collections.sort(cards);
  }
}
