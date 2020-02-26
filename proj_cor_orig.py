import arcpy, sys, string, os, time, datetime, shutil, traceback
from arcpy import env

ws=raw_input("Please enter directory: ")

logpath = raw_input("please enter logpath: ")


scriptName = sys.argv[0]
logName = sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1][0:-3]
logfile = logpath + "\\" + logName + ".log"

outfile = open(logfile,'a')

outfile.write('\n' + ws  + '\n' + scriptName + " ----------------------------------------" '\n')




env.workspace = ws

rasters = arcpy.ListRasters()


dsc = arcpy.Describe(r'R:\Image_ClarkCounty\2017\ClarkCounty_Collection\122\o12204.tif')
coord_sys = dsc.spatialReference

for raster in rasters:
    print "correcting projected coordinate system of " + str(raster)
    timeYearMonDay = datetime.date.today()
    timeHour = time.localtime()[3]
    timeMin = time.localtime()[4]
    outfile = open(logfile,'a')  
    outfile.write(raster + " " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n')

    try:
        arcpy.DefineProjection_management(raster, coord_sys)
    except:
        
        print "Process: Failed for: " + raster
        print arcpy.GetMessages(2)
        ouch = arcpy.GetMessages(2)
        outfile.write(ouch + '\n' )        
        outfile.write("Process: Failed for: " + raster + " " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )



outfile.close()

    
# create a tuple of local time data
timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]


print "Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin)
outfile= open(logfile,'a')
outfile.write("Process Complete "  + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )
outfile.close()
