public class JuegoAdivinaPar extends JuegoAdivinaNumero {

    public JuegoAdivinaPar(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    @Override
    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10) {
            if (numero % 2 == 0) {
                
                return true;
            } else {
                System.out.println("Debe ser Par.");
                return false;
            }
        } else {
            System.err.println("fuera del rango");
            return false;
        }
    }
}
