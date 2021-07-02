from colorama import Fore, Style
import os, sys, argparse, json, time, subprocess, re
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from tqdm import tqdm

with open(r"speed.json", "w") as f:
    f.write("")

# dar clear a consola
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


primos = 0
compostos = 0
lower = 1
upper = 100_000
graph = False
table = False
enum = 2
pro = ""

# cli parser
parser = argparse.ArgumentParser(description='Digite dois numeros para calcular os numeros primos e compostos entre eles' )
parser.add_argument("--custom", help="digite 2 valoros custom", type=int, nargs = 2)
parser.add_argument("--graph", help="Se quer graficos usando os parsers json", action="store_true")
parser.add_argument("--table", help="Se quer tabela usando os parsers json", action="store_true")
parser.add_argument("--pro", help="Este modo é o conjunto de '--graph' com '--table'", action="store_true")
args = parser.parse_args()
if args.custom:
    if sys.argv[1] == "--graph" or sys.argv[1] == "--table" or sys.argv[1] == "--pro":
        enum += 1
    lower = int(sys.argv[enum])
    upper = int(sys.argv[enum + 1])
    
if args.graph: graph = True; pro = "--pro"
if args.table: table = True; pro = "--pro"
if args.pro: table = True; graph = True; pro = "--pro"




def main():
    start = ""
    while start not in ["start", "Start", "START", "sTART"]:

        start = input(f"Digite {Fore.RED}'start'{Fore.RESET} para começar o teste de velocidade ou {Fore.RED}'info'{Fore.RESET} para mais informações sobre este teste! ")
    
        if start == "info":
            print(f"Neste teste estão a ser usadas 4 linguas({Fore.MAGENTA}python{Fore.RESET}, {Fore.GREEN}c#{Fore.RESET}, {Fore.BLUE}c++{Fore.RESET} e {Fore.YELLOW}java{Fore.RESET}) e estou a comapar a velocidade de cada uma delas calcualndo numeros primos e compostos.\nPodes usar a flag '--custom <inicio> <fim>' para por numeros quaisquer.\nTabem podes usar as flags '--table' para a tabela, '--graph' para o grafico e '--pro' para tudo.")

    inicio = time.time()
    print(f"Linguas e ordem!\n\t\t>{Fore.MAGENTA}Python{Fore.RESET}\n\t\t>{Fore.GREEN}C#{Fore.RESET}\n\t\t>{Fore.BLUE}C++{Fore.RESET}\n\t\t>{Fore.YELLOW}Java{Fore.RESET}\n{Fore.RED}{Style.BRIGHT}COMEÇANDO!!!{Style.RESET_ALL}{Fore.RESET}")

    

    def num_primos():


        for num in tqdm(range(lower, upper + 1), ascii=True, desc=F"{Fore.MAGENTA}Python{Fore.RESET}"):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        global compostos
                        compostos += 1
                        break
                else:
                    global primos
                    primos += 1

    #python
    começo = time.time()
    
    print(f"-------------------------------- {Fore.MAGENTA}Python{Fore.RESET} --------------------------------".center(os.get_terminal_size().columns))
    num_primos()
    elapsedTime = time.time() - começo 
    print(f"{Fore.MAGENTA}Python{Fore.RESET} demorou:{Fore.RED}{time.time() - começo: .4}{Fore.RESET}{Style.BRIGHT} segundos{Style.RESET_ALL} a calcular os numeros {Style.BRIGHT}primos{Style.RESET_ALL} e {Style.BRIGHT}compostos{Style.RESET_ALL} entre {Fore.RED}{lower}{Fore.RESET} e {Fore.RED}{upper}{Fore.RESET} que no total são: {Fore.RED}{primos}{Fore.RESET} e {Fore.RED}{compostos}{Fore.RESET}.")

    #c#
    print(f"---------------------------------- {Fore.GREEN}C#{Fore.RESET} ----------------------------------".center(os.get_terminal_size().columns))
    os.system(f'powershell /c "dotnet run -- {pro}"') if not args.custom else os.system(f'powershell /c "dotnet run -- --inicio {sys.argv[enum]} --fim {sys.argv[enum + 1]} {pro}"')

    #c++ 
    print("")
    print(f"--------------------------------- {Fore.BLUE}C++{Fore.RESET} ---------------------------------".center(os.get_terminal_size().columns))
    if not args.custom:

        os.system('powershell /c "if ($?) { g++ main.cpp -o main } ; if ($?) { .\main }"') 
    else:
        
        cpp = f"--inicio {sys.argv[enum]} --fim {sys.argv[enum + 1]}"
        os.system('powershell /c "if ($?) { g++ main.cpp -o main } ; if ($?) { .\main %s "' % pro + cpp +  '"}"' ) 

    #java
    print("")
    print(f"--------------------------------- {Fore.YELLOW}Java{Fore.RESET} --------------------------------".center(os.get_terminal_size().columns))
    if not args.custom:
        os.system('powershell /c "if ($?) { javac main.java } ; if ($?) { java main }"')
    else:
        java = f"--inicio {sys.argv[enum]} --fim {sys.argv[enum + 1]}"
        os.system('powershell /c "if ($?) { javac main.java } ; if ($?) { java main %s "' % pro  + java +  '"}"' ) 
    print(f"--------------------------------- {Fore.CYAN}Fim{Fore.RESET} ---------------------------------".center(os.get_terminal_size().columns))

    

    
    if graph and table:
        with open(r"speed.json") as f:
            speed = json.load(f)

        with open(r"speed.json", "w") as f:
            speed["Python"] = str(round(elapsedTime, 2))
            json.dump(speed, f)

        total = float(speed["Python"]) + float(speed["Cs"]) + float(speed["Cpp"]) + float(speed["Java"])

        # tabela = PrettyTable([f"{Fore.MAGENTA}Python{Fore.RESET}", f"{Fore.GREEN}C#{Fore.RESET}", f"{Fore.BLUE}C++{Fore.RESET}", f"{Fore.YELLOW}Java{Fore.RESET}"])
        print("\n")
        tabela = PrettyTable([f"{Fore.CYAN}Linguas{Fore.RESET}", "Tempo(segundos)", "Compilador/Interpretador"])

        tabela.add_row([f"{Fore.MAGENTA}Python{Fore.RESET}", round(float(speed["Python"]), 2), "Python - 3.9.5"])
        tabela.add_row([f"{Fore.GREEN}C#{Fore.RESET}", round(float(speed["Cs"]), 2), "DotNet - 5.0.301"])
        tabela.add_row([f"{Fore.BLUE}C++{Fore.RESET}", round(float(speed["Cpp"]), 2), "G++ - 6.3.0"])
        tabela.add_row([f"{Fore.YELLOW}Java{Fore.RESET}", round(float(speed["Java"]), 2), "JDK - 16"])
        tabela.add_row([f"{Fore.CYAN}Total(4){Fore.RESET}", round(total, 2), "######"])


        print(tabela)


        
        
        labels = ["Python", "C#", "C++", "Java"]
        valor = [float(speed["Python"]), float(speed["Cs"]), float(speed["Cpp"]), float(speed["Java"])]
        plt.bar(labels, valor)
        plt.xlabel("Linguas")
        plt.ylabel("Tempo em segundos")
        plt.title("Grafico da velocidade das linguas")
        plt.show()


        print("\n--------------------------------")
        print(f"No total {Style.BRIGHT}todos{Style.RESET_ALL} os testes  demoraram {Fore.RED}{round(total, 4)}{Fore.RESET} segundos.")



        with open(r"speed.json", "w") as f:
            f.write("")


        dir = subprocess.run(["dir"], shell=True, text=True)  # doesn't capture output
        # print(f"O COISO EH {dir.stdout}")


        # process = subprocess.Popen(["cloc D:\speed\main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        # out, err = process.communicate()
        # # out = re.findall(int, out)
        # # print([int(s) for s in out.split() if s.isdigit()])
        # print(out)



    else:
        total = False

    print("--------------------------------")
    total_time = round(time.time() - inicio, 4)
    print(f"No {Style.BRIGHT}total{Style.RESET_ALL} este programa demorou {Fore.RED}{total_time}{Fore.RESET} segundos e o tempo {Style.BRIGHT}perdido{Style.RESET_ALL} foi {Fore.RED}{total_time - total}{Fore.RESET} segundos.") if total else print(f"No {Style.BRIGHT}total{Style.RESET_ALL} este programa demorou {Fore.RED}{total_time}{Fore.RESET} segundos.")
    print("--------------------------------")











try:
    clear()
    main()
except KeyboardInterrupt:
    print(Fore.LIGHTMAGENTA_EX + "\nBye..." + Fore.RESET)
    with open(r"speed.json", "w") as f:
        f.write("")
    exit()

################################################################ REFACTOR CODE


## maybe skip the json part with subprocess

#melhor o help menu nos cli parser


#user yaml or xml

#escolher uma lingua ou dar valores para linguas diferentes

# adicionar creditos e coiso para ver quantas linha isto tem
### talvez por a informaçao sobre o pc


## adicionar csx e fs e fsx provavelmente com rosyln


### por o parser do cli mais bonito e facil de enntender

##### progress bar em c# ter que por a posiçao (ver)
#progress bar
#custom numbers
#graficos
#tabelas
#dar mais info tipo compiladores/interpretador usados