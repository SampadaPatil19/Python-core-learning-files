class Song:
    def __init__(self, name, singer, budget):
        self.name = name
        self.singer = singer
        self.budget = budget

    def __str__(self):
        return f"NAME: {self.name}\nSINGER: {self.singer}\nBUDGET: {self.budget}"
    
singer1 = Song('Khairiyat', 'Arjit Singh', 500000000)
print('--------------------------------')
print(singer1)
print('--------------------------------')
