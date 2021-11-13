using System;

namespace FifthLessonCSharp
{
    class Deneme
    {
        public string name;
        public string sound;

        int numOfAnimals;

        public Deneme()
        {
            name = "noname";
            sound = "nosound";
            numOfAnimals++;
        }
        public Deneme( string name = "noname" , string sound = "nosound")
        {
            this.name = name;
            this.sound = sound;
            numOfAnimals++;
        }

        public void MakeSound()
        {
            Console.WriteLine("{0} says {1}", name, sound);
        }

        public int GetNumAnimals()
        {
            return numOfAnimals; 
        }
    }
}