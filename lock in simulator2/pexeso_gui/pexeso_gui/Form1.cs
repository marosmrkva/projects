using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Text;
using System.Linq;
using System.Net.NetworkInformation;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pexeso_gui
{
    public partial class Form1 : Form
    {

        public static int turnsCount = 0;
        public static int cardsTurnedLastTime = 0;
        public List<int> turnedCards = new List<int> { };
        public List<int> remainingCards = new List<int> { };
        public Button lastCard;
        public Button b;
        Random random = new Random();
        public static int pairs = 0;

        public Form1()
        {
            InitializeComponent();
            NastavStav(STAV.START);
        }

        enum STAV
        {
            START,
            HRA,
            JEDEN,
            DVA,
            VYHRA
        }
        STAV stav;

        void NastavStav(STAV novyStav)
        {
            switch (novyStav)
            {
                case STAV.START:
                    turnsCount = 0;
                    turnedCards = new List<int> { };
                    remainingCards = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 };
                    pairs = 0;
                    lastCard = null;
                    b = null;
                    LNazov.Visible = true;
                    LPravidla.Visible = true;
                    LPocetTahov.Visible = false;
                    LVysledok.Visible = false;
                    BStart.Visible = true;
                    BExit.Visible = true;
                    BDalsiaHra.Visible = false;
                    break;
                case STAV.HRA:
                    LPocetTahov.Text = Convert.ToString(turnsCount);
                    remainingCards = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 };
                    if (stav == STAV.START || stav == STAV.VYHRA)
                    {
                        VytvorKarticky();
                    }
                    remainingCards = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 };
                    LNazov.Visible = false;
                    LPravidla.Visible = false;
                    LPocetTahov.Visible = true;
                    LVysledok.Visible = false;
                    BStart.Visible = false;
                    BExit.Visible = true;
                    BDalsiaHra.Visible = false;
                    break;
                case STAV.JEDEN:
                    if (pairs == 18)
                    {
                        NastavStav(STAV.VYHRA);
                    }
                    break;
                case STAV.DVA:
                    LPocetTahov.Text = Convert.ToString(turnsCount);
                    LPravidla.Visible = false;
                    LPocetTahov.Visible = true;
                    LVysledok.Visible = false;
                    BStart.Visible = false;
                    BExit.Visible = true;
                    BDalsiaHra.Visible = false;
                    break;
                case STAV.VYHRA:
                    LPravidla.Visible = false;
                    LPocetTahov.Visible = true;
                    LVysledok.Visible = true;
                    BStart.Visible = false;
                    BExit.Visible = true;
                    BDalsiaHra.Visible = true;
                    LPocetTahov.Location = new Point(454, 196);
                    LPocetTahov.Font = new Font("Elephant", 50, FontStyle.Bold);
                    break;
                default:
                    break;
            }
            stav = novyStav;
        }

        private void BStart_Click(object sender, EventArgs e)
        {
            NastavStav(STAV.HRA);
        }

        void VytvorKarticky()
        {
            int N = 6;
            int HORNY_OKRAJ = 100;
            int sx = ClientRectangle.Width / N;
            int sy = (ClientRectangle.Height - HORNY_OKRAJ) / N;

            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    Button b = new Button();
                    b.Width = sx;
                    b.Height = sy;
                    b.Left = i * sx;
                    b.Top = j * sy + HORNY_OKRAJ;
                    b.Text = "PEXESO";
                    b.BackColor = Color.DarkRed;

                    b.Parent = this;

                    int valueIndex = random.Next(remainingCards.Count);

                    b.Tag = remainingCards[valueIndex];
                    remainingCards.Remove(remainingCards[valueIndex]);
                    b.Click += KLIK;
                }
            }
        }

        async void KLIK(object sender, EventArgs e)
        {

            b = (Button)sender;

            b.BackColor = Color.DarkOrange;

            if (b == lastCard) return;

            b.Text = b.Tag.ToString();
            
            b.Refresh();

            if (lastCard != null)
            {
                turnsCount++;
                LPocetTahov.Text = Convert.ToString(turnsCount);
                b.Refresh();
            }

            cardsTurnedLastTime++;
            turnedCards.Add(Convert.ToInt32(b.Tag.ToString()));

            if (turnedCards.Count() == 2)
            {

                Console.WriteLine(pairs);
                
                if (turnedCards[0] == turnedCards[1])
                {
                    pairs++;
                    remainingCards.Remove(turnedCards[0]);

                    Thread.Sleep(500);

                    b.Visible = false;
                    lastCard.Visible = false;
                    turnedCards.Clear();

                    lastCard = null;
                }
                else
                {
                    Thread.Sleep(500);
                    b.Text = "PEXESO";
                    lastCard.Text = "PEXESO";
                    b.BackColor = Color.DarkRed;
                    lastCard.BackColor = Color.DarkRed;
                    turnedCards.Clear();
                    lastCard = null;
                    
                    
                }
                NastavStav(STAV.JEDEN);
            }
            else
            {
                NastavStav(STAV.DVA);
                lastCard = b;
            }
        }

        private void BExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void BDalsiaHra_Click(object sender, EventArgs e)
        {
            NastavStav(STAV.START);
        }
    }
}
