MagicaVoxel .ply to Minecraft .mcfunction converter
---------------------------------------------------

It works with Ply-Files. To export your MagicaVoxel-creation as a *.*ply-File you can just select "Export" (right bottom of the screen) and "Point". 

Put the Ply-File(s) into the "INPUT"-folder. Run (Below I explain how to run Pythonfiles). Get converted file(s) from "OUTPUT"-folder.

To paste the *.*mcfunction-Files in Minecraft you have to put them into a datapack into your world's folder (I explain below). 

In the script's header you can adapt 2 Settings before running. It's commented in the script.



COLOUR PALETTE:
For existing Magica-Projects the script can (try to) match Macgica's colours to MC's sixteen concrete blocks by just selecting the nearest matching block from the "colourlist.txt". 

You can mod that if you want other blocks, even special blocks like glass or tnt. Add the special block to colourlist.txt, give it a unique R G B value, and paint with that Colour in MagicaVoxel to place that block.

For new Magica-Projects to paint from ground up you can import ColourPalette.png into Magica.



RUNNING PYTHON SCRIPTS
To run this python script you need Python installed. Linux often already has it preinstalled. A python editor like Thonny makes it even more comfy to run Python scripts but you can also run python scrips just by command line. 



RUNNING PYTHON FROM Command Line interface (CLI)
You have to open the CLI in the folder of the script. It's tedious to navigate in the CLI but you can use explorer and directly open CLI in the Script's folder (Windows: Enter "cmd" into file explorer's address bar / Linux: F4). There paste:

"python3 PlyToMcfunction.py"

or

„py PlyToMcfunction.py„

In Linux you have to add "sudo" before for Admin rights.

If dependencies are missing, you can install them with easily with PIP:

"pip install nameofdependency". 

If PIP (the PackageInstaller) is not installed, install PIP first ( https://pypi.org/project/pip/ )

 

WORKING WITH DATAPACKS:
Here's an empty datapack with correct file structure you can use:
https://drive.google.com/file/d/1EIj7ek9I4-YcCS7QhdGnuSUrlGROOPmV/view McFunctions go into the deepest folder called "functions" folder. Maybe you'd have to adapt the pack.mcmeta file to your Minecraft's version. For example MC1.16.1 has the packmcmeta-Number 5. For a list: https://minecraft.fandom.com/wiki/Pack_format
