# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:18:55 2018 by nmtarr

Description: Query the GAP range data for a list of species in Partnership
for Gulf Coast Land Conservation priority areas.
"""
execfile("T:/Scripts/AppendPaths27.py")
import gapproduction as gp
import gapconfig as config
import pandas as pd
aoi = "T:/SmallProjects/PGCLC/pgclc.shp"
species = gp.gaprange.SppInAOI(AOIShp=aoi,
                                 hucShp=config.hucs,
                                 workDir="T:/SmallProjects/PGCLC/",
                                 origin=[1,2],
                                 season=[1,3,4],
                                 reproduction=[1,2,3],
                                 presence=[1])

df = pd.DataFrame(index=species)
df.index.name="gap_code"
df["scientific_name"] = [gp.gapdb.NameSci(x) for x in df.index]
df["common_name"] = [gp.gapdb.NameCommon(x) for x in df.index]
print(df)