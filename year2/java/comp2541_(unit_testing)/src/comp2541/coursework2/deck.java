package comp2541.coursework2;

import java.util.Collections;


/**
 * A standard deck of 52 playing cards.
 *
 * <p>Provided for use in COMP2541 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class Deck extends CardCollection
{
  /**
   * Creates a deck of 52 cards.
   */
  public Deck()
  {
    for (char suit : Card.getSuits()) {
      for (char rank : Card.getRanks()) {
        cards.add(new Card(rank, suit));
      }
    }
  }


  /**
   * Deals a single card from the top of this deck.
   *
   * @return Card from the deck
   */
  public Card deal()
  {
    return cards.remove(0);
  }


  /**
   * Shuffles this deck randomly.
   */
  public void shuffle()
  {
    Collections.shuffle(cards);
  }
}
