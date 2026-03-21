using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Linq;

namespace simulace
{
    public enum TypUdalosti
    {
        Start,
        Trpelivost,
        Obslouzen
    }

    public class Udalost
    {
        public int kdy;
        public Proces kdo;
        public TypUdalosti co;
        public Udalost(int kdy, Proces kdo, TypUdalosti co)
        {
            this.kdy = kdy;
            this.kdo = kdo;
            this.co = co;

        }
    }
    public class Kalendar
    {
        private List<Udalost> seznam;
        public Kalendar()
        {
            seznam = new List<Udalost>();
        }
        public void Pridej(int kdy, Proces kdo, TypUdalosti co)
        {
            //Console.WriteLine("PLAN: {0} {1} {2}", kdy, kdo.ID, co);
            // pro hledani chyby:
            foreach (Udalost ud in seznam)
                if (ud.kdo == kdo)
                    Console.WriteLine("");


            seznam.Add(new Udalost(kdy, kdo, co));
        }
        public void Odeber(Proces kdo, TypUdalosti co)
        {
            foreach (Udalost ud in seznam)
            {
                if ((ud.kdo == kdo) && (ud.co == co))
                {
                    seznam.Remove(ud);
                    return; // odebiram jen jeden vyskyt!
                }
            }
        }
        public Udalost Prvni()
        {
            Udalost prvni = null;
            foreach (Udalost ud in seznam)
                if ((prvni == null) || (ud.kdy < prvni.kdy))
                    prvni = ud;
            seznam.Remove(prvni);
            return prvni;
        }
        public Udalost Vyber()
        {
            return Prvni();
        }

    }

    public abstract class Proces
    {
        public static char[] mezery = { ' ' };
        public int patro;
        public string ID;
        public abstract void Zpracuj(Udalost ud);
        public void log(string zprava)
        {
            //if (ID == "Dana")
            //if (ID == "elefant")
            //if (this is Zakaznik)
            //Console.WriteLine($"{model.Cas}/{patro} {ID}: {zprava}");
        }
        protected Model model;
    }

    public class Oddeleni : Proces
    {
        private int rychlost;
        private List<Zakaznik> fronta;
        private bool obsluhuje;

        public Oddeleni(Model model, string popis)
        {
            this.model = model;
            string[] popisy = popis.Split(Proces.mezery, StringSplitOptions.RemoveEmptyEntries);
            this.ID = popisy[0];
            this.patro = int.Parse(popisy[1]);
            if (this.patro > model.MaxPatro)
                model.MaxPatro = this.patro;
            this.rychlost = int.Parse(popisy[2]);
            obsluhuje = false;
            fronta = new List<Zakaznik>();
            model.VsechnaOddeleni.Add(this);
        }
        public void ZaradDoFronty(Zakaznik zak)
        {
            fronta.Add(zak);
            log("do fronty " + zak.ID);

            if (obsluhuje) ; // nic
            else
            {
                obsluhuje = true;
                model.Naplanuj(model.Cas, this, TypUdalosti.Start);
            }
        }
        public void VyradZFronty(Zakaznik koho)
        {
            fronta.Remove(koho);
        }

        public int ZjistiDelkuFronty()
        {
            return fronta.Count; //pomocná pro S2
        }
        public override void Zpracuj(Udalost ud)
        {
            switch (ud.co)
            {
                case TypUdalosti.Start:
                    if (fronta.Count == 0)
                        obsluhuje = false; // a dal neni naplanovana a probudi se tim, ze se nekdo zaradi do fronty
                    else
                    {
                        Zakaznik zak = fronta[0];
                        fronta.RemoveAt(0);
                        model.Odplanuj(zak, TypUdalosti.Trpelivost);
                        model.Naplanuj(model.Cas + rychlost, zak, TypUdalosti.Obslouzen);
                        model.Naplanuj(model.Cas + rychlost, this, TypUdalosti.Start);
                    }
                    break;
            }
        }
    }
    public enum SmeryJizdy
    {
        Nahoru,
        Dolu,
        Stoji
    }
    public class Vytah : Proces
    {
        private int kapacita;
        private int dobaNastupu;
        private int dobaVystupu;
        private int dobaPatro2Patro;
        static int[] ismery = { +1, -1, 0 }; // prevod (int) SmeryJizdy na smer

        private class Pasazer
        {
            public Proces kdo;
            public int kamJede;
            public Pasazer(Proces kdo, int kamJede)
            {
                this.kdo = kdo;
                this.kamJede = kamJede;
            }
        }

        private List<Pasazer>[,] cekatele; // [patro,smer]
        private List<Pasazer> naklad;   // pasazeri ve vytahu
        private SmeryJizdy smer;
        private int kdyJsemMenilSmer;

        public void PridejDoFronty(int odkud, int kam, Proces kdo)
        {
            Pasazer pas = new Pasazer(kdo, kam);
            if (kam > odkud)
                cekatele[odkud, (int)SmeryJizdy.Nahoru].Add(pas);
            else
                cekatele[odkud, (int)SmeryJizdy.Dolu].Add(pas);

            // pripadne rozjet stojici vytah:
            if (smer == SmeryJizdy.Stoji)
            {
                model.Odplanuj(model.vytah, TypUdalosti.Start); // kdyby nahodou uz byl naplanovany
                model.Naplanuj(model.Cas, this, TypUdalosti.Start);
            }
        }
        public bool CekaNekdoVPatrechVeSmeruJizdy()
        {
            int ismer = ismery[(int)smer];
            for (int pat = patro + ismer; (pat > 0) && (pat <= model.MaxPatro); pat += ismer)
                if ((cekatele[pat, (int)SmeryJizdy.Nahoru].Count > 0) || (cekatele[pat, (int)SmeryJizdy.Dolu].Count > 0))
                {
                    if (cekatele[pat, (int)SmeryJizdy.Nahoru].Count > 0)
                        //log("Nahoru čeká " + cekatele[pat, (int)SmeryJizdy.Nahoru][0].kdo.ID
                            //+ " v patře " + pat + "/" + cekatele[pat, (int)SmeryJizdy.Nahoru][0].kdo.patro);
                    if (cekatele[pat, (int)SmeryJizdy.Dolu].Count > 0)
                        //log("Dolů čeká " + cekatele[pat, (int)SmeryJizdy.Dolu][0].kdo.ID
                            //+ " v patře " + pat + "/" + cekatele[pat, (int)SmeryJizdy.Dolu][0].kdo.patro);

                    //log(" x "+cekatele[pat, (int)SmeryJizdy.Nahoru].Count+" x "+cekatele[pat, (int)SmeryJizdy.Dolu].Count);
                    return true;
                }
            return false;
        }

        public Vytah(Model model, string popis)
        {
            this.model = model;
            string[] popisy = popis.Split(Proces.mezery, StringSplitOptions.RemoveEmptyEntries);
            this.ID = popisy[0];
            this.kapacita = int.Parse(popisy[1]);
            this.dobaNastupu = int.Parse(popisy[2]);
            this.dobaVystupu = int.Parse(popisy[3]);
            this.dobaPatro2Patro = int.Parse(popisy[4]);
            this.patro = 0;
            this.smer = SmeryJizdy.Stoji;
            this.kdyJsemMenilSmer = -1;

            cekatele = new List<Pasazer>[model.MaxPatro + 1, 2];
            for (int i = 0; i < model.MaxPatro + 1; i++)
            {
                for (int j = 0; j < 2; j++)
                {
                    cekatele[i, j] = new List<Pasazer>();
                }

            }
            naklad = new List<Pasazer>();
        }
        public override void Zpracuj(Udalost ud)
        {
            switch (ud.co)
            {
                case TypUdalosti.Start:

                    // HACK pro cerstve probuzeny vytah:
                    if (smer == SmeryJizdy.Stoji)
                        // stoji, tedy nikoho neveze a nekdo ho prave probudil => nastavim jakykoliv smer a najde ho:
                        smer = SmeryJizdy.Nahoru;

                    // chce nekdo vystoupit?
                    foreach (Pasazer pas in naklad)
                        if (pas.kamJede == patro)
                        // bude vystupovat:
                        {
                            naklad.Remove(pas);

                            pas.kdo.patro = patro;
                            model.Naplanuj(model.Cas + dobaVystupu, pas.kdo, TypUdalosti.Start);
                            //log("vystupuje " + pas.kdo.ID);

                            model.Naplanuj(model.Cas + dobaVystupu, this, TypUdalosti.Start);

                            return; // to je pro tuhle chvili vsechno
                        }

                    // muze a chce nekdo nastoupit?
                    if (naklad.Count == kapacita)
                    // i kdyby chtel nekdo nastupovat, nemuze; veze lidi => pokracuje:
                    {
                        // popojet:
                        int ismer = ismery[(int)smer];
                        patro = patro + ismer;

                        string spas = "";
                        foreach (Pasazer pas in naklad)
                            spas += " " + pas.kdo.ID;
                        //log("odjíždím");
                        model.Naplanuj(model.Cas + dobaPatro2Patro, this, TypUdalosti.Start);
                        return; // to je pro tuhle chvili vsechno
                    }
                    else
                    // neni uplne plny
                    {
                        // chce nastoupit nekdo VE SMERU jizdy?
                        if (cekatele[patro, (int)smer].Count > 0)
                        {
                            //log("nastupuje " + cekatele[patro, (int)smer][0].kdo.ID);
                            naklad.Add(cekatele[patro, (int)smer][0]);
                            cekatele[patro, (int)smer].RemoveAt(0);
                            model.Naplanuj(model.Cas + dobaNastupu, this, TypUdalosti.Start);

                            return; // to je pro tuhle chvili vsechno
                        }

                        // ve smeru jizdy nikdo nenastupuje:
                        if (naklad.Count > 0)
                        // nikdo nenastupuje, vezu pasazery => pokracuju v jizde:
                        {
                            // popojet:
                            int ismer = ismery[(int)smer];
                            patro = patro + ismer;

                            string spas = "";
                            foreach (Pasazer pas in naklad)
                                spas += " " + pas.kdo.ID;
                            //log("nekoho vezu");
                            //log("odjíždím: " + spas);

                            model.Naplanuj(model.Cas + dobaPatro2Patro, this, TypUdalosti.Start);
                            return; // to je pro tuhle chvili vsechno
                        }

                        // vytah je prazdny, pokud v dalsich patrech ve smeru jizdy uz nikdo neceka, muze zmenit smer nebo se zastavit:
                        if (CekaNekdoVPatrechVeSmeruJizdy() == true)
                        // pokracuje v jizde:
                        {
                            // popojet:
                            int ismer = ismery[(int)smer];
                            patro = patro + ismer;

                            //log("nekdo ceka");
                            //log("odjíždím");
                            model.Naplanuj(model.Cas + dobaPatro2Patro, this, TypUdalosti.Start);
                            return; // to je pro tuhle chvili vsechno
                        }

                        // ve smeru jizdy uz nikdo neceka => zmenit smer nebo zastavit:
                        if (smer == SmeryJizdy.Nahoru)
                            smer = SmeryJizdy.Dolu;
                        else
                            smer = SmeryJizdy.Nahoru;

                        //log("změna směru");

                        //chce nekdo nastoupit prave tady?
                        if (kdyJsemMenilSmer != model.Cas)
                        {
                            kdyJsemMenilSmer = model.Cas;
                            // podivat se, jestli nekdo nechce nastoupit opacnym smerem:
                            model.Naplanuj(model.Cas, this, TypUdalosti.Start);
                            return;
                        }

                        // uz jsem jednou smer menil a zase nikdo nenastoupil a nechce => zastavit
                        //log("zastavuje");
                        smer = SmeryJizdy.Stoji;
                        return; // to je pro tuhle chvili vsechno
                    }
            }
        }
    }
    public class Zakaznik : Proces
    {
        public static int globalniPocitadlo = 1;
        public int P;
        // P je pořadové číslo zákazníka

        private int trpelivost;
        private int prichod;
        private List<string> Nakupy;
        public Zakaznik(Model model, string popis)
        {
            this.P = globalniPocitadlo;
            globalniPocitadlo++;
            // přiřadíme číslo zákazníkovi a inktementujeme pro dalšího

            this.model = model;
            string[] popisy = popis.Split(Proces.mezery, StringSplitOptions.RemoveEmptyEntries);
            this.ID = popisy[0];
            this.prichod = int.Parse(popisy[1]);
            this.trpelivost = int.Parse(popisy[2]);
            Nakupy = new List<string>();
            for (int i = 3; i < popisy.Length; i++)
            {
                Nakupy.Add(popisy[i]);
            }
            this.patro = 0;
            //Console.WriteLine("Init Zakaznik: {0}", ID);
            model.Naplanuj(prichod, this, TypUdalosti.Start);
        }
        public override void Zpracuj(Udalost ud)
        {
            switch (ud.co)
            {
                case TypUdalosti.Start:
                    PouzijSuperschopnosti();

                    if (Nakupy.Count == 0)
                    // ma nakoupeno
                    {
                        if (patro == 0)
                        {
                            //log("-------------- odchází"); // nic, konci
                            //Console.WriteLine("DKZSVOD = " + (model.Cas - prichod));
                            Program.all_DKZSVOD.Add(model.Cas - prichod);
                        }

                        else
                            model.vytah.PridejDoFronty(patro, 0, this);
                    }
                    else
                    {
                        Oddeleni odd = OddeleniPodleJmena(Nakupy[0]);
                        int pat = odd.patro;
                        if (pat == patro) // to oddeleni je v patre, kde prave jsem
                        {
                            if (Nakupy.Count > 1)
                                model.Naplanuj(model.Cas + trpelivost, this, TypUdalosti.Trpelivost);
                            odd.ZaradDoFronty(this);
                        }
                        else
                            model.vytah.PridejDoFronty(patro, pat, this);
                    }
                    break;
                case TypUdalosti.Obslouzen:
                    //log("Nakoupeno: " + Nakupy[0]);
                    Nakupy.RemoveAt(0);
                    // ...a budu hledat dalsi nakup -->> Start
                    model.Naplanuj(model.Cas, this, TypUdalosti.Start);
                    break;
                case TypUdalosti.Trpelivost:
                    //log("!!! Trpělivost: " + Nakupy[0]);
                    // vyradit z fronty:
                    {
                        Oddeleni odd = OddeleniPodleJmena(Nakupy[0]);
                        odd.VyradZFronty(this);
                    }

                    // prehodit tenhle nakup na konec:
                    string nesplneny = Nakupy[0];
                    Nakupy.RemoveAt(0);
                    Nakupy.Add(nesplneny);

                    // ...a budu hledat dalsi nakup -->> Start
                    model.Naplanuj(model.Cas, this, TypUdalosti.Start);
                    break;
            }
        }

        private void PouzijSuperschopnosti()
        {
            if (Nakupy.Count <= 1) return;

            int druh = P % 3;

            switch (P)
            {
                case 2:
            
                
                    for (int i = 0; i < Nakupy.Count; i++)
                    {
                        Oddeleni odd = OddeleniPodleJmena(Nakupy[i]);
                        if (odd != null && odd.patro == this.patro)
                        {
                            string vybranyNakup = Nakupy[i];
                            Nakupy.RemoveAt(i);
                            Nakupy.Insert(0, vybranyNakup);
                            break;
                        }
                    }
                    break;

                case 0:
                
                    int indexNejlepsiho = 0;
                    int nejmensiFronta = int.MaxValue;

                    for (int i = 0; i < Nakupy.Count; i++)
                    {
                        Oddeleni odd = OddeleniPodleJmena(Nakupy[i]);
                        if (odd != null)
                        {
                            int delkaFronty = odd.ZjistiDelkuFronty();
                            if (delkaFronty < nejmensiFronta)
                            {
                                nejmensiFronta = delkaFronty;
                                indexNejlepsiho = i;
                            }
                        }
                    }
                    if (indexNejlepsiho != 0)
                    {
                        string vybranyNakup = Nakupy[indexNejlepsiho];
                        Nakupy.RemoveAt(indexNejlepsiho);
                        Nakupy.Insert(0, vybranyNakup);
                    }
                    break;
                
            }
        }
        private Oddeleni OddeleniPodleJmena(string kamChci)
        {
            foreach (Oddeleni odd in model.VsechnaOddeleni)
                if (odd.ID == kamChci)
                    return odd;
            return null;
        }
    }


    public class Model
    {
        public int Cas;
        public Vytah vytah;
        public List<Oddeleni> VsechnaOddeleni = new List<Oddeleni>();
        public int MaxPatro;
        private Kalendar kalendar;
        public void Naplanuj(int kdy, Proces kdo, TypUdalosti co)
        {
            kalendar.Pridej(kdy, kdo, co);
        }
        public void Odplanuj(Proces kdo, TypUdalosti co)
        {
            kalendar.Odeber(kdo, co);
        }
        public void VytvorProcesy()
        {
            System.IO.StreamReader soubor
                = new
          System.IO.StreamReader("obchod_data.txt");
            while (!soubor.EndOfStream)
            {
                string s = soubor.ReadLine();
                if (s != "")
                {
                    switch (s[0])
                    {
                        case 'O':
                            new Oddeleni(this, s.Substring(1));
                            break;
                        case 'Z':
                            new Zakaznik(this, s.Substring(1));
                            break;
                        case 'V':
                            vytah = new Vytah(this, s.Substring(1));
                            break;
                    }
                }
            }
            soubor.Close();
        }
        public int Vypocet()
        {
            Cas = 0;
            kalendar = new Kalendar();
            VytvorProcesy();

            Udalost ud;

            while ((ud = kalendar.Vyber()) != null)
            {
                //Console.WriteLine("{0} {1} {2}", ud.kdy, ud.kdo.ID, ud.co);
                Cas = ud.kdy;
                ud.kdo.Zpracuj(ud);
            }
            return Cas;
        }
    }

    public class inputFile
    {
        public static void generateFile(int customerAmount)
        {
            System.IO.StreamWriter soubor = new System.IO.StreamWriter("obchod_data.txt");

            soubor.WriteLine(" Vstupní data pro simulaci obchodního domu");
            soubor.WriteLine("=========================================");
            soubor.WriteLine("");
            soubor.WriteLine(" Oddělení:");
            soubor.WriteLine("=========");
            soubor.WriteLine("O papírnictví 0 5");
            soubor.WriteLine("O potraviny 0 15");
            soubor.WriteLine("O drogerie 0 6");
            soubor.WriteLine("O textil 1 15");
            soubor.WriteLine("O nábytek 2 20");
            soubor.WriteLine("O elektronika 3 5");
            soubor.WriteLine("O CD-DVD 3 4");
            soubor.WriteLine("");
            soubor.WriteLine(" Výtah:");
            soubor.WriteLine("======");
            soubor.WriteLine("V elefant 10 1 1 1");
            soubor.WriteLine("");
            soubor.WriteLine(" Zákazníci:");
            soubor.WriteLine("==========");

            Random rnd = new Random(12345);

            List<string> mena = new List<string>
            {
            "Adam", "Beáta", "Cyril", "Čestmír", "Dávid", "Eliška", "František",
            "Gregor", "Hana", "Ivan", "Jakub", "Karolína", "Lukáš", "Marek",
            "Nina", "Ondrej", "Peter", "Quido", "Radovan", "Sára", "Šimon",
            "Tomáš", "Urban", "Václav", "Xénia", "Yvona", "Zuzana", "Žigmund"
            };

            for (int i = 0; i <= customerAmount; i++)
            {
                string customerName = mena[rnd.Next(mena.Count)];

                int arrival = rnd.Next(1, 601);
                int patience = rnd.Next(1, 181);
                int storeCount = rnd.Next(1, 21);

                string customerData = "Z " + customerName + " " + arrival + " " + patience;
                string storeName = "";

                for (int j = 0; j < storeCount; j++)
                {
                    int storeTypeID = rnd.Next(0, 7);

                    switch (storeTypeID)
                    {
                        case 0:
                            storeName = "papírnictví";
                            break;
                        case 1:
                            storeName = "potraviny";
                            break;
                        case 2:
                            storeName = "drogerie";
                            break;
                        case 3:
                            storeName = "textil";
                            break;
                        case 4:
                            storeName = "nábytek";
                            break;
                        case 5:
                            storeName = "elektronika";
                            break;
                        case 6:
                            storeName = "CD-DVD";
                            break;
                    }

                    customerData += " " + storeName;
                }

                soubor.WriteLine(customerData);
            }

            soubor.Close();
        }
    }

    class Program
    {
        public static List<int> all_DKZSVOD = new List<int> { };
        public static List<double> all_PDKZSVOD = new List<double> { };

        static void Main(string[] args)
        {
            for (int k = 1; k < 50; k++)
            {
                for (int i = 1; i <= 10; i++)
                {
                    inputFile.generateFile(k+1);

                    Model model = new Model();
                    model.Vypocet();
                    //Console.WriteLine("{0} KONEC --------------------------------", model.Vypocet());

                    double PDKZSVOD = all_DKZSVOD.Average();

                    if (i != 1 && i != 10)
                    {
                        all_PDKZSVOD.Add(PDKZSVOD);

                    }

                    //Console.WriteLine("PDKZSVOD = " + PDKZSVOD);
                }

                double avg_PDSZKVOD = all_PDKZSVOD.Average();

                //Console.WriteLine();
                Console.WriteLine("Average PDSZKVOD value for this test case is " + avg_PDSZKVOD);
            }

            Console.ReadLine();
        }
    }
}