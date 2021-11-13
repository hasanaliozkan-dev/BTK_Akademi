using System;

namespace SeventhLessonInheritancePolymorphsim
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Animal whiskers = new Animal()
            {
                Name = "whiskers",
                Sound = "meow"
            };

            Dog grover = new Dog()
            {
                Name = "grover",
                Sound = "woof",
                sound2 = "grrr"
            };

            grover.Sound = "Wooooooffff";

            whiskers.MakeSound();
            grover.MakeSound();

            whiskers.setAnimalIDInfo(12345, "ali");
            whiskers.getAnimalIDInfo();


            Animal.AnimalHealth getHealth = new Animal.AnimalHealth();

            Console.WriteLine("is my animal healthy {0}", getHealth.HealhyWeight(11, 46));

            Animal monkey = new Animal("happy", "heeee");
            Animal spot = new Dog("spot", "woof", "grrrr");

            monkey.MakeSound();
            spot.MakeSound();

        }
    }
}
