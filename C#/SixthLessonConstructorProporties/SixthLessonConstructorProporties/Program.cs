using System;
using System.Linq;

namespace SixthLessonConstructorProporties
{
    class MainClass
    {

        private string Private = "This is a private field";

        protected string Protected = "This is a protected field";
        
        public const string Constaant = "This is a constant field"; 


        public static void Main(string[] args)
        {
                   
        }



        /* another type of constructor for animal class

        public Animal()
        :this("noname","nosound") { }*/


        // a setter and getter example
        private string name;
        private string sound;

        public void SetName(string name)
        {
            if (!name.Any(Char.IsDigit))
            {
                this.name = name;
            }
            else
            {
                this.name = "noname";
                Console.WriteLine("the name can't contain numbers!!");
            }
        }

        public string GetName()
        {
            return name;
        }


        public string Sound
        {
            get { return sound; }
            set
            {

                if(value.Length > 10)
                {
                    sound = "nosound";
                    Console.WriteLine("sound length have to be less than ten!!");
                }
                else
                {
                    sound = value;
                }
            }
        }


    }
}
