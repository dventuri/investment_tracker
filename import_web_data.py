import json
site = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedSupplementCompany/eyJpc3N1aW5nQ29tcGFueSI6IklUVUIiLCJsYW5ndWFnZSI6InB0LWJyIn0="
with open("test.json") as f:
    data=json.load(f)
for provento in data[0]["cashDividends"]:
    print(provento)