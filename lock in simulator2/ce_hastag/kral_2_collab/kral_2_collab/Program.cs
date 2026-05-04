using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int pocetPrekazek = int.Parse(Console.ReadLine());

        // vytvoříme šachovnici 8x8, hodnoty jsou typu bool (true = překážka, false = volné pole)
        bool[,] prekazky = new bool[8, 8];

        for (int i = 0; i < pocetPrekazek; i++)
        {
            string[] vstupPrekazky = Console.ReadLine().Split();
            int x = int.Parse(vstupPrekazky[0]) - 1;
            int y = int.Parse(vstupPrekazky[1]) - 1;
            prekazky[x, y] = true;
        }

        string[] startVstup = Console.ReadLine().Split();
        int startX = int.Parse(startVstup[0]) - 1;
        int startY = int.Parse(startVstup[1]) - 1;

        string[] cilVstup = Console.ReadLine().Split();
        int cilX = int.Parse(cilVstup[0]) - 1;
        int cilY = int.Parse(cilVstup[1]) - 1;

        NajdiNejkratsiCestu(startX, startY, cilX, cilY, prekazky);
        //Console.WriteLine(vysledek);
    }

    static void NajdiNejkratsiCestu(int startX, int startY, int cilX, int cilY, bool[,] prekazky)
    {
        if (prekazky[startX, startY] || prekazky[cilX, cilY])
        {
            Console.WriteLine(-1);
            return;
        }

        bool[,] navstiveno = new bool[8, 8];

        int[] dx = { 1, -1, 0, 0, 1, 1, -1, -1 };
        int[] dy = { 0, 0, 1, -1, 1, -1, 1, -1 };

        Queue<(int[], List<(int, int)>)> fronta = new Queue<(int[], List<(int, int)>)>();

        List<(int, int)> path = new List<(int, int)>();
        path.Add((startX, startY));

        fronta.Enqueue((new int[] { startX, startY }, path));
        navstiveno[startX, startY] = true;

        while (fronta.Count > 0)
        {
            (int[] pole, List<(int, int)> thisPath) = fronta.Dequeue();
            int x = pole[0];
            int y = pole[1];

            if (x == cilX && y == cilY)
            {
                foreach ((int finalX, int finalY) in thisPath)
                {
                    Console.WriteLine((finalX + 1) + " " + (finalY + 1));
                }
                return;
            }

            for (int i = 0; i < 8; i++)
            {
                int novyX = x + dx[i];
                int novyY = y + dy[i];

                if (novyX >= 0 && novyX < 8 && novyY >= 0 && novyY < 8)
                {
                    if (!prekazky[novyX, novyY] && !navstiveno[novyX, novyY])
                    {
                        List<(int, int)> newPath = new List<(int, int)>(thisPath);
                        newPath.Add((novyX, novyY));

                        navstiveno[novyX, novyY] = true;
                        fronta.Enqueue((new int[] { novyX, novyY }, newPath));
                    }
                }
            }
        }

        Console.WriteLine(-1);
    }
}