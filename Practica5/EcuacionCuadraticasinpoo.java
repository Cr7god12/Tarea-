

import java.util.Scanner;

public class EcuacionCuadraticasinpoo {
    
    public static double getDiscriminante(double a, double b, double c) {
        double dis = b * b - 4 * a * c;
    	return dis; 
    }


    public static double getRaiz1(double a, double b, double discriminante) {
        double raiz1=(-b + Math.sqrt(discriminante)) / (2 * a);
    	return raiz1;
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        double raiz2=(-b - Math.sqrt(discriminante)) / (2 * a);
    	return raiz2;
    }

    public static void mostrarSolucion(double a, double b, double c) {
        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            double raiz1 = getRaiz1(a, b, discriminante);
            double raiz2 = getRaiz2(a, b, discriminante);
            System.out.println("La ecuación tiene dos raíces: " + raiz1 + " y " + raiz2);
        } else if (discriminante == 0) {
            double raiz = getRaiz1(a, b, discriminante);
            System.out.println("La ecuación tiene una raíz: " + raiz);
        } else {
            System.out.println("La ecuación no tiene raíces reales.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese a: ");
        double a = scanner.nextDouble();
        System.out.print("Ingrese b: ");
        double b = scanner.nextDouble();
        System.out.print("Ingrese c: ");
        double c = scanner.nextDouble();

   
        mostrarSolucion(a, b, c);
        

        scanner.close();
    }
}
