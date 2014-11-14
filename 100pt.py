from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 5


class MyApp:

	
        def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		#up
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "white")
		self.up.grid(row=0,column=1)
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.upClick)
		
		#down
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "white")
		self.down.grid(row=3,column=1)
		# "Bind" an action to the first button												
		self.down.bind("<Button-1>", self.downClick)
		
		#left
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "white")
		self.left.grid(row=2,column=0)
		# "Bind" an action to the first button												
		self.left.bind("<Button-1>", self.leftClick)
		
		#right
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "white")
		self.right.grid(row=2,column=2)
		# "Bind" an action to the first button												
		self.right.bind("<Button-1>", self.rightClick)  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
                self.animateTarget()

        def animateTarget(self):
            global direction
            # Get the x and y co-ordinates of the circle
            tx1, ty1, tx2, ty2 = drawpad.coords(target)
            if tx2 > drawpad.winfo_width(): 
                direction = - 5
            elif tx1 < 0:
                direction = 5
    #Move our oval object by the value of direction
            drawpad.move(target,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
            didWeHit = self.collisionDetect()
            if didWeHit:
                    drawpad.after(10, self.animateTarget)
        
        

	

		
	def upClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if y1 > 0:
		  drawpad.move(player,0,-10)

        def downClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if y2 < 320:
		  drawpad.move(player,0,10)
		  
	def leftClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if x1 > 0:
		  drawpad.move(player,-10,0)

        def rightClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if x2 < drawpad.winfo_width():
		  drawpad.move(player,10,0)



                
		# Ensure that we are doing our collision detection
		# After we move our object!
                
                
                    
                                                            
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global target
		global drawpad
                global player
                global targetx1,targety1,targetx2,targety2
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                if (x1 > tx1 and x2 < tx2) and (y1 > ty1 and y2 < ty2):
                    return False
                else:
                    return True


                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()