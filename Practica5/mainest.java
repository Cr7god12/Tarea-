import java.util.Scanner;

public class mainest {
   
    	
    	public static void main(String[] args) {
    	Scanner scanner = new Scanner(System.in);
    	double[] numeros = new double[10];

    	System.out.println("Ingrese 10 números:");

    	for (int i = 0; i < 10; i++) {
    		numeros[i] = scanner.nextDouble();
    	}

    	Estadistica estadistica = new Estadistica(numeros);
    	estadistica.mostrarResultados();

    	scanner.close();
 
    }
}