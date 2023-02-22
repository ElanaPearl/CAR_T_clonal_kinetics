import GEOparse
import pandas as pd

gse = GEOparse.get_GEO(geo="GSE125881", destdir="geo_data/")
meta_data = []
for gsm_name, gsm in gse.gsms.items():
    gsm_info = [gsm_name]
    meta = gsm.metadata.get("characteristics_ch1")
    gsm_info.extend([entry.split(": ")[-1] for entry in meta])
    meta_data.append(gsm_info)

meta_df = pd.DataFrame(
    meta_data,
    columns=[
        "gsm_name",
        "id_in_expmatrix",
        "patient_id",
        "disease_state",
        "time_point",
        "time_point_type",
    ],
)
meta_df.to_csv("geo_metadata.csv", index=False)