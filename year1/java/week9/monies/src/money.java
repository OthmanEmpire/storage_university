
/**
 * An amount of money in European currency.
 * 
 * <p>The amount is represented in whole numbers of euros and cents.</p>
 * 
 * @author Ozkh
 */
public class Money 
{
	private int euros;
	private int cents;
	
	/**
	 * @param euros
	 * @param cents
	 * @throws IllegalArgumentException 
	 */
	public Money(int euros, int cents) 
	{
		if (euros < 0)
		{
			throw new IllegalArgumentException("invalid euros");
		}
		
		if (cents < 0 || cents > 99)
		{
			throw new IllegalArgumentException("invalid cents");
		}
		
		this.euros = euros;
		this.cents = cents;
	}

	public int getEuros() {
		return euros;
	}

	public int getCents() {
		return cents;
	}

	@Override
	public String toString() {
		return String.format("Money [euros=%s, cents=%s]", euros, cents);
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + cents;
		result = prime * result + euros;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (!(obj instanceof Money)) {
			return false;
		}
		Money other = (Money) obj;
		if (cents != other.cents) {
			return false;
		}
		if (euros != other.euros) {
			return false;
		}
		return true;
	}
	
	public static void main(String[] args)
	{
		System.out.println("GG");
	}
}
