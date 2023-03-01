import math 

"""class for plotting routes"""
class GridPlotter: 
 
    def __init__(self,size,): # initialise with size of grid plot
        self.size=size
        
            
    def plot(self,coords): # function to visualise the plot        
        M= [[ '+ ' for x in range(self.size)] for x in range(self.size)]
        for coord in coords :
            M[-(coord[1])][coord[0]-1]= 'O '
        M.append(["%2s" % str(x) for x in range(self.size+1)])
        for i in range(self.size):
            M[i].insert(0,"%2d "%(self.size-(i)))
        
        print('\n'.join([' '.join(M[i]) for i in range(self.size+1)]))

"""instance function to generate list of coordinates from route file"""        
def getCoords(filename): 
        ind=False
        with open(filename) as f:
            route=f.readlines()
        route=[direction.strip() for direction in route]
        coords=[]
        pos=[int(route[0]),int(route[1])]
        for i in range(2,len(route)):
            coords.append(tuple(pos))
            if pos[0]<1 or pos[1]<1 or pos[0]>12 or pos[1]>12:
                ind=True
                break
            elif route[i]=='N':
                pos[1]+=1
            elif route[i]=='S':
                pos[1]-=1
            elif route[i]=='E':
                pos[0]+=1
            elif route[i]=='W':
                pos[0]-=1
            else :
                print('Error: Invalid direction') 
        return coords,ind

"""Main function to continually plot routes till asked to stop"""
def Main():
    filename=input('Enter the next route instructions file, or enter STOP to finish:')
    while filename !='STOP':        
        grid=GridPlotter(12)
        c,ind=getCoords(filename)
        if ind == False :
            print('\nGrid Plot:\n')
            grid.plot(c)
            print('\nCoordinates:')
            [print(x) for x in c]
        elif ind == True:
            print("\nError: Route is outside the grid\n")
        filename=input('Enter the next route instructions file, or enter STOP to finish:')

Main()