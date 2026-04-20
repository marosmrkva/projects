namespace abeceda;

class Program
{
    public static int getTotalClicks()
    {

        int tableWidth = int.Parse(Console.ReadLine());
        int tableHeight = int.Parse(Console.ReadLine());

        string inputTableString = Console.ReadLine();

        Dictionary<char, List<(int row, int column)>> charPosMap = new Dictionary<char, List<(int row, int column)>>();

        for (int i = 0; i < inputTableString.Length; i++)
        {
            char currentChar = inputTableString[i];

            int row = i / tableWidth;
            int column = i % tableWidth;

            if (!charPosMap.ContainsKey(currentChar))
            {
                charPosMap[currentChar] = new List<(int row, int column)>();
            }

            charPosMap[currentChar].Add((row, column));
        }

        string inputString = Console.ReadLine();

        Dictionary<(int row, int column), int> possibleCurrentPos = new Dictionary<(int row, int column), int>();
        possibleCurrentPos.Add((0, 0), 0);


        foreach (char currentChar in inputString)
        {
            if (!charPosMap.ContainsKey(currentChar))
            {
                continue;
            }

            Dictionary<(int row, int column), int> possibleNewPos = new Dictionary<(int row, int column), int>();

            foreach ((int newRow, int newColumn) in charPosMap[currentChar])
            {
                int lowestCostToCurentChar = int.MaxValue;

                foreach (var prevPos in possibleCurrentPos)
                {

                    (int prevRow, int prevColumn) = prevPos.Key;
                    int currentCost = prevPos.Value;

                    int newCost = currentCost + Math.Abs(newRow - prevRow) + Math.Abs(newColumn - prevColumn) + 1;

                    if (newCost < lowestCostToCurentChar)
                    {
                        lowestCostToCurentChar = newCost;
                    }
                }
                possibleNewPos.Add((newRow, newColumn), lowestCostToCurentChar);
            }

            possibleCurrentPos = possibleNewPos;
        }
        int minCost = int.MaxValue;
        
        foreach (var pos in possibleCurrentPos)
        {
            if (pos.Value < minCost)
            {
                minCost = pos.Value;
            }
        }
        return minCost;
    }
    
    static void Main(string[] args)
    {
        Console.WriteLine(getTotalClicks());
    }
}