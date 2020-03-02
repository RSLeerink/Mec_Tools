import pandas as pd
import streamlit as st

#FilePath = 'D:/Codeing/Python/TestingSpace/Mec_Tools/Mec_Tools/Beam_Property_Tool/Profiles_S235_Eurocode_3.xlsx'
#ProfileType = 'HEB'
#ProfielSize = '200'

def Profile_Select(FilePath,ProfileType,ProfielSize):
    if ProfileType == 'HEB':
        #FilePath = FilePath+'/HEB_Profiles_S235_Eurocode_3.xlsx'    
        SheetName = 'HEB_Profiles_S235_Eurocode_3'
    elif ProfileType == 'IPE':
        SheetName = 'IPE_Profiles_S235_Eurocode_3'

    df = pd.read_excel(FilePath,sheet_name=SheetName, index_col=0,header=1)  

    ProfileName = ProfileType + ProfielSize
    Profile_df = df.loc[ProfileName]

    Profile_df[10] = Profile_df[10] * 10**6 #Second moment of area 
    Profile_df[12] = Profile_df[12] * 10**3 #Elastic section modulus 
    Profile_df[13] = Profile_df[13] * 10**3 #Plastic section modulus 

    Profile_df[14] = Profile_df[14] * 10**6 #Second moment of area 
    Profile_df[16] = Profile_df[16] * 10**3 #Elastic section modulus 
    Profile_df[17] = Profile_df[17] * 10**3 #Plastic section modulus

    Profile_df[18] = Profile_df[18] * 10**3 #Torsion constant	
    Profile_df[19] = Profile_df[19] * 10**3 #Torsion modulus	
    Profile_df[20] = Profile_df[20] * 10**6 #Warping constant	 
    Profile_df[21] = Profile_df[21] * 10**3 #Warping modulus	

    

    Profile_dimensions = Profile_df[0:2]
    Area_properties = Profile_df[2:10]
    Inertia_properties_about_major_axis_yy = Profile_df[10:14]
    Inertia_properties_about_minor_axis_zz = Profile_df[14:18]
    Torsional_and_warping_properties = Profile_df[18:22]
    Axial_force_and_shear_resistance = Profile_df[22:25]
    Bending_major_axis_yy	= Profile_df[25:27]
    Bending_minor_axis_zz = Profile_df[27:29]
    Buckling_curve	= Profile_df[29:31]
    Section_classification = Profile_df[31:33]

    Out_list = [Profile_df,
                Profile_dimensions,
                Area_properties,
                Inertia_properties_about_major_axis_yy,
                Inertia_properties_about_minor_axis_zz,
                Torsional_and_warping_properties,
                Axial_force_and_shear_resistance,
                Bending_major_axis_yy,
                Bending_minor_axis_zz,
                Buckling_curve,
                Section_classification]

    #print(Out_list)

    return Out_list

#Profile_Select(FilePath,ProfileType,ProfielSize)


#df.set_index('Profile')