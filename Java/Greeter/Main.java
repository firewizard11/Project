import java.util.Scanner; 

public class Main {

    public static void main(String[] args) {
        String name;

        System.out.print("Enter your name: ");
        Scanner UserInput = new Scanner(System.in);
        name = UserInput.nextLine();

        System.out.print("Hello " + name);
    }

}