using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace photoshop
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pero = new Pen(Color.Black, 1);
            pero.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            pero.EndCap = System.Drawing.Drawing2D.LineCap.Round;

            bmp = new Bitmap(1000, 1000);
            g = Graphics.FromImage(bmp);

            pictureBox2.Image = bmp;
        }

        Pen pero;
        Bitmap bmp;
        Graphics g;

        int minx = 0;
        int miny = 0;

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Bitmap paletka = (Bitmap)pictureBox1.Image;

            pero.Color = paletka.GetPixel(e.X, e.Y);
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            pero.Width = trackBar1.Value;
        }

        private void vymažToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Refresh();
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {

            if (e.Button == MouseButtons.Left)
            {
                g.DrawLine(pero, minx, miny, e.X, e.Y);
                Refresh();
            }

            minx = e.X;
            miny = e.Y;
        }

        private void uložiťToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                bmp.Save(saveFileDialog1.FileName);
        }
    }
}
