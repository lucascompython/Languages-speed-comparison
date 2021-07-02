using System;
using CommandLine;
using System.Text.Json;
using System.IO;
using Yaap;
using System.Linq;
using System.Threading;
using static Yaap.YaapConsole;


namespace main {

    

    //progress bar/*
    /*
public class ProgressBar : IDisposable, IProgress<double> {
	private const int blockCount = 10;
	private readonly TimeSpan animationInterval = TimeSpan.FromSeconds(1.0 / 8);
	private const string animation = @"|/-\";

	private readonly Timer timer;

	private double currentProgress = 0;
	private string currentText = string.Empty;
	private bool disposed = false;
	private int animationIndex = 0;

	public ProgressBar() {
		timer = new Timer(TimerHandler);

		// A progress bar is only for temporary display in a console window.
		// If the console output is redirected to a file, draw nothing.
		// Otherwise, we'll end up with a lot of garbage in the target file.
		if (!Console.IsOutputRedirected) {
			ResetTimer();
		}
	}

	public void Report(double value) {
		// Make sure value is in [0..1] range
		value = Math.Max(0, Math.Min(1, value));
		Interlocked.Exchange(ref currentProgress, value);
	}

	private void TimerHandler(object state) {
		lock (timer) {
			if (disposed) return;

			int progressBlockCount = (int) (currentProgress * blockCount);
			int percent = (int) (currentProgress * 100);
			string text = string.Format("[{0}{1}] {2,3}% {3}",
				new string('#', progressBlockCount), new string('-', blockCount - progressBlockCount),
				percent,
				animation[animationIndex++ % animation.Length]);
			UpdateText(text);

			ResetTimer();
		}
	}

	private void UpdateText(string text) {
		// Get length of common portion
		int commonPrefixLength = 0;
		int commonLength = Math.Min(currentText.Length, text.Length);
		while (commonPrefixLength < commonLength && text[commonPrefixLength] == currentText[commonPrefixLength]) {
			commonPrefixLength++;
		}

		// Backtrack to the first differing character
		StringBuilder outputBuilder = new StringBuilder();
		outputBuilder.Append('\b', currentText.Length - commonPrefixLength);

		// Output new suffix
		outputBuilder.Append(text.Substring(commonPrefixLength));

		// If the new text is shorter than the old one: delete overlapping characters
		int overlapCount = currentText.Length - text.Length;
		if (overlapCount > 0) {
			outputBuilder.Append(' ', overlapCount);
			outputBuilder.Append('\b', overlapCount);
		}

		Console.Write(outputBuilder);
		currentText = text;
	}

	private void ResetTimer() {
		timer.Change(animationInterval, TimeSpan.FromMilliseconds(-1));
	}

	public void Dispose() {
		lock (timer) {
			disposed = true;
			UpdateText(string.Empty);
		}
	}

}


*/

    public class data{
        public string Cs{get; set;}
    }

    class Programm{
        protected static int origCol = 0;
        static int min, max;
        static bool pro;
        public class Options
        {
            [Option("inicio", Default = 0, Required = false, HelpText = "Digite o inicio")]
            public int inicio { get; set; }
            [Option("fim", Required = false, Default = 0, HelpText = "Digite o fim")]
            public int fim { get; set; }
            [Option("pro", Required = false, Default= false, HelpText = "Se quer dar 'parse' a informação para json (nao recomendado se nao usar o programa em python)")]
            public bool pro { get; set; }
            
        }
        
        static void Main(string[] args){
            Parser.Default.ParseArguments<Options>(args)
                   .WithParsed<Options>(o =>
                   {
                       
                       min = o.inicio;
                       max = o.fim;
                       pro = o.pro;

                   });
    




            


            System.Diagnostics.Stopwatch stopwatch = new System.Diagnostics.Stopwatch();
            stopwatch.Start();
            int lower, upper, ctr, i, primos = 0, compostos = 0;
            if(min <= 0 || max <= 0){
                min = 1; max = 100_000;
            }
            lower = min;
            upper = max;

            // for(var f = 0; f < 10; f++){
            //     Console.WriteLine("yah");
            // }

            // foreach(var k in Enumerable.Range(0, 10).Yaap()){
            //     Thread.Sleep(10);
            //     Console.WriteLine("drena");
            // }



            foreach(var num in Enumerable.Range(lower, upper).Yaap(description : "\x1B[32mC# \x1B[0m")){
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

            // for(num = lower; num <= upper; num++){
            //         ctr = 0;

            //         for(i = 2;i <= num / 2;i++){
            //             if(num % i == 0){
            //                 ctr++;
            //                 compostos++;
            //                 break;
            //             }
            //         }
                    
            //         if(ctr == 0 && num != 1){
            //             primos++;
            //         }
            // } 
            
            stopwatch.Stop();
            System.TimeSpan ts = stopwatch.Elapsed;
            string elapsedTime = System.String.Format("{0:00}.{1:00}",
                ts.Seconds,
                ts.Milliseconds / 10);
            //mostrar as drenas
            Console.ForegroundColor = System.ConsoleColor.Green; Console.SetCursorPosition(origCol + 0, Console.CursorTop); Console.Write("C# "); Console.ResetColor(); 
            Console.Write("demorou ");
            Console.ForegroundColor = System.ConsoleColor.Red; Console.Write(elapsedTime); Console.ResetColor(); 
            Console.ForegroundColor = System.ConsoleColor.Cyan; Console.Write(" segundos"); Console.ResetColor(); 
            Console.Write(" a calcular os numeros ");
            Console.ForegroundColor = System.ConsoleColor.Cyan; Console.Write("primos"); Console.ResetColor(); 
            Console.Write(" e ");
            Console.ForegroundColor = System.ConsoleColor.Cyan; Console.Write("compostos"); Console.ResetColor(); 
            Console.Write(" entre ");
            Console.ForegroundColor = System.ConsoleColor.Red; Console.Write(lower); Console.ResetColor(); 
            Console.Write(" e ");
            Console.ForegroundColor = System.ConsoleColor.Red; Console.Write(upper); Console.ResetColor(); 
            Console.Write(" que no total são: ");
            Console.ForegroundColor = System.ConsoleColor.Red; Console.Write(primos); Console.ResetColor(); 
            Console.Write(" e ");
            Console.ForegroundColor = System.ConsoleColor.Red; Console.Write(compostos); Console.ResetColor(); 
            Console.Write(".");
            if(pro == true){
                var Data = new data
                {
                    Cs = $"{elapsedTime}",
                };

                
                string json = JsonSerializer.Serialize(Data);
                File.AppendAllText("speed.json", json);
            }

        }
    }
}