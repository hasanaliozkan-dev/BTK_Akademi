using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SeventhLessonInheritancePolymorphsim
{
    class Animal
    {
        private string name;
        protected string sound;
        protected AnimalIDInfo AnimalIDInfo = new AnimalIDInfo();

        public void setAnimalIDInfo(int idnum,string owner)
        {
            AnimalIDInfo.IDNum = idnum;
            AnimalIDInfo.Owner = owner;
        }
        public void getAnimalIDInfo()
        {
            Console.WriteLine($"{name} has ıdnum {AnimalIDInfo.IDNum} and its owner {AnimalIDInfo.Owner}");
        }

        public virtual void MakeSound()
        {
            Console.WriteLine($"{Name} says {Sound}");
            //Console.WriteLine("{0} makes this sound  {1}", name, sound); 
        }
        public Animal()
            :this("noname", "nosound") { }

        public Animal(string name)
            : this(name, "nosound") { }

        public Animal(string name , string sound)
        {
            Name = name;
            Sound = sound;
        }

        public string Name
        {
            get { return name; }
            set {
                if (!value.Any(char.IsDigit))
                {
                    name = "noname";
                }
                name = value;
                }
        }
        public string Sound
        {
            get { return sound; }
            set
            {
                if (value.Length < 10 )
                {
                    sound = "nosound";
                }
                sound = value;
            }
        }

        public class AnimalHealth
        {
            public bool HealhyWeight(double height,double weight)
            {
                double calc = height / weight;
                if ((calc < .18) && (calc > .25))
                {
                    return true;
                }else return false;
                
            }
        }
    }
}