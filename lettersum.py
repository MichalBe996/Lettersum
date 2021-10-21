




while True:

    def lettersum():
        
        let_points = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26
            }
        word = input("Enter the word and the program will count its value: ")
        sum_of_letters = 0
        for letter in word:
            for key in let_points:
                if letter == key:
                    sum_of_letters += let_points[key]
        print("The sum of letters in your word is equal to: ", sum_of_letters)
        
    lettersum()
    