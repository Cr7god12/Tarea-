import  java.util.Scanner;
public class maincua {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el valor de a: ");
        double a = scanner.nextDouble();
        System.out.print("Ingrese el valor de b: ");
        double b = scanner.nextDouble();
        System.out.print("Ingrese el valor de c: ");
        double c = scanner.nextDouble();

        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);

        double discriminante = ecuacion.getDiscriminante();

         if (discriminante > 0) {
            System.out.printf("La ecuación tiene dos raíces:"+ ecuacion.getRaiz1(), ecuacion.getRaiz2());
        } else if (discriminante == 0) {
            System.out.printf("La ecuación tiene una raíz:"+ ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales.");
        }

        scanner.close();
    }
}
    
