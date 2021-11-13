using System;

namespace ThirdLessonDerekBanas
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            //ternary operator
            //int age = 17;

            //bool canDrive = age >= 18 ? true : false; // we dont have to do like that we can do like bool canDrive = age >= 1;  

            //Console.Write(canDrive);
            int age = 1;
            //Switch statement
            /*switch (age)
            {
                case 1:
                case 2:
                    Console.WriteLine("Go to day care");
                    break;
                case 3:
                case 4:
                    Console.WriteLine("Go to pre-school");
                    break;
                case 5:
                case 6:
                    Console.WriteLine("Go to kindergarten");
                    break;
                default:
                    Console.WriteLine("Go to another school");
                    goto OtherSchool;

            }

        OtherSchool:
            Console.WriteLine("hello there is no other school");

            string name1 = "ali";
            string name2 = "ali";

            Console.WriteLine(name1.Equals(name2,StringComparison.Ordinal));
            */

            /*int i = 0;
            while (i < 10)
            {
                if(i%2 == 0)
                {
                    i++;
                    continue;
                }
                if(i == 9) break;
                {
                    Console.WriteLine(i);
                    i++; 
                }

            }*/

            Random rnd = new Random();
            int secretNumber = rnd.Next(1, 11);
            int numberGuessed = 0;
            do
            {
                Console.WriteLine("guess a number:");
                numberGuessed = Convert.ToInt32(Console.ReadLine());
            } while (secretNumber != numberGuessed);





        }
    }
}
