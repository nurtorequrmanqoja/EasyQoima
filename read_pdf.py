import pandas as pd
import tabula

file_path = 'order2.pdf'
dfs = []
combined_df0 = pd.DataFrame
pages = tabula.read_pdf(file_path, pages='all')
for page in pages:
    dfs.append(page)
    # print(page.to_string())
    # print('---------------------------------------------------------')
combined_df = pd.concat(dfs, ignore_index=True, sort=False)
# df1 = tabula.read_pdf_with_template(file_path, multiple_tables=True)
# for i in df1[0].index[3:]:
#     id_book = df1[0].values[i][1]

# for i in combined_df.index:
#     print(combined_df.values)


print(combined_df.to_string())