using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Index;

namespace vykazy_cas_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string riadok = Console.ReadLine();

            while (riadok != ".")
            {
                string[] obsah_riadku = riadok.Split();

                if (obsah_riadku[0] == obsah_riadku[^1])
                {

                }


                riadok = Console.ReadLine();
            }

        }
    }
}
