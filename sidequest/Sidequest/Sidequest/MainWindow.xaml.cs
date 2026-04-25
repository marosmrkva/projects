using System.Runtime.CompilerServices;
using System.Text;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Collections.ObjectModel;
using System.Runtime;
using System.Security.Cryptography.X509Certificates;
using System.IO;

using Microsoft.Data.Sqlite;
using Microsoft.Win32;

namespace Sidequest
{
    public partial class MainWindow : Window
    {
        private string dbPath;

        public ObservableCollection<Quest> listQuests { get; set; }

        public bool isAnimating = false;
        public bool canResize = false;

        private double _anchorRight;
        private double _anchorBottom;

        public static bool isMouseInside = false;

        public static string SaveFile = @"quests_savefile.txt";

        private void SetStartup(bool enable)
        {
            string runKey = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Run";
            string appName = "Sidequest";

            string exePath = Environment.ProcessPath;

            using (RegistryKey key = Registry.CurrentUser.OpenSubKey(runKey, true))
            {
                if (enable)
                {
                    key.SetValue(appName, $"\"{exePath}\"");
                }
                else
                {
                    key.DeleteValue(appName, false);
                }
            }
        }

        private void InitializeDatabase()
        {
            using (var connection = new SqliteConnection(dbPath))
            {
                connection.Open();

                var command = connection.CreateCommand();

                command.CommandText = @"
                    CREATE TABLE IF NOT EXISTS Quests (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        QuestName TEXT NOT NULL,
                        Deadline TEXT,
                        Content TEXT
                    )";

                command.ExecuteNonQuery();
            }
        }

        private void LoadQuestsFromDatabase()
        {
            listQuests.Clear();

            using (var connection = new SqliteConnection(dbPath))
            {
                connection.Open();

                var command = connection.CreateCommand();

                command.CommandText = "SELECT Id, QuestName, Deadline, Content FROM Quests";

                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Quest loadedQuest = new Quest();

                        loadedQuest.ID = reader.GetInt32(0);
                        loadedQuest.QuestName = reader.GetString(1);
                        string deadlineString = reader.GetString(2);
                        loadedQuest.Deadline = Convert.ToDateTime(deadlineString);
                        loadedQuest.QuestContents = reader.GetString(3);

                        listQuests.Add(loadedQuest);
                    }
                }
            }
        }

        

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            NewQuestEntry.Visibility = Visibility.Visible;

        }

        
        private void SaveNewQuest(object sender, RoutedEventArgs e)
        {
            
            string newQuestName = NewQuestEntryTextBox.Text;
            DateTime newQuestDeadline = Convert.ToDateTime(NewQuestDeadlineDate.Text);
            string newQuestContent = NewQuestContentTextBox.Text;

            if (string.IsNullOrWhiteSpace(newQuestName)) return;

            Quest newQuest = new Quest();
            newQuest.QuestName = newQuestName;
            newQuest.Deadline = newQuestDeadline;
            newQuest.QuestContents = newQuestContent;
            listQuests.Add(newQuest);

            using (var connection = new SqliteConnection(dbPath))
            {
                connection.Open();

                var command = connection.CreateCommand();

                command.CommandText = "INSERT INTO Quests (QuestName, Deadline, Content) VALUES (@name, @date, @content)";

                command.Parameters.AddWithValue("@name", newQuestName);
                command.Parameters.AddWithValue("@date", newQuestDeadline.ToString("s"));
                command.Parameters.AddWithValue("@content", newQuestContent);

                command.ExecuteNonQuery();
            }

            NewQuestEntryTextBox.Text = "";
            NewQuestContentTextBox.Text = "";

            NewQuestEntry.Visibility = Visibility.Collapsed;

        }

        private void Window_Expand(object sender, MouseEventArgs e)
        {
            isMouseInside = true;
            
            animateWindow(300);
            
        }

        private async void Window_Collapse(object sender, MouseEventArgs e)
        {
            isMouseInside = false;
            await Task.Delay(500);

            if (isMouseInside) return;

            
            animateWindow(40);
            

        }


        private void animateProperty(DependencyProperty prop, double targetSize)
        {
            DoubleAnimation sizeAnim = new DoubleAnimation()
            {
                To = targetSize,
                Duration = TimeSpan.FromMilliseconds(200),
                EasingFunction = new CubicEase { EasingMode = EasingMode.EaseOut}
            };
            this.BeginAnimation(prop, sizeAnim, HandoffBehavior.Compose);
        }

        private async Task animateWindow(double targetSize)
        {
            if (canResize && targetSize == 40)
            {
                await Task.Delay(5000);
                canResize = false;
                MainGrid.Visibility = Visibility.Collapsed;
            }

            

            canResize = true;

            animateProperty(Window.WidthProperty, targetSize);
            animateProperty(Window.HeightProperty, targetSize);

            animateProperty(Window.LeftProperty, _anchorRight - targetSize);
            animateProperty(Window.TopProperty, _anchorBottom - targetSize);

            if (canResize && targetSize == 300) MainGrid.Visibility = Visibility.Visible;

            Thread.Sleep(250);
        }
        
        private void RemoveQuest(object sender, RoutedEventArgs e)
        {
            Button pressedButton = sender as Button;
            Quest QuestToRemove = pressedButton.DataContext as Quest;

            if (QuestToRemove == null) return;

            using (var connection = new SqliteConnection(dbPath))
            {
                connection.Open();

                var command = connection.CreateCommand();

                command.CommandText = "DELETE FROM Quests WHERE Id = @id";
                command.Parameters.AddWithValue("@id", QuestToRemove.ID);

                command.ExecuteNonQuery();
            }
            listQuests.Remove(QuestToRemove);
        }
        


        private void Button_Exit(object sender, RoutedEventArgs e)
        {
            Environment.Exit(0);
        }

        public MainWindow()
        {
            InitializeComponent();

            try
            {
                string appFolder = AppDomain.CurrentDomain.BaseDirectory;
                string fullDbPath = System.IO.Path.Combine(appFolder, "quests.db");

                dbPath = $"Data Source={fullDbPath}";

                listQuests = new ObservableCollection<Quest>();
                this.DataContext = this;

                var desktopWorkingArea = SystemParameters.WorkArea;

                this.Width = 40;
                this.Height = 40;

                _anchorRight = desktopWorkingArea.Right - 20;
                _anchorBottom = desktopWorkingArea.Bottom - 20;

                this.Left = _anchorRight - this.Width;
                this.Top = _anchorBottom - this.Height;

                MainGrid.Visibility = Visibility.Collapsed;

                InitializeDatabase();
                LoadQuestsFromDatabase();

                SetStartup(true);
            }
            catch (Exception ex)
            {
                string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
                string logFile = System.IO.Path.Combine(desktopPath, "SidequestError.txt");
                System.IO.File.WriteAllText(logFile, "CHYBA PRI ŠTARTE:\n" + ex.ToString());
            }
        }
    }
}