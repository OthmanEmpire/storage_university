public class TestCircle {
	
	public static void main(String args[]) {
		Circle circ1 = new Circle(1, 1, 10);

		System.out.println(circ1);
		System.out.println("Area: " + circ1.calculateArea());
		System.out.println("Perimeter: " + circ1.calculatePerimeter());
	}

}
