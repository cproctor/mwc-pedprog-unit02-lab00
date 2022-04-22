class Pet:
    def __init__(self):
        '''This initializes the pet with its properties.'''

        self.name = None #The pet's name
        self.tired = False #Tells us if the pet is tired
        self.bored = True #Tells us if the pet is bored

    def set_name(self, name):
        '''This method sets the name property'''

        self.name = name

    def introduce(self):
        '''This method introduces the pet with its name.'''

        print("Hi, I'm", self.name)

    def play(self):
        '''If the pet is bored, the pet will play. It will then become tired.
        If the pet is not bored, the pet will not play.
        '''

        if self.bored == True: #The pet will only play if it's bored
            print("Let's play!!!")
            self.bored = False #Now the pet isn't bored anymore
            self.tired = True #But it's tired
        else:
            print("I don't want to play right now")

    def nap(self):
        '''If the pet is tired, the pet will sleep. It will then become bored.
        If the pet is not tired, the pet will not rest.
        '''

        if self.tired == True: #The pet will only nap if it's tired
            print("Zzzzzzzzzzzz.........")
            self.tired = False #Now the pet isn't tired anymore
            self.bored = True #But it's bored
        else:
            print("I'm not tired!!!!!")
