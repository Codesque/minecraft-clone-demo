
from ursina import * 
import random 

# Introduction to Entites and update() method 
'''
def introduction():  
    
    """
    Entities are the base objects for anything in Ursina. 
    With Entites you can build : 
        *Buttons 
        *Shapes 
        *Sounds 
    
    """
    app = Ursina()  
    #test_entity = Entity(model = 'circle' , color = color.yellow) # Draws a circle 
    test_entity = Entity(model = 'quad' , color = color.red) # Draws a square 
    #test_entity = Entity(model = 'cube' , color = color.green) # Draws 3 Dimensional Cube 
    test_entity1 = Entity(model = 'quad' , color = color.yellow , position=(2,2)) 
    test_entity2 = Entity(model = 'quad' , color = color.green , position=(-2,2) , scale = (1,4))  
    """
    Center of the screen is determined as (0,0) point. when y position is positive , the shape goes up . 
    Reversely if position y is negative , then the shape goes downwards  
    """ 
    
    
    app.run() 


def update(): 
    print("update method executes on every frame automaticly")   
    # test_entity.y -= 4 * time.dt # Moves the object in every frame 

introduction() 
'''


# Uploading a texture to the Entity
'''
def update(): 
    """
    You can use held_keys with keyboard , mouse inputs 
    
    """
    
    
    
    test_entity.z += 1 * time.dt  
    if held_keys['a'] : 
        test_entity.x -= 4 * time.dt 
    if held_keys['d'] : 
        test_entity.x += 4 * time.dt  
    if held_keys['w'] : 
        test_entity.y += 4 * time.dt 
    if held_keys['s'] : 
        test_entity.y -= 4 * time.dt   


app = Ursina()
test_entity = Entity( model = "cube" , color = color.pink)  
"""
sans_texture = load_texture("../assets/Sans.png")
sans = Entity(model = 'quad' , position = (2,2) , texture = sans_texture)  

OR YOU CAN DO THIS :
""" 
sans = Entity(model = 'quad' , position = (2,2) , texture = "../assets/Sans.png") 
app.run()  
''' 

# Creating Entities and buttons with OO Design
class TestCube(Entity):  

    def __init__(self):
        super().__init__(

            model = 'cube',
            color = color.peach,
            texture = 'white_cube',
            rotation = Vec3(45,45,45) 

        ) 

    def update(self): 
        if held_keys['d']: 
            self.x += 4 * time.dt  


class Test_Button(Button): 
    def __init__(self, text='Hello', radius=0.1, **kwargs):
        super().__init__(text,
         radius, 
         parent = scene, # parrent argument is essential . Without it , the button will cover the screen 
         model = "cube", 
         color = color.azure , 
         texture = "brick" , 
         highlight_color = color.cyan, # when you hover over it , it's color becomes cyan
         pressed_color = color.lime #green 
         ) 

    def input(self, key):
        
        if key == "left mouse down": 
            print("I am pressed") 

app = Ursina() 

smCube = TestCube()  
smButton = Test_Button()

app.run()



