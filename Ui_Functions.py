#######################
# Signal and slot
#######################
import time
from PyQt5.QtCore import Qt


class Ui_Functions():
    def __init__(self, window):
        self.window = window
        self.ui = window.ui

        ########################
        # Declare Variables#####
        ########################
        self.arrAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't',
                            'u',
                            'v', 'w', 'x', 'y', 'z', ]
        self.arrMorse = ['01', '1000', '1010', '100', '0', '0010', '110', '0000', '00', '0111', '101', '0100', '11',
                         '10', '111',
                         '0110', '1101', '010', '000', '1', '001', '0001', '011', '1001', '1011', '1100']

        self.strText = "Ryusei takagi"

        ################################################
        # Connect Event Signals to Slots(Functions) ####
        ################################################
        self.ui.text_entry.textEdited.connect(self.text2morse)
        self.ui.morse_entry.textEdited.connect(self.morse2text)

    #######################
    # functions for slots
    #######################

    def text2morse(self):
        text = self.ui.text_entry.text()
        encoded_text, _ = self.encodeMor(text)
        self.ui.morse_entry.setText(" ".join(encoded_text))

    def morse2text(self):
        morse = self.ui.morse_entry.text().split(" ")
        decoded_morse = self.decodeMor(morse)
        self.ui.text_entry.setText(decoded_morse)

    def encodeMor(self, strText):
        strLower = strText.lower()
        arrCapital = []

        for i in range(len(strText)):
            if strText[i] == strLower[i]:
                arrCapital.append('0')
            else:
                arrCapital.append('1')

        strMorse = []
        for i in strLower:
            index = 0
            for j in self.arrAlphabet:

                if i == j:
                    strMorse.append(self.arrMorse[index])
                    index += 1

                elif i == ' ':
                    strMorse.append("/")  # Whatever symbol you want for space at arrMose[26]
                    index += 1
                    break
                else:
                    index += 1
        return strMorse, arrCapital

    def decodeMor(self, s, k=False):
        m = " "
        for i in range(len(s)):
            if s[i] == "/":
                m += " "
                continue
            for j in range(len(self.arrMorse)):
                if s[i] == self.arrMorse[j]:
                    if k is False or k[i] == "0":
                        m += self.arrAlphabet[j].lower()
                    else:
                        m += self.arrAlphabet[j].upper()
                    break

        return m

    ########################
    # Key Setting (ASCII)###
    ########################
    def key_event(self, event):
        # event.key() to get keyboard input
        print(event.key())
        key = event.key()
        if 48 <= key <= 57:
            self.update_pass(int(chr(key)))

        # 16777220 is Enter key code
        if key == 16777220:
            self.mousePressEvent()
