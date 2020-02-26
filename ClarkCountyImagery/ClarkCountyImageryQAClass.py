import sys, string, os, time, datetime, shutil, traceback, arcpy
from arcpy import env
from LogClass.LogFile_Class import LogFile_Class

ws = input(" Enter the workspace path: ")
output = input(" Enter output directory to copy images to: ")


if os.path.exists(ws) == False:
    print("Directory: " + ws + " does not exist... creating the directory here: C:\\" + ws.replace(" ", ""))
    os.mkdir("C:\\" + ws.replace(" ", "_"))
    print("The directory has been created")
    


env.workspace = ws
arcpy.env.overwriteOutput = True
arcpy.env.pyramid = "None"
arcpy.env.rasterStatistics = "None"

LogFile = LogFile_Class()


class CopyImages:
    
    
    def __init__(self):
        pass

    def copy_images(self):
        fcs = arcpy.ListRasters()

        for fc in fcs:
            if len(fc) == 10:
                name = fc[1:4]
            elif len(fc) == 11:
                name = fc[1:5]

            tilename = fc[0:-4]

            LogFile.append_start_status()

            outputPath = output

            movedRas = os.path.join(HiSpeedPath, name, fc)
            PyrFile = os.path.join(ws, tilename, '.rrd')
            StatFile = os.path.join(ws, tilename, '.aux')
            TfwFile = os.path.join(ws, tilename, '.tfw')
            tifFile = os.path.join(ws, tilename, '.tif')
            newPath = os.path.join(outputPath, name)

            try:
                print(fc)
                is os.path.exists(newPath) == False:
                    os.mkdir(newPath)

                    try:
                        shutil.copy(tifFile, newPath)
                        shutil.copy(PyrFile, newPath)
                        shutil.copy(StatFile, newPath)
                        shutil.copy(TfwFile, newPath)

                    except:
                        
                        LogFile.failed_status()

                elif arcpy.Exists(movedRas):
                    LogFile

        except:
            ouch = arcpy.GetMessages(2)
            LogFile.failed_status()

        LogFile.close()
    LogFile.get_end_time()
                        
                        

            
