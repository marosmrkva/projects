using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace rozklad_na_prvocisla
{
    class rozklad
    {
        public static string rozklad_na_prvocisla(int num, int div) {
            if (num == 1)
            {
                return null;
            }

            while (num%div != 0)
            {
                div++;
            }

            if (num%div == 0)
            {
                int zvysok = num / div;
                string vystup = rozklad_na_prvocisla(zvysok, div);
                if (vystup == "1")
                {
                    return div.ToString();
                }
                return div + "*" + vystup;
            }

            return num.ToString();
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {

            int inputNumber = Convert.ToInt32(Console.ReadLine());

            string vysledok = rozklad.rozklad_na_prvocisla(inputNumber, 2);

            Console.WriteLine(inputNumber + "=" + vysledok.Remove(vysledok.Length-1));


        }
    }
}
