#importS
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from workout import Workout
from exercises import Exercise
from kivy.uix.textinput import TextInput
kivy.require('1.9.0')
from pymongo import MongoClient
MONGODB_URL = "mongodb://localhost:27017/" 

class MeuApp(App):

    def build(self):
        try:
            client= MongoClient(MONGODB_URL)
            db=client['wkapp']
            collection = db['workout']
        except:
            print('ERROR AT THE CONNECTION TO BD')

        Workout_a = Workout("Treino Push A", [Exercise("Supino Reto", 20),
                                              Exercise("Supino Inclinado", 20),
                                              Exercise("Desenvolvimento Militar", 16)])
        
        Workout_b = Workout("Treino Push B", [Exercise("Banco Scott", 20),
                                              Exercise("Tríceps Corda", 20),
                                              Exercise("Tríceps Testa", 16)])

        Workout_c = Workout("Treino Pull A", [Exercise("Remada baixa", 90),
                                              Exercise("Puxada alta aberta", 50),
                                              Exercise("Puxada alta fechada", 45)])
        
        Workout_d = Workout("Treino Push B", [Exercise("Supino Reto", 20),
                                              Exercise("Supino Inclinado", 20),
                                              Exercise("Desenvolvimento Militar", 16),
                                              Exercise("Stiff", 10),
                                              Exercise("Banco Scott", 28)])
        
        self.layout_principal = BoxLayout(orientation='vertical')
        self.label_Workout = Label(text="Selecione um Treino")

        botao_Workout_a = Button(text="Push")
        botao_Workout_a.bind(on_press=lambda instance: self.showExercises(Workout_a))

        botao_Workout_b = Button(text="Pull")
        botao_Workout_b.bind(on_press=lambda instance: self.showExercises(Workout_b))

        self.layout_principal.add_widget(self.label_Workout)
        self.layout_principal.add_widget(botao_Workout_a)
        self.layout_principal.add_widget(botao_Workout_b)

        return self.layout_principal

    def showExercises(self, workout):
        self.layout_principal.clear_widgets()
        self.layout_principal.add_widget(self.label_Workout)

        self.label_Workout.text = f"Exercícios do {workout.name}:"
        for exercise in workout.exercises:
            label_exercise = Label(text=f"{exercise.name}: {exercise.weight} kg")
            input_weight = TextInput(text=str(exercise.weight), multiline=False)
            button_update = Button(text="Atualizar Peso")
            button_update.bind(on_press=lambda instance, e=exercise, i=input_weight:
                               self.update_weight(e, i.text))

            self.layout_principal.add_widget(label_exercise)
            self.layout_principal.add_widget(input_weight)
            self.layout_principal.add_widget(button_update)

    def update_weight(self, exercise, new_weight):
        try:
            exercise.weight = float(new_weight)
            self.label_Workout.text += f"\n{exercise.name}: {exercise.weight} kg"
        except ValueError:
            print("Erro: Peso inválido.")


if __name__ == '__main__':
    MeuApp().run()