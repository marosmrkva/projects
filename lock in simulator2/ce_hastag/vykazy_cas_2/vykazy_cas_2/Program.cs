using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vykazy_cas_2
{
    internal class Program
    {


        static void Main(string[] args)
        {
            int sekundy = 0;

            string riadok = Console.ReadLine();

            while (riadok != ".")
            {
                if (riadok == "") 
                { 
                    riadok = Console.ReadLine();
                    continue;
                }

                string[] obsah_riadku = riadok.Split();

                if (obsah_riadku.Length < 3)
                {
                    riadok = Console.ReadLine();
                    continue;
                }

                if (obsah_riadku[0] == obsah_riadku[obsah_riadku.Length - 2])
                {
                    string[] cas = obsah_riadku[1].Split(':');

                    int[] cas1 = new int[3];
                    for (int i = 0; i < cas.Length; i++)
                    {
                        cas1[i] = Convert.ToInt32(cas[i]);
                    }

                    cas = obsah_riadku[obsah_riadku.Length - 1].Split(':');

                    int[] cas2 = new int[3];
                    for (int i = 0; i < cas.Length; i++)
                    {
                        cas2[i] = Convert.ToInt32(cas[i]);
                    }

                    int cas1_sec = cas1[0] * 3600 + cas1[1] * 60 + cas1[2];
                    int cas2_sec = cas2[0] * 3600 + cas2[1] * 60 + cas2[2];
                    
                    sekundy += (cas2_sec - cas1_sec);
                }

                riadok = Console.ReadLine();
            }

            int hodiny = sekundy / 3600;
            sekundy = sekundy % 3600;
            int minuty = sekundy / 60;
            sekundy = sekundy % 60;
            string sekundy_str = Convert.ToString(sekundy);

            if (sekundy < 10) sekundy_str = "0" + sekundy_str;

            Console.WriteLine("celkem: " + hodiny + ":" + minuty + ":" + sekundy_str);
        }
    }
}
