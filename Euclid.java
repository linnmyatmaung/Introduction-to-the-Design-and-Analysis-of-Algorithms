import java.util.Scanner;
public class Euclid{
   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      System.out.println("Enter 2 integers to find gcd");
      int n = sc.nextInt();
      int m = sc.nextInt();
      if(n>m){
        int temp = n;
        n = m ;
        m = temp;
      }
       System.out.println("The two numbers are "+ m + " and " + n);
      while (n!=0){
        int r = m%n;
        m = n;
        n = r;
     }
      System.out.println("GCD is " + m);
      sc.close();
}
}
