using System;

namespace FifthLessonCSharp
{
    public static class ShapeMath
    {
        public static double GetArea(string name = "", double length = 1, double width = 1)
        {
            if(String.Equals("Rectangle",name,StringComparison.OrdinalIgnoreCase))
            {
                return length * width;
            }
            else if (String.Equals("Triangle", name, StringComparison.OrdinalIgnoreCase))
            {
                return length * width  /  2;
            }
            else
            {
                return 0;
            }

            
        }
    }
}