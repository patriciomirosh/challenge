package math;

import java.math.BigInteger;


public class Puzzle {    
final static BigInteger M =new BigInteger("2017"); 
private static BigInteger compute(long n){ // aca creo una varibale biginteger para luego llamarlo y usarlo para darles valor a n 


        
    
    
    String s =""; //inicializo una variable s sin valores.
    for (long i = 0; i<n;i++){
        s="58184241583791680"+s;   // en este bucle lo que hago es repetir la secuencia de s, hasta n numeros de veces 
      
        
         
    
    }
     return new BigInteger(s.toString()).mod(M);
      /* hago esto por este razonamiento : para no pasar por todo el bucle como en el ejemplo ya inicio en el final.
       pero voy imprimiendo la secuencia n veces.  Como yo se que la ultima secuencia a mostrar es:
        s veces la secuencia s se que el resultado de BigInteger(s.toString()).mod(M) va a tener una posibilidad de repetirse 2017 veces(2017 es primo )
        entonces cada 2017 secuencias de s se va a repetir la secuencia de resultados de  BigInteger(s.toString()).mod(M).
        entonces si se repite cada 2017 el resultado. Yo se que si calculo el residuo de 58184241583791680/2017 tendre un valor que me dira
        en que parte de la secuencia de repeticiones de resto me encuentro lo llamo H, ahora yo se que el resto de:  s veces s = H veces s.
        lo unico que tengo que hacer ahora es hallar el BigInteger(s.toString()).mod(M) cuando n sea igual a H y con eso soluciono el problema.
       
     */
   
     
         

}
  public static void main(String[] args) {
     for(long n: new long[]{1L,2L,3L,2017L,2018L,2005L,2019L}){
         System.out.println(""+ n + ":"+ compute(n));
     }
 }     
    /*  Para finalizar el programa compruebo que se repite cada 2017 veces el mod con n=1,n=2 y n=2017,n=2018
        luego con el valor de compute(2017) cuando n es 2017 hallo h=2005 y luego para saber el resultado calculo compute(2005)
        el resultado es 1551.
  */
}


