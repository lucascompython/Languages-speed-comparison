#include <iostream>
#include <chrono>
#include <locale.h> 
#include <string.h>
#include <sstream>
#include <fstream>
#include <cstring>
// #include "./include/tqdm.h"
using namespace std;





int main(int argc, char** argv){
    setlocale(LC_ALL, "Portuguese");



    int num, lower = 1, upper = 100000, ctr, i, primos = 0, compostos = 0, primeiro = 1, fim = 3, drena = 0;
    bool pro = false;
    char opcoes[8][9] = {"--pro", "-p", "--inicio", "-i", "--fim", "-f", "--help", "-h"};
    stringstream ss, sss;
    //cli parser
    if(argc > 1){

        for(int l = 1; l < argc; l++){
            if(strcmp(argv[l], opcoes[0]) == 0 || strcmp(argv[l], opcoes[1]) == 0){ pro = true; drena++; }

            if(strcmp(argv[l], opcoes[2]) == 0 || strcmp(argv[l], opcoes[3]) == 0){
                ss << argv[l + 1];
                ss >> lower;
                drena++;
            }

            if(strcmp(argv[l], opcoes[4]) == 0 || strcmp(argv[l], opcoes[5]) == 0){
                sss << argv[l + 1];
                sss >> upper;
                drena++;
            }



            if(strcmp(argv[l], opcoes[6]) == 0 || strcmp(argv[l], opcoes[7]) == 0){
                cout << "Use a flag '--pro' ou '-p' para guardar a informação do teste em json(apenas recomando uso quando utilizado o ficheiro principal em python)\nA flags '--inicio' ou '-i' e '--fim' ou '-f' servem para por uma valor(inteiro) asseguir á flag para defenir o inicio e o fim do teste.";
                exit(0);
            }

            if(drena < 1){
                cout << "\x1B[31mComando não encontrado\x1B[0m!!\nUse a flag '--pro' ou '-p' para guardar a informação do teste em json(apenas recomando uso quando utilizado o ficheiro principal em python)\nA flags '--inicio' ou '-i' e '--fim' ou '-f' servem para por uma valor(inteiro) asseguir á flag para defenir o inicio e o fim do teste.";
                exit(0);
            }
            
        }

        



        // if(strcmp(argv[primeiro], "--pro") == 0){
        //     cout << "PRO TA A DAR";
        //     pro = true;
        //     primeiro++;
        //     fim++;
        // }
        // else if (strcmp(argv[fim + 2], "--pro") == 0){ pro = true; cout << "PRO TA A DAR"; }

        // else if (strcmp(argv[1], "--inicio") == 0){
        //     cout << "drena";
        // }
        

        // if (strcmp(argv[primeiro], "--pro") == 0){ pro = true; } 

        // else if(strcmp(argv[primeiro], "--inicio") == 0 && strcmp(argv[fim], "--fim") == 0 && argc < 5){
            
        //     ss << argv[primeiro + 1];
        //     ss >> lower;
        //     // lower = atoi(argv[2]);
        //     // cout << lower << "dasdasda";
        //     sss << argv[fim + 1];
        //     sss >> upper;
        //     // upper = atoi(argv[4]);
        // }
        // else if(strcmp(argv[1], "-h") == 0 || strcmp(argv[3], "--help") == 0){
        //     cout << "Digite dois numeros\n\t" << ">--inicio\n\t" << ">--fim"; 
        // }



        // else if(strcmp(argv[primeiro], "--pro") == 0 && strcmp(argv[primeiro + 1], "--inicio") == 0 && strcmp(argv[fim + 1], "--fim") == 0) {


        //     pro = true;
        //     ss << argv[primeiro + 2];
        //     ss >> lower;
        //     // lower = atoi(argv[2]);
        //     // cout << lower << "dasdasda";
        //     sss << argv[fim + 2];
        //     sss >> upper;
        //     // upper = atoi(argv[4]);
        //     }
        //     else if(strcmp(argv[1], "-h") == 0 || strcmp(argv[3], "--help") == 0){
        //         std::cout << "Digite dois numeros\n\t" << ">--inicio\n\t" << ">--fim"; 
        //     }

        // else if(strcmp(argv[primeiro], "--inicio") == 0 && strcmp(argv[fim], "--fim") == 0 && strcmp(argv[fim + 2], "--pro") == 0){

        //     pro = true;
        //     ss << argv[primeiro + 1];
        //     ss >> lower;
        //     // lower = atoi(argv[2]);
        //     // cout << lower << "dasdasda";
        //     sss << argv[fim + 1];
        //     sss >> upper;
        //     // upper = atoi(argv[4]);
        //     }
        //     else if(strcmp(argv[1], "-h") == 0 || strcmp(argv[3], "--help") == 0){
        //         std::cout << "Digite dois numeros\n\t" << ">--inicio\n\t" << ">--fim"; 
        //     }


        }




        


    



    auto t1 = std::chrono::high_resolution_clock::now();
    
    
    for(num = lower; num <= upper; num++){
         ctr = 0;

         for(i = 2; i <= num / 2; i++){
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
    auto t2 = std::chrono::high_resolution_clock::now();
    auto segundos = std::chrono::duration_cast<std::chrono::seconds>( t2 - t1 ).count();
    auto millisegundos = std::chrono::duration_cast<std::chrono::milliseconds>( t2 - t1 ).count();
    cout << "\x1B[94mC++\033[0m demorou " << "\x1B[31m" << segundos << "." << millisegundos << "\033[0m" << " \e[1msegundos\e[0m a calcular os numeros \e[1mprimos\e[0m e \e[1mcompostos\e[0m entre " <<  "\x1B[31m" << lower << "\033[0m" << " e " <<"\x1B[31m" << upper <<"\033[0m" << " que no total são: " << "\x1B[31m" <<primos << "\033[0m" << " e " << "\x1B[31m" << compostos << "\033[0m" << ".";
    

    if(pro == true){

        const char ficheiro[200] = "speed.json";
        string texto;
        ifstream ReadFile(ficheiro);
        while (getline (ReadFile, texto))
        
        cout << "";     // nao se sabe porque mas se tirar texto_char fica undefined
        char* texto_char;
        texto_char = &texto[0];
        




        
        FILE * fPointer;
        fPointer = fopen(ficheiro, "w+");
        fputs(texto_char , fPointer);
        fseek(fPointer, 13, SEEK_SET);
        fprintf(fPointer, ",\"Cpp\": \"");
        fprintf(fPointer, "%lld.%lld\"", segundos, millisegundos); //dividir por 100

        fclose(fPointer);
    }
    return 0;
}