    #SETTINGS:

    #you can place the spawned object to: Northwest, Northeast, Southwest or Southeast of you
    # NW, NE, SW, SE
    # Standard is NW (script choses NW if you don't enter sth else or if you mispell it)
wheretoplaceit = "SW"

    #normally 11 first lines of Magiva-PLY-Files are the header. So >11 skips this. I dont know if its always 11. Here you could adapt it           
linesofheader = 11




from pathlib import Path
import os
directory = str("INPUT")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".ply") or filename.endswith(".PLY"): 
        
 





        x = 999999999999
        y = 999999999999
        x = 999999999999
        f = "notassigned"
        row = 0
        outputfile = []


        dateiname = os.path.join(directory, filename)
        dateiname2 = "OUTPUT/" + str.lower(Path(filename).stem) + '.mcfunction'

        #COLOURMATCH
        colourlist = "colourlist.txt"
        #COLOURMATCH


        file = open(dateiname, "r")
        linien = file.readlines()


        #COLOURMATCH
        file2 = open(colourlist, "r")
        referencecolours = file2.readlines()
        #COLOURMATCH

        for linie in linien:
         row = row + 1

         if row > linesofheader:   #normally 11 first lines of Magiva-PLY-Files are the header. So >11 skips this. I dont know if its always 11. Here you could adapt it
             

             x = linie.split()[0] 
             y = linie.split()[1] 
             z = linie.split()[2] 
             #colourcode = linie.split()[3] + linie.split()[4] + linie.split()[5]
             
             
             #COLOURMATCH
             
             
             R = linie.split()[3]
             G = linie.split()[4]
             B = linie.split()[5]
             lowestdifference = 765 #highest possible euclidian difference between two RGB values (three times 255) 
             colourcode = "white_concrete" # just as a standard colour for it not to be empty - will be reassigned to other colour by script below
             
             for refcolour in referencecolours:

                 Rref = refcolour.split()[0] 
                 Gref = refcolour.split()[1] 
                 Bref = refcolour.split()[2] 
                 refcolourcode = refcolour.split()[3]
                 
                 momentdifferenceR = abs(int(R) - int(Rref))
                 momentdifferenceG = abs(int(G) - int(Gref))
                 momentdifferenceB = abs(int(B) - int(Bref))

                 momentdifferencetot = momentdifferenceR + momentdifferenceG + momentdifferenceB



                 #print(momentdifferencetot)
                # print(R)
                # print(G)
                 #print(B)
                 #print(Rref)
                 #print(Gref)
                # print(Bref)
                # print(momentdifferenceR)
                # print(momentdifferenceG)
                # print(momentdifferenceB)
                 if momentdifferencetot <= lowestdifference:
                     colourcode = refcolourcode
                     lowestdifference = momentdifferencetot
                     #print(colourcode)
                 
          
                 
            
             #COLOURMATCH       
                    
             #in the following line we swap z and y (xzy - normally its xyz in MC)
             #but if we dont do this, the model will be rotated 90 the wrong way (around an axis called x in MagicaVoxel strangely)       
             setblockrow = "setblock " + x + " " + z + " " + y + " " + colourcode
             #print(setblockrow)
             
        #     print("setblock " + x + " " + y + " " + z + " " + colourcode)
             #print(setblockrow)
             outputfile.append(setblockrow + "\n")
             
             
        file.close()
        file = open(dateiname2, "w")
        file.writelines(outputfile)
        file.close()
         
        print("half of momentary file processed. now making coords relative") 
         #chunkstoload = ("forceload add " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\n") 

         
         
         #new_lines.append(forceloadremoveall)
          
          
          
         #filenames have to be written lowercase
        #minecraft cannot execute .mcfunction files with uppercase filetitles

        #Turns coords into relative coords (relative to players position)
        #and
        #corrects the heigth so no block can be under your pos (the lowest block will spawn on player's height)

         


        filenumber = 1
        detectlowesty = 0
        detectlowestz = 0
        detecthighestz = 0
        detectlowestx = 0
        detecthighestx = 0
        outputfile2 = []


        file = open(dateiname2, "r")
        linien = file.readlines()

        for linie in linien:
             
             y = linie.split()[2] 
             
             if int(y) < int(detectlowesty):
                  detectlowesty = y
                  
             z = linie.split()[3] 
             
             if int(z) < int(detectlowestz):
                  detectlowestz = z
                  
             if int(z) > int(detecthighestz):
                  detecthighestz = z
                  
         
         
             x = linie.split()[1] 
             
             if int(x) < int(detectlowestx):
                  detectlowestx = x
                  
             if int(x) > int(detecthighestx):
                  detecthighestx = x
         
          
        print("the block with the lowest height coord is " + str(detectlowesty) + " blocks deep")     
        print("the block with the lowest z coord is " + str(detectlowestz))     
        print("the block with the highest z coord is " + str(detecthighestz))     

        print("the block with the lowest x coord is " + str(detectlowestx))     
        print("the block with the highest x coord is " + str(detecthighestx))     
             
             
             
        difference = int(detecthighestz) - int(detectlowestz)
        print(difference)
        compensatezoffset = difference     
             
             
        differencex = int(detecthighestx) - int(detectlowestx)
        print(differencex)
        compensatexoffset = differencex / 2     
             
         
         
         
        if int(detectlowesty) < 0:
            
            detectlowestypos = int(detectlowesty) - (int(detectlowesty) + int(detectlowesty))

        else: 

            detectlowestypos = detectlowesty
            
            
        for linie in linien:
            
            yint = int(linie.split()[2])
            zint = int(linie.split()[3])
            xint = int(linie.split()[1])
            
            z = zint - int(compensatezoffset / 2) 
            y = yint + int(detectlowestypos)
            x = xint - int(compensatexoffset)
            
            if wheretoplaceit == "NE":
                z = zint - int(compensatezoffset / 2) 
                y = yint + int(detectlowestypos)
                x = xint + int(compensatexoffset)
            
            if wheretoplaceit == "SE":
                z = zint + int(compensatezoffset / 2) 
                y = yint + int(detectlowestypos)
                x = xint + int(compensatexoffset)
            
            if wheretoplaceit == "SW":
                z = zint + int(compensatezoffset / 2)  
                y = yint + int(detectlowestypos)
                x = xint - int(compensatexoffset)
            
            
            
            color = linie.split()[4]
            
            correctedline = "setblock ~" + str(x) + " ~" + str(y) + " ~" + str(z) + " " + color
            #print(correctedline)
            
            outputfile2.append(correctedline + "\n")
            
               
             
             
        file.close()
        file = open(dateiname2, "w")
        file.writelines(outputfile2)
        file.close()
         
        print("io")
        print(compensatexoffset)
         #chunkstoload = ("forceload add " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\n") 

         
         
         #new_lines.append(forceloadremoveall)
          
        continue
    else:
        continue
        
        
        





     







