import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    private int numeroAAdivinar;

    public JuegoAdivinaNumero(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
    }

    public void juega() {
        reiniciaPartida();
        Random random = new Random();
        numeroAAdivinar = random.nextInt(11); // número entre 0 y 10

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Adivina un número entre 0 y 10: ");
            int intento = scanner.nextInt();

            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!!");
                actualizaRecord();
                break;
            } else {
                boolean quedanVidas = quitaVida();
                if (quedanVidas) {
                    if (intento < numeroAAdivinar) {
                        System.out.println("El número a adivinar es mayor. Intenta de nuevo.");
                    } else {
                        System.out.println("El número a adivinar es menor. Intenta de nuevo.");
                    }
                } else {
                    break;
                }
            }
        }
    }
}
