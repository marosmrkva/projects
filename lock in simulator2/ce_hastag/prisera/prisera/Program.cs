using Microsoft.Win32.SafeHandles;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prisera
{
    class Monster
    {
        static int[] monsterPos = new int[2];
        static bool wasLastMoveRight = false;

        public static void readMap()
        {
            int mapWidth = int.Parse(Console.ReadLine());
            int mapHeight = int.Parse(Console.ReadLine());

            char[,] map = new char[mapHeight, mapWidth];

            for (int i = 0; i < mapHeight; i++)
            {
                string mapRow = Console.ReadLine();

                for (int j = 0; j < mapWidth; j++)
                {
                    map[i, j] = mapRow[j];

                    if (mapRow[j] == '>' || mapRow[j] == '<' || mapRow[j] == 'v' || mapRow[j] == '^') 
                    {
                        monsterPos[0] = i;
                        monsterPos[1] = j; 
                    }
                }
            }

            move(map);
        }

        private static void printMap(char[,] mapToPrint)
        {
            int mapHeight = mapToPrint.GetLength(0);
            int mapWidth = mapToPrint.GetLength(1);

            for (int i = 0; i < mapHeight; i++)
            {
                for (int j = 0; j < mapWidth; j++)
                {
                    Console.Write(mapToPrint[i, j]);
                }
                Console.Write("\n");
            }
            Console.WriteLine();
        }

        private static void move(char[,] getMap)
        {
            for (int i = 0; i < 20; i++) 
            {
                //did we turn last move
                if (!wasLastMoveRight) //no
                {
                    wasLastMoveRight = false; //reset

                    //check surroundings
                    switch (getMap[monsterPos[0], monsterPos[1]])
                    {
                        case '>':
                            if (getMap[monsterPos[0] + 1, monsterPos[1]] == 'X') //wall on the right
                            {
                                if (getMap[monsterPos[0], monsterPos[1] + 1] == 'X') //wall in front
                                {
                                    getMap[monsterPos[0], monsterPos[1]] = '^';
                                }
                                else //no wall in front
                                {
                                    getMap[monsterPos[0], monsterPos[1] + 1] = '>';
                                    getMap[monsterPos[0], monsterPos[1]] = '.';
                                    monsterPos[1] += 1;
                                }
                            }
                            else //right clear
                            {
                                getMap[monsterPos[0], monsterPos[1]] = 'v';
                                wasLastMoveRight = true;
                            }
                            break;
                        case '^':
                            if (getMap[monsterPos[0], monsterPos[1] + 1] == 'X')
                            {
                                if (getMap[monsterPos[0] - 1, monsterPos[1]] == 'X')
                                {
                                    getMap[monsterPos[0], monsterPos[1]] = '<';
                                }
                                else //no wall in front
                                {
                                    getMap[monsterPos[0] - 1, monsterPos[1]] = '^';
                                    getMap[monsterPos[0], monsterPos[1]] = '.';
                                    monsterPos[0] -= 1;
                                }
                            }
                            else //right clear
                            {
                                getMap[monsterPos[0], monsterPos[1]] = '>';
                                wasLastMoveRight = true;
                            }
                            break;
                        case '<':
                            if (getMap[monsterPos[0] - 1, monsterPos[1]] == 'X')
                            {
                                if (getMap[monsterPos[0], monsterPos[1] - 1] == 'X')
                                {
                                    getMap[monsterPos[0], monsterPos[1]] = 'v';
                                }
                                else //no wall in front
                                {
                                    getMap[monsterPos[0], monsterPos[1] - 1] = '<';
                                    getMap[monsterPos[0], monsterPos[1]] = '.';
                                    monsterPos[1] -= 1;
                                }
                            }
                            else //right clear
                            {
                                getMap[monsterPos[0], monsterPos[1]] = '^';
                                wasLastMoveRight = true;
                            }
                            break;
                        case 'v':
                            if (getMap[monsterPos[0], monsterPos[1] - 1] == 'X')
                            {
                                if (getMap[monsterPos[0] + 1, monsterPos[1]] == 'X')
                                {
                                    getMap[monsterPos[0], monsterPos[1]] = '>';
                                }
                                else //no wall in front
                                {
                                    getMap[monsterPos[0] + 1, monsterPos[1]] = 'v';
                                    getMap[monsterPos[0], monsterPos[1]] = '.';
                                    monsterPos[0] += 1;
                                }
                            }
                            else //right clear
                            {
                                getMap[monsterPos[0], monsterPos[1]] = '<';
                                wasLastMoveRight = true;
                            }
                            break;

                    }
                }
                else //yes 
                {
                    wasLastMoveRight = false;
                    //move one step
                    switch (getMap[monsterPos[0], monsterPos[1]])
                    {
                        case '>':
                            getMap[monsterPos[0], monsterPos[1] + 1] = '>';
                            getMap[monsterPos[0], monsterPos[1]] = '.';
                            monsterPos[1] += 1;
                            break;
                        case '^':
                            getMap[monsterPos[0] - 1, monsterPos[1]] = '^';
                            getMap[monsterPos[0], monsterPos[1]] = '.';
                            monsterPos[0] -= 1;
                            break;
                        case '<':
                            getMap[monsterPos[0], monsterPos[1] - 1] = '<';
                            getMap[monsterPos[0], monsterPos[1]] = '.';
                            monsterPos[1] -= 1;
                            break;
                        case 'v':
                            getMap[monsterPos[0] + 1, monsterPos[1]] = 'v';
                            getMap[monsterPos[0], monsterPos[1]] = '.';
                            monsterPos[0] += 1;
                            break;
                    }
                }
                printMap(getMap);
            }
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Monster.readMap();
        }
    }
}
