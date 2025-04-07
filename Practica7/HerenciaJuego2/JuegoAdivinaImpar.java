public class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    
    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    @Override
    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10) {
            if (numero % 2 != 0) {
                
                return true;
                
            } else {
                System.out.println(" Debe ser Impar.");
                return false;
            }
        } else {
            System.err.println("esta fuera del rango");
            return false;
        }
    }
}
