using System;

namespace FourthLessonMethods
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            /*double x = 5;
            double y = 4;
            Console.WriteLine(GetSum(x, y));
            Console.WriteLine(x);

            int num1 = 10;
            int num2 = 20;
            Console.WriteLine("before {0},{1} " , num1, num2);


            Swap(ref num1, ref num2);

            Console.WriteLine("after {0},{1} ", num1, num2);
            

            Console.WriteLine(GetSumMore(1, 2, 3,4,5,6,7,8,9,0,65,5.43,4.325,3.54));*/
            PrintInfo(23445, "hasan ali");

        }

        private static void PrintInfo(int zipCode, string name)
        {
            Console.WriteLine("{0} live in {1}", name, zipCode);
        }

        /*private static double GetSumMore(params double[] nums)
        {
            double sum = 0;
            foreach(int i in nums)
            {
                sum += i;
            }
            return sum;
        }

        private static void Swap(ref int num1, ref int num2)
        {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }

        static double GetSum(double x = 1 , double y = 1)
        {
            double temp = x;
            x = y;
            y = temp;
            return x + y;
        }*/

    }
}
