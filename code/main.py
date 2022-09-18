from ursina import *  
from ursina.prefabs.first_person_controller import FirstPersonController   
#from menu import background , grid 





app = Ursina()  
menu_opened = False  
# Minecraft is voxel based game which means every single block that you see on minecraft is a voxel  

grass_texture = load_texture("assets/grass_block.png")
dirt_texture = load_texture("assets/dirt_block.png") 
stone_texture = load_texture("assets/stone_block.png") 
brick_texture = load_texture("assets/brick_block.png") 
sky_texture = load_texture("assets/skybox.png")

voxel_model = load_model("assets/block.obj") 



print(dir(voxel_model))




class Voxel(Button):   
    
    # Every voxel should be inherit from Button class.When you click on a voxel , it will create another voxel next to that voxel 
    def __init__(self , pos = (0,0,0) , texture = grass_texture  , gamemode = "survival"): 
        
        super().__init__(

            parent = scene,
            model = "assets/block.obj",
             
            position = pos, 
            origin_y = 0.5, 
            color = color.color(0,0,random.uniform(0.9 , 1)), # changes the shade of color by changing the z value of (,,)  
            texture = texture,
            highlight_color = color.lime ,
            scale = 0.5
        )  
        self.chosen_block = grass_texture 
        self.gamemode = gamemode 
        self.clicked = False    
      


        



    def input(self, key): 


            

        if self.hovered :   
            if key == "right mouse down": 
                voxel = Voxel(pos = self.position + mouse.normal , texture = self.chosen_block)  
            if key == "left mouse down": 
                
                if self.gamemode == "creative":
                    destroy(self)       

                if self.gamemode == "survival": 
                    destroy(self) 


                    
        

    def update(self):  
        
        if held_keys['1']: self.chosen_block = grass_texture 
        if held_keys['2']:  self.chosen_block = stone_texture  
        if held_keys['3']:  self.chosen_block = dirt_texture 
        if held_keys['4']:  self.chosen_block = brick_texture  

class Sky(Entity): 
    def __init__(self):
        super().__init__(
            model = "sphere",
            texture = sky_texture, 
            parent= scene,
            scale = 150,
            double_sided = True
        ) 

class Hand(Entity): 

    def __init__(self , mode = "creative"):
        super().__init__(

            parent = camera.ui ,
            model = "assets/arm.obj",
            texture = "assets/arm_texture.png", 
            position = Vec2(0.5 , -0.5) ,
            rotation = Vec3(150 , -30 , 0) , 
            scale = 0.2

        )  
        self.startAnimation = [False , False]  
        self.punch_animation = [False , False] 
        self.holding_mouse = False    
        self.punch_sound = Audio("assets/punch_sound.wav" , loop = True , autoplay = False )  
    
    def putting_animation(self):  
        kx , ky , kz = 100 * time.dt , 5 * time.dt , 0 * time.dt  
        px , py = 2 * time.dt , 2 * time.dt 
        if held_keys['right mouse']: 
            self.startAnimation[0] = True 
            self.position = Vec2(0.5 , -0.5) 
            self.rotation = Vec3(150 , -30 , 0)
            
        if self.startAnimation[0]: 
            
            if self.position.x > 0.3 and self.position.y < 0 : 
                self.position =  Vec2(self.position.x  - px  , self.position.y + py  )  
                self.rotation = Vec3(self.rotation.x +kx   , self.rotation.y    , self.rotation.z - kz )   
            else : 
                self.startAnimation[0] = False 
                self.startAnimation[1] = True 

        elif self.startAnimation[1]: 
             
            if self.position.x < 0.5 and self.position.y > -0.5 : 
                self.position =  Vec2(self.position.x  + px  , self.position.y - py  )    
                self.rotation = Vec3(self.rotation.x -kx     , self.rotation.y   , self.rotation.z + kz )
            else : 
                self.startAnimation[0] = False 
                self.startAnimation[1] = False 

    def punching_animation_active(self): 
        rx , ry , rz = 300 * time.dt  , 3 * time.dt , 3 * time.dt

        if self.punch_animation[0]: 
            
            self.rotation = Vec3(self.rotation.x + rx, self.rotation.y , self.rotation.z ) 
            if self.rotation.x > 200 : 
                self.punch_animation[0] = False 
                self.punch_animation[1] = True   

        if self.punch_animation[1]: 
            
            self.rotation = Vec3(self.rotation.x - rx, self.rotation.y , self.rotation.z ) 
            if self.rotation.x < 150 : 
                self.punch_animation[1] = False 
                self.punch_animation[0] = True  

    def input(self , key):  

        
        if key == "left mouse down":  
            self.isloop = True 
            self.punch_sound.play()  
            self.holding_mouse = True  
            self.punch_animation[0] = True 
             
        else :  
            self.punch_sound.stop()
            self.isloop = False 
            self.holding_mouse = False  
            self.punch_animation = [False , False]
            self.position = Vec2(0.5 , -0.5)
            self.rotation = Vec3(150 , -30 , 0)
  

    def update(self): 
        self.putting_animation()   
        self.punching_animation_active() 
        


def update(): 
    global menu_opened  



    if held_keys['q']:  
        raise SystemExit  



     
     
"""
def input(key): 
    global menu_opened
    if not menu_opened : 
        if held_keys['e'] : 
            menu_bg.enabled = True 
            menu_grids.enabled = True 
            menu_opened = True  
    elif held_keys['e']: 
        menu_bg.enabled = False 
        menu_bg.enabled = False  
        menu_opened = False  
"""



for i in range(40):  
    for j in range(40):
        voxel = Voxel((i , 0 , j )) 
player = FirstPersonController() 
sky = Sky() 
hands = Hand() 
 


app.run() 
