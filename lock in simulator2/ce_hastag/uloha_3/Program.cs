using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace uloha_3 { 

    class numReader
    {
        public static int readNumber(){

            int znak = Console.Read();
            bool minus = false;

            while (znak < '0' || znak > '9') {
                if (znak == '-')
                {
                    minus = true;
                }
                znak = Console.Read();
                
            }

            int x = 0;
            while (znak >= '0' &&  znak <= '9')
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
            var a = numReader.readNumber();
            var b = numReader.readNumber();

            if (b == 0)
            {
                Console.WriteLine("NELZE");
            }
            else
            {
                int output = a / b;
                Console.WriteLine(output);
            }

                

            
        }
    }
}