using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace FirsCSharpLessonderekBanas
{
    class Program
    {
        public static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");

            //String answer = Console.ReadLine();
            //Console.WriteLine("answer is " + answer);

            //Console.WriteLine(args.Length);

            /*for (int i = 0; i < args.Length; i++)
            {   
                Console.WriteLine("Arg {0} : {1}", i, args[i]);
            }

            String[] myArgs = Environment.GetCommandLineArgs(); 

            Console.WriteLine(string.Join(", ", myArgs));
            SayHello();

            bool canIVote = true;

            Console.WriteLine("The biggest {0}", int.MaxValue); // 2147483647
            Console.WriteLine(" The smallest {0}", int.MinValue); //-2147483648
            Console.WriteLine("The biggest {0}", long.MaxValue); //9223372036854775807
            Console.WriteLine("The smallest {0}", long.MinValue); //-9223372036854775808
            Console.WriteLine("The biggest {0}", double.MaxValue.ToString("#"));//1.79769313486232E+308
            Console.WriteLine(" The smallest {0}" , double.MinValue.ToString("#")); //-1.79769313486232E+308
            Console.WriteLine("The biggest {0}", decimal.MaxValue); //79228162514264337593543950335
            

            //Convert data type
            bool boolFromStr = bool.Parse("true");
            int intFromStr = int.Parse("1234567890");
            double doubleFromStr = double.Parse("1.2345");

            DateTime awesomeDate = new DateTime(1919,05,19);
            Console.WriteLine(" Day of week {0} ", awesomeDate.DayOfWeek);

            awesomeDate = awesomeDate.AddDays(4);
            awesomeDate = awesomeDate.AddMonths(11);
            awesomeDate = awesomeDate.AddYears(0);
            Console.WriteLine("another avesome day {0} ", awesomeDate.Date);


            TimeSpan lunchTime = new TimeSpan(12, 30, 0);

            lunchTime = lunchTime.Subtract(new TimeSpan(0, 15, 0));
            lunchTime = lunchTime.Add(new TimeSpan(1, 45, 0));
            Console.WriteLine(lunchTime.ToString());


            Console.WriteLine("currency : {0:c}", 12.34545);
            Console.WriteLine("pad with 0's : {0:d4}", 12);
            Console.WriteLine("3 decimals: {0:f3}", 12.34545);
            Console.WriteLine("ccommas : {0:n4}", 1200);*/

            string randomString = "This is a string.";

            Console.WriteLine("String length {0}" , randomString.Length);
            Console.WriteLine(" string contains is {0}" , randomString.Contains("is"));
            Console.WriteLine("Index of is {0}", randomString.IndexOf("is"));
            Console.WriteLine("Remove string {0} " , randomString.Remove(0,6));
            Console.WriteLine("Insert string {0} " , randomString.Insert(10,"short "));
            Console.WriteLine("Replace {0} " , randomString.Replace("string","sentence"));
            Console.WriteLine("compare a to B {0} " , String.Compare("A","B", StringComparison.OrdinalIgnoreCase) );
            Console.WriteLine("Equals 'A' to 'a' {0}" , String.Equals("a","A"));
            Console.WriteLine(value: randomString.ToUpper());
        }

        public static void SayHello()
        {
            string name = "";
            Console.WriteLine("What is your name? : ");
            name = Console.ReadLine(); // get input
            Console.WriteLine("Hello {0}",name);
        }
    }

}
