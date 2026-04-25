using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace test_vs2026
{
    class Prvocinitel
    {
        public static string prvocinitel(int cislo, int delitel)
        {
            if (cislo == 1)
                return "";
            while (cislo % delitel != 0)
            {
                delitel++;
            }
            if (cislo % delitel == 0)
            {
                int vysledek = cislo / delitel;
                string pamatuj = prvocinitel(vysledek, delitel);
                return delitel + "*" + pamatuj;
            }
            return cislo.ToString();
        }
    }

    internal class Program
    {
        
        static void Main(string[] args)
        {
            int vstup = Convert.ToInt32(Console.ReadLine());
            string vystup = Prvocinitel.prvocinitel(vstup, 2);
            Console.WriteLine(vstup + "=" + vystup.Remove(vystup.Length-1));
        }
    }
}
