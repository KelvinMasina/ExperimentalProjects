using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Speech;
using System.Speech.Synthesis;
using System.Speech.Recognition;
using System.Threading;
using System.Diagnostics;

namespace VoiceRecognition
{
    public partial class Form1 : Form
    {
        //Declaring global variables and objects
        SpeechSynthesizer ss = new SpeechSynthesizer();
        PromptBuilder pb = new PromptBuilder();
        SpeechRecognitionEngine sre = new SpeechRecognitionEngine();
        Choices clist = new Choices();


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void BtnStart_Click(object sender, EventArgs e)
        {
            
            //Star button click
            btnStart.Enabled = false;
            btnStop.Enabled = true;
            clist.Add(new string[]{ "Hello", "How are you?", "Thank You", "What is the current time?",
                "Open VLC", "Close" });
            Grammar gr = new Grammar(new GrammarBuilder(clist)); 

            try
            {
                sre.RequestRecognizerUpdate();
                sre.LoadGrammar(gr);
                sre.SpeechRecognized += sre_SpeechRecognized;
                sre.SetInputToDefaultAudioDevice();
                sre.RecognizeAsync(RecognizeMode.Multiple);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error");               
            }

        }

        private void sre_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            ss.SelectVoiceByHints(VoiceGender.Female);
            switch(e.Result.Text.ToString())
            {
                case "Hello":
                    ss.SpeakAsync("Hello Johnny Flag. My name is Florence, I am your personal assistant.");
                    break;
                case "How are you?":
                    ss.SpeakAsync("I am doing great, How about you?");
                    break;
                case "Thank You":
                    ss.SpeakAsync("You are welcome Johnny");
                    break;
                case "What is the current time?":
                    ss.SpeakAsync("Current time is " + DateTime.Now.ToLongTimeString());
                    break;
                case "Open VLC":
                    Process.Start("VLC"); 
                    break;
                case "Close":
                    Application.Exit();
                    break;
            }
            txtContents.Text += e.Result.Text.ToString() + Environment.NewLine;
        }

        private void BtnStop_Click(object sender, EventArgs e)
        {
            //Stop button click
            sre.RecognizeAsyncStop();
            btnStart.Enabled = true;
            btnStop.Enabled = false;
        }
    }
}
