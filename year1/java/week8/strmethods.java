// Examples of using String methods - compare with strmethods.cpp
// See also http://docs.oracle.com/javase/7/docs/api/java/lang/String.html
// (NDE, 2015-02-22)

class StrMethods
{
  public static void main(String[] args)
  {
    String word = "Maximum";

    System.out.println("Word: " + word);
    System.out.println("Length: " + word.length());
    System.out.println("First three chars: " + word.substring(0, 3));
    System.out.println("Position of 'x': " + word.indexOf("x"));

    String newWord = word.replaceFirst("Max", "Min");
    System.out.println("After replacing chars: " + newWord);
  }
}
