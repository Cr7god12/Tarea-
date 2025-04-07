public class Main {
    public static void main(String[] args) {
        JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3);
        juego1.juega();

        JuegoAdivinaPar juego2 = new JuegoAdivinaPar(3);
        juego2.juega();

        JuegoAdivinaImpar juego3 = new JuegoAdivinaImpar(3);
        juego3.juega();
    }
}
