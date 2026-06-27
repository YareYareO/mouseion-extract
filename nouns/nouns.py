from pathlib import Path
import pandas as pd
import os


def main():
    os.chdir("/home/eray")
    os.chdir(os.getcwd()+"/Schreibtisch/mouseion-extract/nouns")

    in_path = Path("data_noun.txt")
    out_path = Path("../sql_scripts/noun_inserts.sql")
    lemma_path = Path("lemmas.csv")

    insert_lines = []
    iteration = 0

    lemmas = pd.read_csv(lemma_path, index_col="id").dropna()
    lemmas = lemmas.drop_duplicates("lemma")
    lemmas = lemmas.set_index("lemma").to_dict()["lex"]


    with in_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # skip empty 
                continue

            parts = line.split()
            if len(parts) < 5:
                continue

            child_id = parts[0]
            label = parts[4]

            if label.find("'") >= 0:
                continue

            parent_ids = []
            skip = False
            count = 15
            for i, tok in enumerate(parts[7:]):
                if skip == True:
                    skip = False
                    continue
                if tok == "@":
                    parent_ids.append(parts[i + 8])  # 8 wegen 1+7, 7 wegen enumerates
                    count = 4
                    skip = True
                count -= 1
                if count == 0:
                    break

            lemma_type = lemmas.get(label)
            if not lemma_type:
                lemma_type = -1

            if not parent_ids:
                # write at least one INSERT even if no parent found
                insert_lines.append(
                    f"INSERT INTO noun (noun_id, label, lemma_type, parent_id) VALUES ({child_id}, '{label}', {lemma_type}, NULL);"
                )
            else:
                for pid in parent_ids:
                    insert_lines.append(
                        f"INSERT INTO noun (noun_id, label, lemma_type, parent_id) VALUES ({child_id}, '{label}', {lemma_type}, {pid});"
                    )
            if iteration % 1000 == 0:
                print(iteration, "\r")
            iteration += 1
        

    out_path.write_text("\n".join(insert_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(insert_lines)} INSERT statements to {out_path}")

if __name__ == "__main__":
    main()