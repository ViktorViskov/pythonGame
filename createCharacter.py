from character import Character

characters = {
    "Fighter":
    {
        "HP":100,
        "attack":10,
        "defence":7
    },
    "Defender":
    {
        "HP":150,
        "attack":5,
        "defence":12
    },
    "Mag":
    {
        "HP":70,
        "attack":15,
        "defence":5
    }
}

# creating characters
class CreateCharacter: 
    # initialization
    def __init__(self, name, type):
        # create character
        self.createdCharacter = Character(name,characters[type]["HP"],characters[type]["attack"],characters[type]["defence"])


