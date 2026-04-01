# 1 base class -> 1 child class -> 1 child class

class Book:
    def __init__(self, title):
        self.title = title

class Ebook(Book):
    def __init__(self, title, file_size):
        super().__init__(title)
        self.file_size = file_size

    def display(self):
        print('TITLE: ',self.title)
        print('FILE SIZE: ',self.file_size)

class AudioBook(Ebook):
    def __init__(self, title, file_size, duration):
        super().__init__(title, file_size)
        self.duration = duration
    
    def show_data(self):
        super().display()
        print('DURATION: ',self.duration)

# book = AudioBook('ABC', '12mb', '3hr')
# book.show_data()

ebook = Ebook('BCS', '11mb')
ebook.display()