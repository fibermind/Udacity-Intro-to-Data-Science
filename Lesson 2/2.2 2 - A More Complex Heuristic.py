
import pandas


def complex_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        predictions = {}
        df = pandas.read_csv(file_path)
        for passenger_index, passenger in df.iterrows():
            passenger_id = passenger['PassengerId']
            if passenger['Sex'] == 'female':
                predictions[passenger['PassengerId']] = 1
            elif passenger['Age'] < 18 and passenger['Pclass'] is 1:
                predictions[passenger['PassengerId']] = 1

            else:
                predictions[passenger['PassengerId']] = 0
        return predictions

    print complex_heuristic(file_path)

file_path= './titanic-data2.csv'
print complex_heuristic(file_path)
