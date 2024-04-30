# serializace

import pickle

# seznam = ['ab', 'cd', 'ef', 'gh']
#
# serializovane_data = pickle.dumps(seznam)
# print(serializovane_data)
#
# deserializovane_data = pickle.loads(serializovane_data)
# print(deserializovane_data)

class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def __str__(self):
        return f'Jméno a příjmení je {self.jmeno} {self.prijmeni}'

def save_data(file):
    return pickle.dumps(file)

def load_data(file):
    return pickle.loads(file)



def main():
    p1 = Clovek('Papa', 'Smurf')
    serializace = save_data(p1)
    deserializace = load_data(serializace)
    print(deserializace)



if __name__ == '__main__':
    main()







