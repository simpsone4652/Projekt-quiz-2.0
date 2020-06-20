import time

print("Witaj w teleturnieju!\nZa chwilę otrzymasz 10 pytań, na które będziesz musiał poprawnie odpowiedzieć.\nPowodzenia! \n\n")
time.sleep(2)
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

print("Przejdźmy do pierwszego pytania!")
time.sleep(1)
question_prompts = [
    "\nCarpaccio to danie kuchni:\n(a)Włoskiej \n(b)Portugalskiej\nOdpowiedż: ",
    "\n"
    "Włożyliśmy 100 zł do banku i dostaliśmy od razu 20 proc. odsetek. Rząd zabrał nam z całej kwoty w banku 20 proc. podatku. Zyskaliśmy, czy straciliśmy na tej operacji? Zyskaliśmy Straciliśmy Nic się nie dla nas zmieniło?\n(a)Straciliśmy \n(b)Zyskaliśmy\nOdpowiedż: ",
    "\n"
    "Który miesiąc ma 28 dni?\n(a)Luty co 4 lata \n(b)Marzec co 4 lata\nOdpowiedż: ",
    "\n"
    "Jakie jest trzecie terytorialnie największe państwo świata (po Rosji i Kanadzie)?\n(a)Chiny\n(b)Mongolia\nOdpowiedż: ",
    "\n"
    "Przez który z tych krajów przechodzi równik?\n(a)Etiopia\n(b)Kenia\nOdpowiedż: ",
    "\n"
    "Co to jest batyskaf?\n(a)Łódź podwodna przeznaczona do dużych głębokości\n(b)Rodzaj mikroskopu\nOdpowiedż: ",
    "\n"
    "W którym roku uruchomiono wyszukiwarkę Google??\n(a)w 1998r.\n(b)w 1995 r.\nOdpowiedż: ",
    "\n"
    "Jaki kolor ma zazwyczaj czarna skrzynka w samolocie??\n(a)Pomarańczowy \n(b)Czarny\nOdpowiedż: ",
    "\n"
    "Która marka nie produkuje ciągników??\n(a)Massey Ferguson(a) \n(b)Jaguar\nOdpowiedż: ",
    "\n"
    "Który producent telewizorów pochodzi z Niemiec??\n(a)Grundig \n(b)Philips\nOdpowiedż: ",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a"),

]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("\nDobrze to poprawna odpowiedź!")
            
        else:
              print("\nNiestety ale to nie prawda..")
      
    print("Gratulacje to już było ostatnie pytanie w tym teleturnieju...")
    print("Odpowiedziałeś poprawnie na:", score, "z", len(questions))


        

  
run_quiz(questions)