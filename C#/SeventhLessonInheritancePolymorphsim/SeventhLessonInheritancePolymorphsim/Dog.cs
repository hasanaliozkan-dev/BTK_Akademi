using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SeventhLessonInheritancePolymorphsim
{
    class Dog : Animal
    {

        public string sound2 { set; get; } = "grrrr";

        public override void MakeSound()
        {
            Console.WriteLine($"{Name} says {Sound} and {sound2} ");
        }

        public Dog(string name = "noname" , string sound = "nosound",string soundtwo = "nosound")
            :base(name,sound)
        {
            sound2 = soundtwo;
        } 


    }
}