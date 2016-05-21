package comp2541.coursework2;

import java.util.*;


/**
 * A small program that unravels the mysterious probabilities
 * of poker and perhaps life too...
 *
 * @author Othman Alikhan
 */
public class Probabilities {

    /**
     * Generates raw data to calculate the probabilities of a special
     * poker hand occurring by running a large number of iterations.
     *
     * Each iterations generates a new deck and deals a poker hand
     * which is inspected and counted if a special poker hand type
     * has occurred.
     *
     * The data is stored and returned as a Map of
     * (poker hand type, amount of times occurred)
     *
     * @return Map of (poker hand type, amount of times occurred)
     */
    private Map<String, Integer> generateData(int iterations)
    {
        int handSize = 5;
        String handType = "";

        Deck deck;
        PokerHand pokerHand;
        Map<String, Integer> pokerHandDictionary;

        // A dictionary that maps (poker hand type, amount of times occurred)
        pokerHandDictionary = new LinkedHashMap<String, Integer>();
        pokerHandDictionary.put("TotalHands", 0);
        pokerHandDictionary.put("Flush", 0);
        pokerHandDictionary.put("ThreeOfAKind", 0);
        pokerHandDictionary.put("FourOfAKind", 0);
        pokerHandDictionary.put("TwoPair", 0);

        // Iterates a large number of times to improve numerical estimations
        for(int i = 0; i < iterations; i++)
        {
            // Generates a new deck and shuffles it per iterations
            deck = new Deck();
            deck.shuffle();

            // Deals a total of 50 cards from a deck of 52 cards
            for(int j = 0; j < 5; j++) {

                // Creates a new poker hand for every 5 cards dealt
                pokerHand = new PokerHand();
                for(int k = 0; k < handSize; k++)
                    pokerHand.add(deck.deal());

                // Checks whether a special poker hand type has been dealt

                if(pokerHand.isFlush() == true)
                {
                    handType = "Flush";
                    pokerHandDictionary.put(handType, pokerHandDictionary.get(handType)+1);
                }
                if(pokerHand.hasThreeOfAKind() == true)
                {
                    handType = "ThreeOfAKind";
                    pokerHandDictionary.put(handType, pokerHandDictionary.get(handType)+1);
                }

                if(pokerHand.hasFourOfAKind() == true)
                {
                    handType = "FourOfAKind";
                    pokerHandDictionary.put(handType, pokerHandDictionary.get(handType)+1);
                }
                if (pokerHand.hasTwoPair() == true)
                {
                    handType = "TwoPair";
                    pokerHandDictionary.put(handType, pokerHandDictionary.get(handType)+1);
                }
                // Keeps track of total hands dealt
                handType = "TotalHands";
                pokerHandDictionary.put(handType, pokerHandDictionary.get(handType)+1);
            }
        }
        return pokerHandDictionary;
    }


    /**
     * Prints the table of occurrences and probabilities of special poker hands occurring
     * (data is derived from generateData method).
     *
     * @param pokerHandDictionary contains the data of the form (rank, occurrences)
     */
    public void printProbabilities(Map<String, Integer> pokerHandDictionary)
    {
        String handOccurrenceTemplate = "Poker hand type: %s ||  Occurrences: %d";
        String handProbabilityTemplate = "P(%s) = %.3f %%";
        String headerTemplate = "Total amount of hands dealt: %d\n";

        int totalHandsDealt = 0;
        double handProbability = 0.0;

        Map.Entry<String, Integer> handEntry = null;
        Iterator<Map.Entry<String, Integer>> entriesIterator;
        entriesIterator = pokerHandDictionary.entrySet().iterator();

        System.out.println(String.format("----------------------------------------------"));

        // Prints the header (total amount of hands dealt)
        Map.Entry<String, Integer> totalHandsDealtEntry = entriesIterator.next();
        totalHandsDealt = totalHandsDealtEntry.getValue();
        System.out.println(String.format(headerTemplate, totalHandsDealt));

        // Prints the body (amount of occurrences per type of hand)
        while(entriesIterator.hasNext())
        {
            handEntry = entriesIterator.next();
            System.out.println(String.format(handOccurrenceTemplate, handEntry.getKey(), handEntry.getValue()));
        }

        // 'Resets' iterator to point to first entry in dictionary
        entriesIterator = pokerHandDictionary.entrySet().iterator();
        entriesIterator.next();     // Skips header

        System.out.println();

        // Prints the body (probability per type of hand)
        while(entriesIterator.hasNext())
        {
            handEntry = entriesIterator.next();
            handProbability = ((double) handEntry.getValue() / totalHandsDealt) * 100;
            System.out.println(String.format(handProbabilityTemplate, handEntry.getKey(), handProbability));
        }

        System.out.println(String.format("----------------------------------------------"));
    }


    /**
     * Runs the poker hand simulation that generates data through numerical
     * means then estimates the probabilities of each special poker hand being dealt.
     *
     * @param iterations a means to refine numerical estimations (generally set to 100000)
     */
    public void runSimulation(int iterations)
    {
        printProbabilities(generateData(iterations));
    }


    /**
     * Runs the probabilities program which prints probabilities
     */
    public static void main(String args[])
    {
        int iterations = 100000;
        Probabilities probabilities = new Probabilities();

        probabilities.runSimulation(iterations);
    }
}
