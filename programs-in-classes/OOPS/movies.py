class Movie:
    def __init__(self, name = 'YJHD', genre = 'Drama', director = 'Ayaan Mukharjee', release_date = '31 May 2013'):
        self.name = name
        self.genre = genre
        self.director = director
        self. release_date = release_date

    def getData(self):
        data = f"NAME: {self.name}\nGENRE: {self.genre}\nDIRECTOR: {self.director}\nRELEASE_DATE: {self.release_date}\n--------------------------------"

        return data
    
m1 = Movie()
m2 = Movie('Singham', 'Action', 'Rohit Shetty', '22 June 2011')

print(m1.getData())
print(m2.getData())