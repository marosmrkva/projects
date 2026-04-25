using System;

namespace programko_2_prva_prednaska
{
    internal class Program
    {
        static void dosat7(ref int a)
        {
            Console.WriteLine(a);
            a = 7;
        }

        static int Main()
        {
            int x = 9;
            
            dosat7(ref x);
            Console.WriteLine(x);

            bool plati = true;

            Console.WriteLine(plati);

            return x;
        }
    }
}
