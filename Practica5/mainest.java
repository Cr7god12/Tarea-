import java.util.Scanner;

public class mainest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] datos = new double[10];
        
        System.out.println("Ingrese 10 números :");
        for (int i = 0; i < 10; i++) {
            datos[i] = scanner.nextDouble();
        }
        
        Estadistica estadistica = new Estadistica(datos);
        double promedio = estadistica.Promedio();
        double desviacion = estadistica.Desviacion();
        
        System.out.printf("El promedio es: %.2f\n", promedio);
        System.out.printf("La desviación estándar es: %.2f\n", desviacion);
        
        scanner.close();
    }
}
