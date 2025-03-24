import  java.util.Scanner;
public class maincua {
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese a: ");
        double a = scanner.nextDouble();
        System.out.print("Ingrese b: ");
        double b = scanner.nextDouble();
        System.out.print("Ingrese c: ");
        double c = scanner.nextDouble();
        

    
        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);
        ecuacion.mostrarSolucion();
        

        scanner.close();
    }
}