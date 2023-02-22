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
print("-----------------------------------------------------------")
print(
    f"{len(meta_df)} samples collected from {meta_df['patient_id'].nunique()} "
    + f"patients across {meta_df['time_point_type'].nunique()} time points"
)
print("Metadata:")
print(meta_df)
print("Saving metadata to geo_metadata.csv")
meta_df.to_csv("geo_metadata.csv", index=False)
