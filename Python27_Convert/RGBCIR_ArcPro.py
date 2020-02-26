import arcpy



aprx = arcpy.mp.ArcGISProject("CURRENT")
m=aprx.listMaps()[0]



source_layer = r"D:\Python27_Convert\o12603.tif.lyrx"
#source_layer = r"D:\Python27_Convert\Color\o17604_ne.tif.lyrx"

for lyr2 in m.listLayers():
    x = lyr2.name
    image = x[-3:]               
    if image == 'tif':
        arcpy.ApplySymbologyFromLayer_management(lyr2, source_layer)

        

