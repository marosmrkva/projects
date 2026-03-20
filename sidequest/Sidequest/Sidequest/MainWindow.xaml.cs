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

namespace Sidequest
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public bool isAnimating = false;
        public bool canResize = false;

        private double _anchorRight;
        private double _anchorBottom;

        public MainWindow()
        {
            InitializeComponent();

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

        }

        private void Window_Expand(object sender, MouseEventArgs e)
        {
            if (this.Width > 290 && this.Height > 290) return;
            animateWindow(300);
        }

        private void Window_Collapse(object sender, MouseEventArgs e)
        {
            if (this.Width < 50 && this.Height < 50) return;
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