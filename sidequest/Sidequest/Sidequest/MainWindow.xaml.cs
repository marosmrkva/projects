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

namespace Sidequest
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        public ObservableCollection<Quest> listQuests { get; set; }

        public bool isAnimating = false;
        public bool canResize = false;

        private double _anchorRight;
        private double _anchorBottom;

        public static bool isMouseInside = false;

        public static string SaveFile = @"quests_savefile.txt";

        public MainWindow()
        {
            InitializeComponent();

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

            if (!File.Exists(SaveFile))
            {
                File.Create(SaveFile).Dispose();
            }
            else
            {
                using (StreamReader sr = File.OpenText(SaveFile))
                {
                    string line = "";
                    while ((line = sr.ReadLine()) != null)
                    {
                        if (string.IsNullOrWhiteSpace(line)) continue;

                        string[] loadQuest = line.Split('|');

                        if (loadQuest.Length >= 3)
                        {
                            Quest loadedQuest = new Quest();

                            loadedQuest.QuestName = loadQuest[0];
                            loadedQuest.deadline = Convert.ToDateTime(loadQuest[1]);
                            loadedQuest.QuestContents = loadQuest[2];

                            listQuests.Add(loadedQuest);
                        }
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
            newQuest.deadline = newQuestDeadline;
            newQuest.QuestContents = newQuestContent;
            listQuests.Add(newQuest);

            NewQuestEntryTextBox.Text = "";
            NewQuestContentTextBox.Text = "";

            NewQuestEntry.Visibility = Visibility.Collapsed;

            string lineToSave = $"{newQuestName}|{newQuestDeadline}|{newQuestContent}";

            File.AppendAllText(SaveFile, lineToSave + Environment.NewLine);


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
        
        private void Button_Exit(object sender, RoutedEventArgs e)
        {
            Environment.Exit(0);
        }
    }
}