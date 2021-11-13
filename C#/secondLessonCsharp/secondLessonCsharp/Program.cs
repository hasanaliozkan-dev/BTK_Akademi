using System;
using System.Linq;
using System.Collections.Generic;

using System.Text;
using System.Threading.Tasks;

using System.Globalization;


namespace secondLessonCsharp
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            /*var a = 1234;
            Console.WriteLine(a.GetType());
            int[] favNums = new int[3];
            favNums[0] = 1;

            Console.WriteLine(favNums[0]);

            string[] ali = { "a", "l", "i" };
            Console.WriteLine("{0}{1}{2}", ali[0], ali[1], ali[2]);

            var ali1 = new[] { "a", "l", "i" };

            object[] randomArray = { "ali", 1234, 1.234 };

            string[,] customNames = new string[2, 2] { { "ali", "hasan" }, { "büşra", "erturan" } };

            Console.WriteLine("The name of my mean {0}",customNames.GetValue(1, 0));

            int[] randomArr = { 1, 5, 2, 6, 3, 4};
            Array.Sort(randomArr);
            Array.Reverse(randomArr);
            Array.Resize(ref randomArr,8);
            randomArr[6] = 7;
            randomArr[7] = 8;

            PrintArray(randomArr, "ForEach");

            int[] numArray = { 1, 11, 22 };

            Console.WriteLine("{0}", Array.FindAll(numArray, GT10));
            Console.WriteLine("{0}", Array.FindIndex(numArray, GT10));
            Console.WriteLine("{0}", Array.FindLastIndex( numArray, GT10));
            Console.WriteLine("{0}", Array.Find(numArray, GT10));
            */

            //String Builder

            StringBuilder sb = new StringBuilder("Random Text");

            StringBuilder sb1 = new StringBuilder("more stuf these are important", 56);

            Console.WriteLine(sb.Capacity);
            Console.WriteLine(sb1.Capacity);
            sb1.Replace("are", "ali");
            Console.WriteLine(sb1);

            Console.WriteLine(sb.Equals(sb1));
            long num1 = 12345;
            int num2 = (int)num1;

            int a = 1245543;
            long b = a;
            Console.WriteLine(b);

            
        }

        /*private static bool GT10(int obj)
        {
            return obj > 10;
        }

        static void PrintArray(int[] intArr, string message)
        {
             foreach( int k in intArr)
            {
                Console.WriteLine("{0} : {1}",message, k);
            }
        }*/
    }
}
