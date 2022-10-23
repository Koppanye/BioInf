import requests

resp = requests.get("https://rest.uniprot.org/uniprotkb/B5ZC00.fasta")
#print(resp.text)

s = "http://www.uniprot.org/uniprot/"
z = ".fasta"

with open("mprt_test_2", "r") as f:
    ids = f.readlines()
    for i in ids:
        html = s + str(i).strip() + z
        print(html)
        #resp = requests.get(html)
        #print(resp.text)