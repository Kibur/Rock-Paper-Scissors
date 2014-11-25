__author__ = 'Kibur'

from gi.repository import Gtk
import random

class RPS:
    def __init__(self, choice = None):
        if choice is not None:
            self._selected = choice
        else:
            options = ["Rock", "Paper", "Scissors"]
            self._selected = options[random.randint(0, len(options) - 1)]

    def getSelected(self):
        return self._selected

    def combinations(self, yourChoice, otherChoice):
        result = -1

        print "Player1: %s" % (yourChoice)
        print "Player2: %s" % (otherChoice)

        if ((yourChoice == "Rock") and (otherChoice == "Scissors"))\
                or ((yourChoice == "Paper") and (otherChoice == "Rock"))\
                or ((yourChoice == "Scissors") and (otherChoice == "Paper")):
            result = True
        elif ((yourChoice == "Scissors") and (otherChoice == "Rock"))\
                or ((yourChoice == "Paper") and (otherChoice == "Scissors"))\
                or ((yourChoice == "Rock") and (otherChoice == "Paper")):
            result = False

        return result

    def compare(self, other):
        yourChoice = self.getSelected()
        otherChoice = other.getSelected()

        win = self.combinations(yourChoice, otherChoice)

        print win

        if win is True:
            return "Congratulations, you win!"
        elif win is False:
            # Senior Chang
            return "HA, gay!"
        else:
            # Abed
            return "Cool cool, cool ..."

class UI:
    # Handlers
    def window_close(self, *args):
        Gtk.main_quit(args)

    def on_button_clicked(self, button):
        player1 = RPS(self.choice)
        player2 = RPS()

        self.lblResult.set_label(player1.compare(player2) + '\n' + "System had " + player2.getSelected().upper())

    def on_radio_toggle(self, radio):
        # Load appropriate images
        if radio.get_active():
            self.choice = radio.get_label()
            self.imgSelected.set_from_file(self.images[self.choice])
    # ---

    def connectHandlers(self):
        self.window.connect('delete-event', self.window_close)
        self.btnPlay.connect('clicked', self.on_button_clicked)
        self.rbRock.connect('toggled', self.on_radio_toggle)
        self.rbPaper.connect('toggled', self.on_radio_toggle)
        self.rbScissors.connect('toggled', self.on_radio_toggle)

    def retreiveObjects(self):
        self.window = self.builder.get_object("window1")
        self.rbRock = self.builder.get_object('rbRock')
        self.rbPaper = self.builder.get_object('rbPaper')
        self.rbScissors = self.builder.get_object('rbScissors')
        self.lblResult = self.builder.get_object('lblResult')
        self.btnPlay = self.builder.get_object('btnPlay')
        self.imgSelected = self.builder.get_object('imgSelected')

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("view.glade")

        self.retreiveObjects()
        self.connectHandlers()

        self.window.show()

        self.choice = "Rock"
        self.images = {
            "Rock" : "img/Rock.gif",
            "Paper" : "img/Paper.gif",
            "Scissors" : "img/Scissors.gif"
        }

if __name__ == "__main__":
    ui = UI()
    Gtk.main()