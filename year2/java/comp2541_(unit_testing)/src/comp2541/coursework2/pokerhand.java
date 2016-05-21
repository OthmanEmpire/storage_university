package comp2541.coursework2;

import java.util.Hashtable;
import java.util.Map;


/**
 * Represents a standard poker hand from the card game poker.
 * Simplifies dealing hands and checking for special type of
 * hands (e.g. three of a kind).
 *
 * @author Othman Alikhan.
 */
public class PokerHand extends CardCollection
{

    /**
     * Adds a card to the poker hand.
     *
     * @param card Card to be added
     * @throws IllegalArgumentException if the hand contains a full poker hand.
     */
    @Override public void add(Card card)
    {
        int maxHandSize = 5;

     if (cards.size() == maxHandSize)
     {
          throw new IllegalArgumentException("Cannot add any more cards to the hand which is full.");
     }
        cards.add(card);
    }

    /**
     * Displays the current cards in the hand. For instance, "KS AC" for
     * king of spades and ace of clubs.
     */
    @Override public String toString()
    {
        String stringHand = "";

        // Checks whether hand is empty otherwise it generates a string containing the cards in the hand
        if(cards.size() == 0) { stringHand = "<empty>"; }
        else{ for(Card card : cards) { stringHand += card.toString() + " "; } }

        // Removes trailing space in stringHand
        if(stringHand.endsWith(" ")) { stringHand = stringHand.substring(0, stringHand.length()-1); }

        return stringHand;
    }

    /**
     * Checks whether the current hand is a valid flush (i.e. 5 cards of the same suit)
     */
    public boolean isFlush()
    {
        Character handSuit = null;

        // Checks whether all hand contains 5 cards
        if(cards.size() != 5) { return false; }

        // Checks whether hand has cards of same suit
        handSuit = cards.get(0).getSuit();
        for (Card card : cards) { if(card.getSuit() != handSuit){ return false; } }

        return true;
    }

    /**
     * Checks whether the current hand is a valid three of a kind (i.e. only 3 cards of the same rank)
     *
     * This is done by creating a dictionary of (rank, occurrence) for each possible rank. Then
     * updating the dictionary based on the current hand. Then checking how many sets of the
     * same rank have occurred and whether they match our needs for this poker hand.
     * (e.g. "AC AH 2D 3C 4D" contains 1 set of two same ranks and 3 sets of single ranks)
     */
    public boolean hasThreeOfAKind()
    {
        int sameRankSize = 3;        // Amount of cards of the same rank
        int numSameRankSize = 0;
        int requiredNumSameRankSize = 1;

        // Initializes a dictionary of ranks (rank, occurrence)
        Map<Character, Integer> rankDictionary = new Hashtable<Character, Integer>();
        for (Character rank : Card.getRanks()) { rankDictionary.put(rank, 0); }

        // Checks whether all hand contains 5 cards
        if(cards.size() != 5) { return false; }

        // Counts the occurrences of each rank in the hand
        for (Card card : cards) {
            rankDictionary.put(card.getRank(), rankDictionary.get(card.getRank()) + 1);
        }

        // Counts how many sets of the of the same rank
        for(Map.Entry<Character, Integer> entry: rankDictionary.entrySet()) {
            if(entry.getValue() == sameRankSize) { numSameRankSize += 1; }
        }

        // Checks whether the amount of sets of the same rank meets the requirements
        // of this special poker hand
        if(numSameRankSize == requiredNumSameRankSize) { return true; }
        else { return false; }
    }

    /**
     * Checks whether the current hand is a valid four of a kind (i.e. only 4 cards of the same rank)
     *
     * This is done by creating a dictionary of (rank, occurrence) for each possible rank. Then
     * updating the dictionary based on the current hand. Then checking how many sets of the
     * same rank have occurred and whether they match our needs for this poker hand.
     * (e.g. "AC AH 2D 3C 4D" contains 1 set of two same ranks and 3 sets of single ranks)
     */
    public boolean hasFourOfAKind()
    {
        int sameRankSize = 4;       // Amount of cards of the same rank
        int numSameRankSize = 0;
        int requiredNumSameRankSize = 1;

        // Initializes a dictionary of ranks (rank, occurrence)
        Map<Character, Integer> rankDictionary = new Hashtable<Character, Integer>();
        for (Character rank : Card.getRanks()) { rankDictionary.put(rank, 0); }

        // Checks whether all hand contains 5 cards
        if(cards.size() != 5) { return false; }

        // Counts the occurrences of each rank in the hand
        for (Card card : cards) {
            rankDictionary.put(card.getRank(), rankDictionary.get(card.getRank()) + 1);
        }

        // Counts how many sets of the of the same rank
        for(Map.Entry<Character, Integer> entry: rankDictionary.entrySet()) {
            if(entry.getValue() == sameRankSize) { numSameRankSize += 1; }
        }

        // Checks whether the amount of sets of the same rank meets the requirements
        // of this special poker hand
        if(numSameRankSize == requiredNumSameRankSize) { return true; }
        else { return false; }
    }

    /**
     * Checks whether the current hand is a valid two pair (i.e. only 2 sets of pairs of the same rank
     * but both pairs differ in terms of rank)
     *
     * This is done by creating a dictionary of (rank, occurrence) for each possible rank. Then
     * updating the dictionary based on the current hand. Then checking how many sets of the
     * same rank have occurred and whether they match our needs for this poker hand.
     * (e.g. "AC AH 2D 3C 4D" contains 1 set of two same ranks and 3 sets of single ranks)
     */
    public boolean hasTwoPair()
    {
        int sameRankSize = 2;       // Amount of cards of the same rank
        int numSameRankSize = 0;
        int requiredNumSameRankSize = 2;

        // Initializes a dictionary of ranks (rank, occurrence)
        Map<Character, Integer> rankDictionary = new Hashtable<Character, Integer>();
        for (Character rank : Card.getRanks()) { rankDictionary.put(rank, 0); }

        // Checks whether all hand contains 5 cards
        if(cards.size() != 5) { return false; }

        // Counts the occurrences of each rank in the hand
        for (Card card : cards) {
            rankDictionary.put(card.getRank(), rankDictionary.get(card.getRank()) + 1);
        }

        // Counts how many sets of the of the same rank
        for(Map.Entry<Character, Integer> entry: rankDictionary.entrySet()) {
            if(entry.getValue() == sameRankSize) { numSameRankSize += 1; }
        }

        // Checks whether the amount of sets of the same rank meets the requirements
        // of this special poker hand
        if(numSameRankSize == requiredNumSameRankSize) { return true; }
        else { return false; }
    }
}
