using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cviko3
{
    class numReader
    {
        public static int readNumber()
        {

            int znak = Console.Read();
            bool minus = false;

            while (znak < '0' || znak > '9')
            {
                if (znak == '-')
                {
                    minus = true;
                }
                znak = Console.Read();
            }

            int x = 0;
            while (znak >= '0' && znak <= '9')
            {
                x = 10 * x + znak - '0';
                znak = Console.Read();
            }

            if (minus == true)
            {
                return -x;
            }
            else
            {
                return x;
            }

        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] numbersArr = new int[1000];
            var number = 0;
            int currentIndex = 0;

            while (number != -1)
            {
                if (number == -1)
                {
                    break;
                }

                number = numReader.readNumber();
                numbersArr[currentIndex] = number;
                currentIndex++;
            }

            for (int i = currentIndex-2; i >= 0; i--)
            {
                Console.Write(numbersArr[i] + " ");
            }
        }
    }
}
