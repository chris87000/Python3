class Quiz:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse
        self.tries = 0

    def ask(self):
        print(self.question)
        rep = input()
        if rep == self.reponse:
            print('bravo')
        else:
            print("c'est faux !")
            self.tries += 1
            if self.tries > 2:
                print("perdu")
                return
            self.ask()
         
q = Quiz("Est-ce que ce MOOC est sur Python 3 ?", "oui")
q.ask()

