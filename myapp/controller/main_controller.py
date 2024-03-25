from model.DBfunctions import makeDictBd
from model import Exercise, Workout
from view.main_view import MeuApp

def buscar_treinos():
    return makeDictBd()

def show_exercises(nome_treino):
    treinos_exercicios = buscar_treinos()
    exercicios = treinos_exercicios.get(nome_treino, [])
    
    # Criando instâncias da classe Workout
    exercises_list = [Exercise(name, weight) for name, weight in zip(exercicios.keys(), exercicios.values())]
    workout = Workout(nome_treino, exercises_list)
    
    app = MeuApp.get_running_app()
    app.showExercises(workout)

def update_weight(exercise, new_weight):
    try:
        exercise.weight = float(new_weight)
    except ValueError:
        print("Erro: Peso inválido.")
