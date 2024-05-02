using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Speech.Synthesis;

namespace SpeechToText
{
    public partial class Form1 : Form
    {
        SpeechSynthesizer speech;
        
        public Form1()
        {
            InitializeComponent();
            speech = new SpeechSynthesizer();
        }

        private void PictureBox1_Click(object sender, EventArgs e)
        {
            
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            if (richTextBox1.Text != "")
            {
                speech.SelectVoiceByHints(VoiceGender.Female);
                speech.SpeakAsync(richTextBox1.Text);
                
            }
        }

        private void Button1_Click_1(object sender, EventArgs e)
        {
            if (speech.State == SynthesizerState.Speaking)
            {
                speech.Pause();
            }
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            if (speech.State == SynthesizerState.Paused)
            {
                speech.Resume();
            }
        }
    }
}
