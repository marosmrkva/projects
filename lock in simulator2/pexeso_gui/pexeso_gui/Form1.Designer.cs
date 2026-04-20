namespace pexeso_gui
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.LPravidla = new System.Windows.Forms.Label();
            this.LPocetTahov = new System.Windows.Forms.Label();
            this.LVysledok = new System.Windows.Forms.Label();
            this.BStart = new System.Windows.Forms.Button();
            this.BExit = new System.Windows.Forms.Button();
            this.BDalsiaHra = new System.Windows.Forms.Button();
            this.LNazov = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // LPravidla
            // 
            this.LPravidla.AccessibleName = "LPravidla";
            this.LPravidla.AutoSize = true;
            this.LPravidla.Font = new System.Drawing.Font("Elephant", 15F);
            this.LPravidla.Location = new System.Drawing.Point(317, 136);
            this.LPravidla.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LPravidla.Name = "LPravidla";
            this.LPravidla.Size = new System.Drawing.Size(319, 130);
            this.LPravidla.TabIndex = 0;
            this.LPravidla.Text = "Pravidla:\r\n1. Obráť kartičku\r\n2. Skús jej nájsť pár\r\n3. Opakuj kým nenájdeš všetk" +
    "y\r\n4. Uži si hru :)";
            this.LPravidla.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // LPocetTahov
            // 
            this.LPocetTahov.AccessibleName = "LSkore";
            this.LPocetTahov.AutoSize = true;
            this.LPocetTahov.Font = new System.Drawing.Font("Elephant", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LPocetTahov.Location = new System.Drawing.Point(716, 30);
            this.LPocetTahov.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LPocetTahov.Name = "LPocetTahov";
            this.LPocetTahov.Size = new System.Drawing.Size(54, 35);
            this.LPocetTahov.TabIndex = 1;
            this.LPocetTahov.Text = "53";
            this.LPocetTahov.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // LVysledok
            // 
            this.LVysledok.AccessibleName = "LPocetTahov";
            this.LVysledok.AutoSize = true;
            this.LVysledok.Font = new System.Drawing.Font("Elephant", 39.74999F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LVysledok.Location = new System.Drawing.Point(242, 99);
            this.LVysledok.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LVysledok.Name = "LVysledok";
            this.LVysledok.Size = new System.Drawing.Size(496, 68);
            this.LVysledok.TabIndex = 2;
            this.LVysledok.Text = "GRATULUJEM!";
            this.LVysledok.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // BStart
            // 
            this.BStart.AccessibleName = "BStart";
            this.BStart.BackColor = System.Drawing.Color.Red;
            this.BStart.Font = new System.Drawing.Font("Elephant", 47.99999F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BStart.Location = new System.Drawing.Point(306, 297);
            this.BStart.Margin = new System.Windows.Forms.Padding(4);
            this.BStart.Name = "BStart";
            this.BStart.Size = new System.Drawing.Size(330, 189);
            this.BStart.TabIndex = 3;
            this.BStart.Text = "START";
            this.BStart.UseVisualStyleBackColor = false;
            this.BStart.Click += new System.EventHandler(this.BStart_Click);
            // 
            // BExit
            // 
            this.BExit.AccessibleName = "BNaStart";
            this.BExit.BackColor = System.Drawing.Color.Red;
            this.BExit.Font = new System.Drawing.Font("Elephant", 15F);
            this.BExit.Location = new System.Drawing.Point(799, 13);
            this.BExit.Margin = new System.Windows.Forms.Padding(4);
            this.BExit.Name = "BExit";
            this.BExit.Size = new System.Drawing.Size(150, 61);
            this.BExit.TabIndex = 4;
            this.BExit.Text = "EXIT";
            this.BExit.UseVisualStyleBackColor = false;
            this.BExit.Click += new System.EventHandler(this.BExit_Click);
            // 
            // BDalsiaHra
            // 
            this.BDalsiaHra.AccessibleName = "BExit";
            this.BDalsiaHra.BackColor = System.Drawing.Color.Red;
            this.BDalsiaHra.Font = new System.Drawing.Font("Elephant", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.BDalsiaHra.Location = new System.Drawing.Point(306, 297);
            this.BDalsiaHra.Margin = new System.Windows.Forms.Padding(4);
            this.BDalsiaHra.Name = "BDalsiaHra";
            this.BDalsiaHra.Size = new System.Drawing.Size(330, 189);
            this.BDalsiaHra.TabIndex = 5;
            this.BDalsiaHra.Text = "Späť do menu";
            this.BDalsiaHra.UseVisualStyleBackColor = false;
            this.BDalsiaHra.Click += new System.EventHandler(this.BDalsiaHra_Click);
            // 
            // LNazov
            // 
            this.LNazov.AccessibleName = "";
            this.LNazov.AutoSize = true;
            this.LNazov.Font = new System.Drawing.Font("Elephant", 50F);
            this.LNazov.Location = new System.Drawing.Point(307, 30);
            this.LNazov.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LNazov.Name = "LNazov";
            this.LNazov.Size = new System.Drawing.Size(367, 87);
            this.LNazov.TabIndex = 6;
            this.LNazov.Text = "PEXESO";
            this.LNazov.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Gray;
            this.ClientSize = new System.Drawing.Size(962, 550);
            this.Controls.Add(this.LNazov);
            this.Controls.Add(this.BDalsiaHra);
            this.Controls.Add(this.BExit);
            this.Controls.Add(this.BStart);
            this.Controls.Add(this.LVysledok);
            this.Controls.Add(this.LPocetTahov);
            this.Controls.Add(this.LPravidla);
            this.Font = new System.Drawing.Font("Comic Sans MS", 10F);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label LPravidla;
        private System.Windows.Forms.Label LPocetTahov;
        private System.Windows.Forms.Label LVysledok;
        private System.Windows.Forms.Button BStart;
        private System.Windows.Forms.Button BExit;
        private System.Windows.Forms.Button BDalsiaHra;
        private System.Windows.Forms.Label LNazov;
    }
}

