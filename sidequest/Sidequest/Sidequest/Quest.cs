using System;
using System.Collections.Generic;
using System.Text;


namespace Sidequest
{
    public class Quest
    {
        public string QuestName { get; set; }
        public string QuestContents { get; set; }
        public bool isCompleted = false;
        public DateTime deadline { get; set; }

    }
}
