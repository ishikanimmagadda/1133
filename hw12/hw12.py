import tkinter as tk
import random
import csv

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    print("Implement this and then remove this print statement")
    def __init__(self, dex_number, name, catch_rate, speed): 
        self.dex_number = int(dex_number)
        self.name = name 
        self.catch_rate = int(catch_rate)
        self.speed = int(speed)

        
    def __str__(self): 
        string = "Species Name: " + self.name
        return string
    
if __name__ == "__main__": 
    pikachu = Pokemon(25, "Pikachu", 190, 90)
    print(pikachu)
    
#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        print("In SafariSimulator init")
        super().__init__(master)
        self.master = master 
        
        pokedex = []
        with open("pokedex.csv", 'r') as csv_file: 
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                dex_number, name, catch_rate, speed = row
                pokedex.append(Pokemon(dex_number, name, catch_rate, speed))
        
        self.pokedex = pokedex
        self.current_pokemon = None # Tracks the currently encountered Pokémon
        self.safari_balls = 30
        self.caught_pokemon = []
        
        
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        #Call nextPokemon() method here to initialize your first random pokemon
        self.nextPokemon()

    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.safari_balls) + " left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()
        
        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        
        # Status message label
        self.messageLabel = tk.Label(self, bg="grey", text="", font=("Arial", 12))
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        # Pokémon image label
        self.pokemonImageLabel = tk.Label(self)
        self.pokemonImageLabel.pack(pady=20)

        # Catch probability label
        self.catchProbLabel = tk.Label(self, text="", font=("Arial", 12))
        self.catchProbLabel.pack(pady=9)

        #Complete and pack the catchProbLabel here.
        self.catchProbLabel = tk.Label(self, text="")
        self.catchProbLabel.pack(pady=10)

    def nextPokemon(self):
        print("In nextPokemon")
        self.current_pokemon = random.choice(self.pokedex)
        probability = int((min((self.current_pokemon.catch_rate + 1), 151) / 449.5) * 100)
        
        self.messageLabel["text"] = f"You encounter a wild {self.current_pokemon.name}!"
        self.catchProbLabel["text"] = f"Your chance of catching it is {probability}%!"
        
        # Load and display the Pokémon image
        self.photo = tk.PhotoImage(file=f"sprites/{self.current_pokemon.dex_number}.gif")
        self.pokemonImageLabel["image"] = self.photo
        
        

        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        print("In throwBall")
        self.safari_balls = self.safari_balls - 1 
        self.throwButton["text"] = f"Throw Safari Ball ({self.safari_balls} left)"
        
        if self.safari_balls <= 0:
            self.endAdventure()
            return
        
        rand_value = random.random()
        probability = min((self.current_pokemon.catch_rate + 1), 151) / 449.5
        
        if rand_value < probability:
            self.caught_pokemon.append(self.current_pokemon)
            self.messageLabel["text"] = f"Gotcha! You caught {self.current_pokemon.name}!"
            self.nextPokemon()
        else:
            self.messageLabel["text"] = "Aargh! It escaped!"

        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        print("In endAdventure")
        
        print("In endAdventure")
        self.throwButton.pack_forget()
        self.runButton.pack_forget()
        self.pokemonImageLabel.pack_forget()
        self.catchProbLabel.pack_forget()
        
        self.messageLabel["text"] = "You're all out of balls, hope you had fun!"
        # Create the summary of caught Pokémon
        if hasattr(self, 'caught_pokemon') and self.caught_pokemon:  # Check if any Pokémon were caught
            caught_list = "\n".join([pokemon.name for pokemon in self.caught_pokemon])
            summary = f"You caught {len(self.caught_pokemon)} Pokémon:\n{caught_list}"
        else:
            summary = "Oops, you caught 0 Pokémon."
        
        # Display the result summary
        resultLabel = tk.Label(self, text=summary, font=("Arial", 12), justify="left", wraplength=250)
        resultLabel.pack(pady=10)
        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.

#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
