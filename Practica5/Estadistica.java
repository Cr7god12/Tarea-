
class Estadistica {
    double[] numeros;
    int N = 10; 

    public Estadistica(double[] nums) {
        numeros = nums;
    }

    public double Promedio() {
        double suma = 0;
        for (int i = 0; i < N; i++) {
            suma += numeros[i];
        }
        double prom = suma/N;
        return prom;
    }

    public double Desviacion() {
        double promedio = Promedio();
        double sumaDiferencias = 0;
        for (int i = 0; i < N; i++) {
            sumaDiferencias += (numeros[i] - promedio) * (numeros[i] - promedio);
        }
        double des = Math.sqrt(sumaDiferencias / (N - 1));
        
        return des;
    }

    
}







