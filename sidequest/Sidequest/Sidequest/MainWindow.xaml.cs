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
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            NewQuestEntry.Visibility = Visibility.Visible;

            
        }


        private void SaveNewQuest(object sender, RoutedEventArgs e)
        {
            string newQuestName = NewQuestEntryTextBox.Text;

            if (string.IsNullOrWhiteSpace(newQuestName)) return;

            Quest newQuest = new Quest();
            newQuest.QuestName = newQuestName;
            listQuests.Add(newQuest);

            NewQuestEntryTextBox.Text = "";

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

        private void isMouseInApp(object sender, MouseEventArgs e)
        {
            isMouseInside = !isMouseInside;
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
            }

            canResize = true;

            animateProperty(Window.WidthProperty, targetSize);
            animateProperty(Window.HeightProperty, targetSize);

            animateProperty(Window.LeftProperty, _anchorRight - targetSize);
            animateProperty(Window.TopProperty, _anchorBottom - targetSize);

            Thread.Sleep(250);
        }
        
    }
}