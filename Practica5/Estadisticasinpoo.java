

import java.util.Scanner;

public class Estadisticasinpoo {
    static int N = 10;
    public static double Promedio(double[] numeros) {
        double suma = 0;
        for (int i = 0; i < N; i++) {
            suma += numeros[i];
        }
        double prom=suma / N;
        return prom;
    }
    public static double Desviacion(double[] numeros, double promedio) {
        double sumaDiferencias = 0;
        for (int i = 0; i < N; i++) {
            sumaDiferencias += (numeros[i] - promedio) * (numeros[i] - promedio);
        }
        double des=Math.sqrt(sumaDiferencias / (N - 1));
        return des ;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] num = new double[N];

        System.out.println("Ingrese 10 números:");

        for (int i = 0; i < N; i++) {
            num[i] = scanner.nextDouble();
        }

        double prom = Promedio(num);
        double des= Desviacion(num, prom);

        System.out.printf("El promedio es: %.2f\n", prom);
        System.out.printf("La desviación estándar es: %.2f\n", des);

        scanner.close();
    }
}
