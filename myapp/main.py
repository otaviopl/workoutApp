#importS
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from workout import Workout
from exercises import Exercise
kivy.require('1.9.0')

class MeuApp(App):
    def build(self):
        Workouto_a = Workout("Treino Push", [Exercise("Supino Reto", 26),
                                        Exercise("Supino Inclinado", 24),
                                        Exercise("Agachamento Livre", 10),
                                        Exercise("Stiff",10),
                                        Exercise("Banco Scott",28)])

        Workouto_b = Workout("Treino Pull", [Exercise("Remada baixa", 90),
                                        Exercise("", 20),
                                        Exercise("Exercício 3", 35)])

        layout_principal = BoxLayout(orientation='vertical')
        self.label_Workouto = Label(text="Selecione um Treino")

        botao_Workouto_a = Button(text="Push")
        botao_Workouto_a.bind(on_press=lambda instance: self.mostrar_Exercises(Workouto_a))

        botao_Workouto_b = Button(text="Pull")
        botao_Workouto_b.bind(on_press=lambda instance: self.mostrar_Exercises(Workouto_b))

        layout_principal.add_widget(self.label_Workouto)
        layout_principal.add_widget(botao_Workouto_a)
        layout_principal.add_widget(botao_Workouto_b)

        return layout_principal

    def mostrar_Exercises(self, Workouto):
        self.label_Workouto.text = f"Exercícios do {Workouto.name}:"
        for Exercise in Workouto.exercises:
            self.label_Workouto.text += f"\n{Exercise.name}: {Exercise.weight} kg"


if __name__ == '__main__':
    MeuApp().run()