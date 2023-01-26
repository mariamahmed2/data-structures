import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

interface ICalculator {
    // Addition
    int add(int x, int y);
   // Division
    float divide(int x, int y) throws RuntimeException;
}


public class Calculator implements ICalculator{
    @Override
    public int add(int x, int y) {
        return x + y;
    }

    @Override
    public float divide(int x, int y) throws RuntimeException {
        if (y == 0) throw new RuntimeException(); // dividion by zero
        return (float) ((x * 1.0) / y);
    }
    /* calculator class Implementation*/
    public static void main(String[] args) {
            // Take the input equation
        Scanner input = new Scanner(System.in);
        int x = input.nextInt(); // first num
        char ch = input.next().charAt(0); // sign
        int y = input.nextInt(); // second num.
        ICalculator calculator = new Calculator();
        switch (ch) {
            case '+':
                System.out.println(calculator.add(x, y));
                break;
            case '/':
                try {
                    float z = calculator.divide(x, y);
                    System.out.println(z);
                } catch (RuntimeException e) {
                    System.out.println("Error");
                }
                break;
            default:
                System.out.println("Error");
        }
    }
}




