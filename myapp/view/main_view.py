import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from controller.main_controller import buscar_treinos, show_exercises, update_weight

kivy.require('1.9.0')

class MeuApp(App):

    def build(self):
        self.layout_principal = BoxLayout(orientation='vertical')
        self.label_Workout = Label(text="Selecione um Treino")

        botao_Workout_a = Button(text="Push")
        botao_Workout_a.bind(on_press=lambda instance: show_exercises("Treino Push A"))

        botao_Workout_b = Button(text="Pull")
        botao_Workout_b.bind(on_press=lambda instance: show_exercises("Treino Pull B"))

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
                               update_weight(e, i.text))

            self.layout_principal.add_widget(label_exercise)
            self.layout_principal.add_widget(input_weight)
            self.layout_principal.add_widget(button_update)

    def update_weight(self, exercise, new_weight):
        try:
            exercise.weight = float(new_weight)
            self.label_Workout.text += f"\n{exercise.name}: {exercise.weight} kg"
        except ValueError:
            print("Erro: Peso inválido.")
