using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sklad
{
    internal class Program
    {
        static int Skladnik()
        {
            char[,] mapa_skladu = new string[10, 10];

            int[] start;
            int[] ciel;

            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    char policko = Console.Read();

                    switch (policko)
                    {
                        case ".":
                            mapa_skladu[j, i] = ".";
                            break;
                        case "X":
                            mapa_skladu[j, i] = "X";
                            break;
                        case "C":
                            mapa_skladu[j, i] = ".";
                            break;
                        case "S":
                            mapa_skladu[j, i] = ".";
                            break;
                        case "B":
                            mapa_skladu[j, i] = ".";
                            break;
                    }
                }
            }
            
            return 0;
        }

        static void Main(string[] args)
        {
        }
    }
}
