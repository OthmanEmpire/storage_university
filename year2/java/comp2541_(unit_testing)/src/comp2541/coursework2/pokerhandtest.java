package comp2541.coursework2;

import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.MatcherAssert.*;


/**
 * Unit tests for the PokerHand class.
 *
 * @author Othman Alikhan
 */
public class PokerHandTest
{
    private PokerHand emptyHand;
    private PokerHand fullHand;
    private PokerHand singleCardHand;
    private PokerHand notFlushHand;
    private PokerHand flushHand;
    private PokerHand twoOfAKindHand;
    private PokerHand threeOfAKindHand;
    private PokerHand fourOfAKindHand;
    private PokerHand fullSameHand;
    private PokerHand twoPairHand;
    private PokerHand notTwoPairHand;

    private Card aceClubs;
    private Card twoClubs;
    private Card twoDiamonds;
    private Card jackHearts;
    private Card kingSpades;

    @Before public void setUp()
    {
        aceClubs = new Card("AC");
        twoClubs = new Card("2C");
        twoDiamonds = new Card("2D");
        jackHearts = new Card("JH");
        kingSpades = new Card("KS");

        // Empty hand: "<empty>"
        emptyHand = new PokerHand();

        // Full hand: "KS KS KS KS KS"
        fullHand = new PokerHand();
        for(int i = 0; i < 5; i++) { fullHand.add(kingSpades); }

        // Single card hand: "KS"
        singleCardHand = new PokerHand();
        singleCardHand.add(kingSpades);

        // non-flush hand: "AC 2C 2D JH KS"
        notFlushHand = new PokerHand();
        notFlushHand.add(aceClubs);
        notFlushHand.add(twoClubs);
        notFlushHand.add(twoDiamonds);
        notFlushHand.add(jackHearts);
        notFlushHand.add(kingSpades);

        // Flush hand: "2C AC AC AC AC"
        flushHand = new PokerHand();
        flushHand.add(twoClubs);
        for(int i = 0; i < 4; i++) { flushHand.add(aceClubs); }

        // Two of a kind hand: "KS KS AC JH 2D"
        twoOfAKindHand = new PokerHand();
        twoOfAKindHand.add(kingSpades);
        twoOfAKindHand.add(kingSpades);
        twoOfAKindHand.add(aceClubs);
        twoOfAKindHand.add(jackHearts);
        twoOfAKindHand.add(twoDiamonds);

        // Three of a kind hand: "KS KS KS JH 2D"
        threeOfAKindHand = new PokerHand();
        threeOfAKindHand.add(kingSpades);
        threeOfAKindHand.add(kingSpades);
        threeOfAKindHand.add(kingSpades);
        threeOfAKindHand.add(jackHearts);
        threeOfAKindHand.add(twoDiamonds);

        // Four of a kind hand: "KS KS KS KS 2D"
        fourOfAKindHand = new PokerHand();
        fourOfAKindHand.add(kingSpades);
        fourOfAKindHand.add(kingSpades);
        fourOfAKindHand.add(kingSpades);
        fourOfAKindHand.add(kingSpades);
        fourOfAKindHand.add(twoDiamonds);

        // Same full hand: "KS KS KS KS KS"
        fullSameHand = new PokerHand();
        for(int i = 0; i < 5; i++) { fullSameHand.add(kingSpades); }

        // Two pair hand: "JH JH 2D 2C AC"
        twoPairHand = new PokerHand();
        twoPairHand.add(jackHearts);
        twoPairHand.add(jackHearts);
        twoPairHand.add(twoDiamonds);
        twoPairHand.add(twoClubs);
        twoPairHand.add(aceClubs);

        // Not a two pair hand: "JH KS 2D 2C AC"
        notTwoPairHand = new PokerHand();
        notTwoPairHand.add(jackHearts);
        notTwoPairHand.add(kingSpades);
        notTwoPairHand.add(twoDiamonds);
        notTwoPairHand.add(twoClubs);
        notTwoPairHand.add(aceClubs);
    }



    /**
     * Checks whether the add method fails when adding a card
     * to a full deck.
     */
    @Test(expected=IllegalArgumentException.class) public void testAdd()
    {
        // Attempts to add a sixth card to the hand
        fullHand.add(aceClubs);
        assertThat(fullHand.size(), equalTo(5));
    }

    /**
     * Checks that the toString method returns "<empty>" if there are no cards
     * in the current hand. Otherwise it returns, for instance, "AC 4D" for a
     * ace of spades and four of diamonds in the current hand.
     */
    @Test public void testToString()
    {
        assertThat(emptyHand.toString(), equalTo("<empty>"));
        assertThat(notFlushHand.toString(), equalTo("AC 2C 2D JH KS"));
    }

    /**
     * Checks that the isFlush method works (i.e. five cards of the same suit)
     */
    @Test public void testIsFlush()
    {
        assertThat(emptyHand.isFlush(), equalTo(false));
        assertThat(singleCardHand.isFlush(), equalTo(false));
        assertThat(notFlushHand.isFlush(), equalTo(false));
        assertThat(flushHand.isFlush(), equalTo(true));
    }

    /**
     * Checks that the hasThreeOfAKind method works (i.e. only three cards of the same rank)
     */
    @Test public void testHasThreeOfAKind()
    {
        assertThat(emptyHand.hasThreeOfAKind(), equalTo(false));
        assertThat(singleCardHand.hasThreeOfAKind(), equalTo(false));
        assertThat(twoOfAKindHand.hasThreeOfAKind(), equalTo(false));
        assertThat(threeOfAKindHand.hasThreeOfAKind(), equalTo(true));
        assertThat(fourOfAKindHand.hasThreeOfAKind(), equalTo(false));
    }


    /**
     * Checks that the hasFourOfAKind method works (i.e. only four cards of the same rank)
     */
    @Test public void testHasFourOfAKind()
    {
        assertThat(emptyHand.hasFourOfAKind(), equalTo(false));
        assertThat(singleCardHand.hasFourOfAKind(), equalTo(false));
        assertThat(twoOfAKindHand.hasFourOfAKind(), equalTo(false));
        assertThat(threeOfAKindHand.hasFourOfAKind(), equalTo(false));
        assertThat(fullSameHand.hasFourOfAKind(), equalTo(false));
        assertThat(fourOfAKindHand.hasFourOfAKind(), equalTo(true));
    }

    /**
     * Checks that the hasTwoPair method works (i.e. only two pair cards of the same rank
     * but both pairs must be of different ranks)
     */
    @Test public void testHasTwoPair()
    {
        assertThat(emptyHand.hasTwoPair(), equalTo(false));
        assertThat(singleCardHand.hasTwoPair(), equalTo(false));
        assertThat(twoOfAKindHand.hasTwoPair(), equalTo(false));
        assertThat(threeOfAKindHand.hasTwoPair(), equalTo(false));
        assertThat(fourOfAKindHand.hasTwoPair(), equalTo(false));
        assertThat(fullSameHand.hasTwoPair(), equalTo(false));
        assertThat(notTwoPairHand.hasTwoPair(), equalTo(false));
        assertThat(twoPairHand.hasTwoPair(), equalTo(true));
    }
}
