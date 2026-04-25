using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sklad
{
    internal class Program
    {
        static bool isSpaceFree(int x, int y, char[,] map)
        {
            return map[y, x] == '.';
        }

        static int Skladnik()
        {
            //array velkosti 12 kvoli okraju z X aby skladnik nevysiel von, je to jednoduchsie ako kontrolovat indexy mimo mapu
            char[,] roomMap = new char[12, 12];

            for (int i = 0; i < 12; i++)
            {
                //nastavime vsetky policka na okraji na barieru X
                roomMap[0, i] = 'X';
                roomMap[11, i] = 'X';
                roomMap[i, 0] = 'X';
                roomMap[i, 11] = 'X';
            }

            int[] start = new int[2];
            int[] end = new int[2];
            int[] box = new int[2];

            for (int i = 1; i <= 10; i++)
            {
                string line = Console.ReadLine();
                while (string.IsNullOrEmpty(line))
                {
                    //preskakujeme prazdne a neviditelne znaky
                    line = Console.ReadLine();
                }

                for (int j = 1; j <= 10; j++)
                {
                    //prejdeme kazdy znak vstupu a urcime jeho hodnotu v mape
                    char position = j - 1 < line.Length ? line[j - 1] : '.';

                    switch (position)
                    {
                        case '.':
                            roomMap[i, j] = '.';
                            break;
                        case 'X':
                            roomMap[i, j] = 'X';
                            break;
                        case 'C':
                            roomMap[i, j] = '.';
                            end[0] = j;
                            end[1] = i;
                            break;
                        case 'S':
                            roomMap[i, j] = '.';
                            start[0] = j;
                            start[1] = i;
                            break;
                        case 'B':
                            roomMap[i, j] = '.';
                            box[0] = j;
                            box[1] = i;
                            break;
                        default:
                            roomMap[i, j] = '.';
                            break;
                    }
                }
            }

            /*
            vytvorime si frontu pre BFS
            pridame do nej zaciatocnu poziciu

            vytvorime si aj array s moznymi tahmi skladnika

            vytvorime si este 4D array navstivenych pozicii, kde prve dve suradnice su poloha skladnika, druhe dve su poloha bedne
            rovnako ako do fronty donho 
            */

            
            Queue<(int, int, int, int, int)> movesQueue = new Queue<(int, int, int, int, int)>();

            movesQueue.Enqueue((start[0], start[1], box[0], box[1], 0));

            (int, int)[] moves = new (int, int)[] { (0, 1), (1, 0), (0, -1), (-1, 0) };

            bool[,,,] visited = new bool[12, 12, 12, 12];
            visited[start[0], start[1], box[0], box[1]] = true;

            while (movesQueue.Count > 0)
            {
                //spustime BFS, prehladavame pozicie skladnika a bedne zaroven

                (int currX, int currY, int boxX, int boxY, int currentMovesCount) = movesQueue.Dequeue();

                if ((boxX, boxY) == (end[0], end[1]))
                {
                    //ak mame bednu v cieli, koncime a funkcia vracia pocet tahov

                    return currentMovesCount;
                }

                foreach ((int moveX, int moveY) in moves)
                {
                    //prejdeme vsetky mozne kroky skladnika

                    int newX = currX + moveX;
                    int newY = currY + moveY;

                    //ak je nove miesto volne, ideme dalej
                    if (!isSpaceFree(newX, newY, roomMap)) continue;
                                      
                    if (newX == boxX && newY == boxY)
                    {
                        //ak skladnik vliezol do bedne, zmenime poziciu bedne rovnako ako skladnika

                        int newBoxX = boxX + moveX;
                        int newBoxY = boxY + moveY;

                        //ak bedna nevliezla do steny, ideme dalej
                        if (!isSpaceFree(newBoxX, newBoxY, roomMap)) continue;

                        if (!visited[newX, newY, newBoxX, newBoxY])
                        {
                            //ak skladnik a bedna este neboli v tejto pozicii, pridame do fronty

                            visited[newX, newY, newBoxX, newBoxY] = true;
                            movesQueue.Enqueue((newX, newY, newBoxX, newBoxY, currentMovesCount + 1));
                        }
                    }
                    else
                    {
                        if (!visited[newX, newY, boxX, boxY])
                        {
                            //ak skladnik a bedna este neboli v tejto pozicii, pridame do fronty

                            visited[newX, newY, boxX, boxY] = true;
                            movesQueue.Enqueue((newX, newY, boxX, boxY, currentMovesCount + 1));
                        }
                    }


                }
            }

            //ak prejdeme vsetko a nemame ciel, funkcia vrati -1
            return -1;
        }

        static void Main(string[] args)
        {
            Console.WriteLine(Skladnik());
        }
    }
}
