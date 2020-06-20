class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Carpaccio to danie kuchni:?\n(a)Włoskiej \n(b)Portugalskiej\nOdpowiedż: ",
    "Włożyliśmy 100 zł do banku i dostaliśmy od razu 20 proc. odsetek. Rząd zabrał nam z całej kwoty w banku 20 proc. podatku. Zyskaliśmy, czy straciliśmy na tej operacji? Zyskaliśmy Straciliśmy Nic się nie dla nas zmieniło?\nStraciliśmy(a) \n(b)Zyskaliśmy\nOdpowiedż: ",
    "Który miesiąc ma 28 dni?\n(a)Luty co 4 lata \n(b)Marzec co 4 lata\nOdpowiedż: ",
    "Jakie jest trzecie terytorialnie największe państwo świata (po Rosji i Kanadzie)?\nChiny(a)\nMongolia(b)\nOdpowiedż: ",
    "Przez który z tych krajów przechodzi równik?\nEtiopia(a)\nKenia(b)\nOdpowiedż: ",
    "Co to jest batyskaf?\nŁódź podwodna przeznaczona do dużych głębokości(a)\nRodzaj mikroskopu(b)\nOdpowiedż: ",
    "W którym roku uruchomiono wyszukiwarkę Google??\nw 1998r.(a) \nw 1995 r.(b)\nOdpowiedż: ",
    "Jaki kolor ma zazwyczaj czarna skrzynka w samolocie??\nPomarańczowy(a) \nCzarny(b)\nOdpowiedż: ",
    "Która marka nie produkuje ciągników??\nMassey Ferguson(a) \nJaguar(b)\nOdpowiedż: ",
    "Który producent telewizorów pochodzi z Niemiec??\nGrundig(a) \nPhilips(b)\nOdpowiedż: ",
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
    print("you got", score, "out of", len(questions))


run_quiz(questions)