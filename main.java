import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;
import java.io.FileNotFoundException;
public class main {

    
  public static void main(String[] args) {
    
    int num, lower = 1, upper = 100000, ctr, i, primos = 0, compostos = 0, primeiro = 0, fim = 2;
    Boolean pro = false;
    //cli parser
    if(args.length > 0){



        for(int k = 0; k < args.length; k++){
            if(args[k].equals("--pro")){ pro = true; }

            if(args[k].equals("--inicio")){
                lower = Integer.parseInt(args[k + 1]);
            }
            if(args[k].equals("--fim")){
                upper = Integer.parseInt(args[k + 1]);
            }
        }













        // if(args[primeiro].equals("--pro")){
        //     pro = true;
        //     primeiro++;
        //     fim++;
        // }
        // try{
        //         if(args[fim + 2].equals("--pro")){
        //             pro = true;
        //         }

        //     if(args[primeiro].equals("--inicio") && args[fim].equals("--fim")){
        //         lower = Integer.parseInt(args[primeiro + 1]);
        //         upper = Integer.parseInt(args[fim + 1]);
        //     }
        //     else if (args[primeiro].equals("-h") || args[fim].equals("--help")){
        //         System.out.println("Digite dois numeros\n\t>--inicio\n\t>--fim");
        //     }
        // } catch( ArrayIndexOutOfBoundsException e){
        //     // System.out.println("COMIA TE TODO");
        // }
    }
    long nanosegundos = System.nanoTime();

    for(num = lower; num <= upper; num++){
        ctr = 0;

        for(i = 2;i <= num / 2;i++){
            if(num % i == 0){
                ctr++;
                compostos++;
                break;
            }
       }
       
        if(ctr == 0 && num != 1){
           primos++;
       }
    }
    long millisegundos = (System.nanoTime() - nanosegundos) / 1000000;
    System.out.printf("\033[0;33mJava\u001B[0m demorou \u001B[31m" + millisegundos / 1000.0 + "\u001B[0m \033[0;36msegundos\033[0m a calcular os numeros \033[0;36mprimos\033[0m e \033[0;36mcomposots\033[0m entre \u001B[31m%d\u001B[0m e \u001B[31m%d\u001B[0m que no total são: \u001B[31m%d\u001B[0m e \u001B[31m%d\u001B[0m.\n", lower, upper, primos, compostos);
    if(pro == true){
        final String ficheiro = "speed.json";
        try{
            File obj = new File(ficheiro);
            Scanner reader = new Scanner(obj);
            String linha = reader.nextLine();
            
            reader.close();
            try{
                FileWriter writer = new FileWriter(ficheiro);
                writer.write(linha + ", \"Java\": \"" + millisegundos / 1000.0 + "\"}");
                writer.close();
            } catch (IOException e){
                System.out.println("Ocurreu um erro...");
                e.printStackTrace();
            }
    
    
        } catch(FileNotFoundException e){
            System.out.println("Ocurreu um erro...");
            e.printStackTrace();
        }
    }


    }
}
