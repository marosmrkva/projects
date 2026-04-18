namespace abeceda;

class Program
{
    public static int getTotalClicks()
    {
        int tableWidth = Console.Read();
        int tableHeight = Console.Read();
        
        char[,] table = new char[tableWidth, tableHeight];

        for (int i = 0; i < tableWidth; i++)
        {
            for (int j = 0; j < tableHeight; j++)
            {
                table[i, j] = Console.ReadKey().KeyChar;
            }
        }
        
        string inputString = Console.ReadLine();
        
        char currentChar = inputString[0];
        
        
        
        
        
        
        return 0;
    }
    
    static void Main(string[] args)
    {
        Console.WriteLine(getTotalClicks());
    }
}