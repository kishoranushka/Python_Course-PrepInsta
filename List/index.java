import java.util.Scanner;

public class index{



public static void main(String[] args){
  int b,c;
  Scanner sc=new Scanner(System.in);
  System.out.println(x:"enter first no.: ");
  b=sc.nextInt();
  System.out.println(x:"enter second no.: ");
  c=sc.nextInt();

  int a[][]= new int[b][c];

  
  System.out.println("Enter the elements of the matrix: ");


  for(int i=0;i<b;i++)
  {
    for(int j=0;j<c;j++)
    {
      a[i][j]=sc.nextInt();
    }
  }
 // for printing the original matrix
 System.out.println("Original matrix:");

  for(int i=0;i<b;i++)
  {
    for(int j=0;j<c;j++)
    {
      System.out.print(a[i][j]+" ");
    }
    system.out.println();
  }

  int br[][]=new int[c][b];
  for(int i=0;i<c;i++)
  {
    for(int j=0;j<b;j++)
    {
      br[i][j]= a[j][i];
    }
  }


  // for printing the transpose matrix
  System.out.println("Transpose matrix:");

  for(int i=0;i<c;i++)
  {
    for(int j=0;j<b;j++)
    {
      System.out.print(br[i][j]+" ");
    }
    system.out.println();
  }

  sc.close();


}
}