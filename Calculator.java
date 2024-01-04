
public class Calculator {
    int result;

    public void add(int num1, int num2) {
        result = num1 + num2;
    }

    public void subtract(int num1, int num2) {
        result = num1 - num2;
    }

    public int getResult() {
        return result;
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        int num1 = 10;
        int num2 = 5;
        calculator.add(num1, num2);
        System.out.println("Addition result: " + calculator.getResult());
        calculator.subtract(num1, num2);
        System.out.println("Subtraction result: " + calculator.getResult());
    }
}
