using System;

namespace FifthLessonCSharp
{
    class MainClass
    {

        public static void Main(string[] args)
        {
            // we dont use constructor
            Rectangle rect1;
            rect1.length = 15;
            rect1.width = 23;
            Console.WriteLine(rect1.Area());
            // we use constructor

            Rectangle rect2 = new Rectangle(20, 75);

            Console.WriteLine(rect2.Area());

            Deneme deneme1 = new Deneme("wolf", "aauuu");

            deneme1.MakeSound();
            Console.WriteLine(deneme1.GetNumAnimals());

            Console.WriteLine(ShapeMath.GetArea("rectangle", 4, 6));

            // nullable if we pass question mark like that int? it can be a null otherwise not

            int? nullable = null;
            //int nullable2 = null;

            if (nullable == null)
            {
                Console.WriteLine("the number is null!!!");
            }

            if (!nullable.HasValue)
            {
                Console.WriteLine("the number is null");
            }

        }
        // structure

        struct Rectangle
        {
            public double length;
            public double width;

            //contructor method

            public Rectangle(double l = 1, double w = 1)
            {
                length = l;
                width = w;
            }

            public double Area()
            {
                return length * width;
            }
        }




    }
}
