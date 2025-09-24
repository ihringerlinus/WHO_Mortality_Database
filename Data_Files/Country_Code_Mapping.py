import pandas as pd

codes = pd.read_csv("../codes_Files/country_codes.csv", encoding="utf-8-sig")
mortality = pd.read_csv("Morticd10_part6.csv", encoding="utf-8-sig")
merged = mortality.merge(codes, left_on="Country", right_on="country", how="left")
merged["Country"] = merged["name"]
merged = merged.drop(columns=["country", "name"])
merged.to_csv("mortality_with_country_names.csv", index=False)