
from ursina import * 

app = Ursina()


def update(): 

    if held_keys["q"]: 
        raise SystemExit


class BG(Entity): 
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "quad",
            texture = "assets/bg.png" ,  
            scale = (0.56,0.86) # 0.06 values are coming from padding that is here for grid 

        ) 

class Item(Draggable): 
    def __init__(self , container , type , pos):
        super().__init__(

            parent = container, 
            model = "quad", 
            texture = type ,
            color = color.white, 
            scale_x = 1 / (container.texture_scale[0] * 1.5) , 
            scale_y = 1 / (container.texture_scale[1] * 1.5) , 
            origin = (-0.75 , 0.75),
            x = pos[0] / container.texture_scale[0] , 
            y = pos[1] / container.texture_scale[1] 
        ) 

    
    def drag(self): 
        self.xy_pos = (self.x , self.y)  

    

    def get_item_pos(self): 
        x = int(self.x * self.parent.texture_scale[0]) 
        y = int(self.y * self.parent.texture_scale[1])
        return Vec2(x,y) 
    
    
    def menu_constrait(self): 
        if self.x < 0 or self.x > 1 or self.y > 0 or self.y < -1 : 
            self.x , self.y = self.xy_pos
    

    def drop(self): 
        #print(f"x:{self.x} // y: {self.y} ")  
        self.x = int((self.x + self.scale_x/2 ) * 5) / 5  
        self.y = int((self.y - self.scale_x/2 ) * 8) / 8  
        self.menu_constrait()   
        self.overlap_check() 

    def overlap_check(self): 

        for child in self.parent.children : 
            if child.x == self.x and child.y == self.y and self != child : 
                child.x = self.xy_pos[0] 
                child.y = self.xy_pos[1] 



class Grid(Entity): 

    def __init__(self):
        super().__init__(

            parent = camera.ui ,
            model = "quad",
            texture = "assets/box.png",
            texture_scale = (5,8),
            scale = (0.5 , 0.8), 
            color = color.gray , 
            origin = (-0.5 , 0.5) , 
            position = (-0.25 , 0.4) 
        )   
        self.import_textures()
        self.add_new_item() 

 

    def find_free_cell(self): 
        all_cells = [Vec2(x , y) for y in range(0,-8,-1) for x in range(0,5)] 
        taken_cells = [child.get_item_pos() for child in self.children  ] 
        for cell in all_cells : 
            if cell not in taken_cells:   
                return cell
        return False 


    def add_new_item(self): 
        pos = self.find_free_cell() 
        if pos :
            Item(self , random.choice(self.textures) , pos)  

    def import_textures(self): 
        self.textures = [ 
            load_texture("assets/grass.png") , 
            load_texture("assets/dirt.png") ,
            load_texture("assets/stone.png") ,
        ] 

def input(key): 
    if key == 'a': 
        grid.add_new_item() 

    if key == 'e': 
        inventory_opened = not inventory_opened



background = BG() 
grid = Grid() 




app.run()





