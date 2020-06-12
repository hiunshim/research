# Copyright 2021, Hiun Shim, All rights reserved.

import csv
from itertools import zip_longest

def write_csv(npd_data, npd_weighted_data, zss_data, with_transformer):
    if with_transformer:
        with open("./../csv_files/with_transformer/npd.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(npd_data)
        with open("./../csv_files/with_transformer/npd_weighted.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(npd_weighted_data)
        with open("./../csv_files/with_transformer/zss.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(zss_data)
    else:
        with open("./../csv_files/without_transformer/npd.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(npd_data)
        with open("./../csv_files/without_transformer/npd_weighted.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(npd_weighted_data)
        with open("./../csv_files/without_transformer/zss.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Design_Data", "Ground_Data", "Transformer", "DesignMST_Ground", "GroundMST_Ground", "DesignMST_GroundMST"])
            writer.writerows(zss_data)

def polylines_csv(design_file_name, ground_file_name, transformer_id, designMST_polylines, groundMST_polylines, ground_polylines, with_transformer):
    if with_transformer:
        with open("./../csv_files/polylines/with_transformer/"+design_file_name+"_"+ground_file_name+".csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Transformer", "DesignMST_Polylines", "GroundMST_Polylines", "Ground_Polylines"])
            # writer.writerows([designMST_polylines, groundMST_polylines, ground_polylines])
            for l1, l2, l3 in zip_longest(designMST_polylines, groundMST_polylines, ground_polylines):
                writer.writerow([transformer_id, l1, l2, l3])
    else:
        with open("./../csv_files/polylines/without_transformer/"+design_file_name+"_"+ground_file_name+".csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Transformer", "DesignMST_Polylines", "GroundMST_Polylines", "Ground_Polylines"])
            # writer.writerows([designMST_polylines, groundMST_polylines, ground_polylines])
            for l1, l2, l3 in zip_longest(designMST_polylines, groundMST_polylines, ground_polylines):
                writer.writerow([transformer_id, l1, l2, l3])
