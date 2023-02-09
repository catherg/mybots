from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color_name, color_string):

        self.depth  = 3

        #self.string1 = '<material name="Cyan">'
        self.string1 = '<material name="'+color_name+'">' 

        #self.string2 = '    <color rgba="0 1.0 1.0 1.0"/>'

        self.string2 = '    <color rgba="'+color_string+'"/>'

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
