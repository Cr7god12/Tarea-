
public class Juego {
    protected int numeroDeVidas;
    protected int record;

    public void reiniciaPartida() {
        numeroDeVidas = 3;
    }

    public void actualizaRecord() {
        record++;
        System.out.println("Record actualizado: " + record);
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        if (numeroDeVidas > 0) {
            return true;
        } else {
            System.out.println("¡Has perdido todas tus vidas!");
            return false;
        }
    }
}
