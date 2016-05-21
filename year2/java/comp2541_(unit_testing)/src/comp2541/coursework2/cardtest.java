package comp2541.coursework2;

import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.MatcherAssert.*;
import static org.hamcrest.number.OrderingComparison.*;


/**
 * Unit tests for Card class.
 *
 * <p>Provided for use in COMP2541 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class CardTest
{
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
    }


    @Test public void testHashCode()
    {
        Card card = new Card("AC");
        assertThat(aceClubs.hashCode(), equalTo(card.hashCode()));
        assertThat(aceClubs.hashCode(), not(equalTo(twoClubs.hashCode())));
        assertThat(twoClubs.hashCode(), not(equalTo(twoDiamonds.hashCode())));
        assertThat(aceClubs.hashCode(), not(equalTo(kingSpades.hashCode())));
    }


    @Test public void testEquals()
    {
        assertThat(aceClubs, equalTo(aceClubs));
        assertThat(aceClubs, equalTo(new Card("AC")));
        assertThat(aceClubs, not(equalTo(null)));
        assertThat(aceClubs, not(equalTo(twoClubs)));
        assertThat(twoClubs, not(equalTo(twoDiamonds)));
        assertThat(aceClubs, not(equalTo(jackHearts)));
    }


    @Test public void testToString()
    {
        assertThat(aceClubs.toString(), equalTo("AC"));
        assertThat(twoDiamonds.toString(), equalTo("2D"));
        assertThat(kingSpades.toString(), equalTo("KS"));
    }


    @Test public void testCompareTo()
    {
        assertThat(aceClubs.compareTo(aceClubs), equalTo(0));
        assertThat(aceClubs.compareTo(twoClubs), lessThan(0));
        assertThat(twoClubs.compareTo(twoDiamonds), lessThan(0));
        assertThat(kingSpades.compareTo(jackHearts), greaterThan(0));
    }


    @Test public void testImageLoading()
    {
        assertThat(aceClubs.getImage(), not(equalTo(null)));
        assertThat(twoDiamonds.getImage(), not(equalTo(null)));
        assertThat(kingSpades.getImage(), not(equalTo(null)));
    }
}
