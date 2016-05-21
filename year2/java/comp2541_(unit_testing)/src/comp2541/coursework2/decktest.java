package comp2541.coursework2;

import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.MatcherAssert.*;


/**
 * Unit tests for the Deck class.
 *
 * @author Othman Alikhan
 */
public class DeckTest
{
    private Deck deck;
    private Card aceClubs;
    private Card twoClubs;
    private Card kingSpades;


    /**
     * Sets up a deck with 52 cards.
     * Also, creates other independent cards.
     */
    @Before public void setUp()
    {
        deck = new Deck();      // Deck containing 52 cards
        aceClubs = new Card("AC");
        twoClubs = new Card("2C");
        kingSpades = new Card("KS");
    }

    /**
     * Checks whether a deck contains 52 cards.
     */
    @Test public void testCreation()
    {
        Deck newDeck = new Deck();
        assertThat(newDeck.size(), equalTo(52));
    }

    /**
     * Checks whether the contain method works.
     */
    @Test public void testContains()
    {
        assertThat(deck.contains(aceClubs), equalTo(true));
        assertThat(deck.contains(twoClubs), equalTo(true));
        assertThat(deck.contains(kingSpades), equalTo(true));
    }

    /**
     * Checks whether the deal method removes the first most card
     * and reduces the size of the deck.
     */
    @Test public void testDeal()
    {
        assertThat(deck.cards.get(0), equalTo(deck.deal()));
        assertThat(deck.size(), equalTo(51));
    }

    /**
     * Checks whether adding a missing card is successful.
     */
    @Test public void testAdd()
    {
        // Removes the card first from the deck
        Card removedCard = deck.deal();
        assertThat(deck.contains(removedCard), equalTo(false));

        // Adds the removed card back into the deck
        deck.add(removedCard);
        assertThat(deck.contains(removedCard), equalTo(true));
    }

    /**
     * Checks whether adding an existing card throws an exception.
     */
    @Test(expected=IllegalArgumentException.class) public void testFailedAdd()
    {
        deck.add(aceClubs);
    }
}
