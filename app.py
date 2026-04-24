import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")


# Function to format authors and affiliations
def format_authors_affiliations(df):
    df.columns = df.columns.map(lambda x: x.lower().strip())
    authors = []
    affiliations_dict = {}
    affiliation_counter = 1
    total_affiliations = len([x for x in df.columns.to_list() if 'affiliation' in x]) + 1

    for _, row in df.iterrows():
        full_name = f"{row['first name']} {row['middle name'] if pd.notna(row['middle name']) else ''} {row['surname']}".strip()
        affiliations = [row[f'affiliation{i}'] for i in range(1, total_affiliations) if pd.notna(row[f'affiliation{i}'])]

        affiliation_indices = []
        for affiliation in affiliations:
            if affiliation not in affiliations_dict:
                affiliations_dict[affiliation] = affiliation_counter
                affiliation_counter += 1
            affiliation_indices.append(affiliations_dict[affiliation])

        authors.append(f"{full_name}<sup>{','.join(map(str, affiliation_indices))}</sup>")

    affiliation_list = [f"{num}. {aff}" for aff, num in sorted(affiliations_dict.items(), key=lambda item: item[1])]

    return authors, affiliation_list


# Function to create HTML content
def create_html_authors_file(authors, affiliations):
    html_content = """
    <html>
    <head>
        <title>Authors and Affiliations</title>
        <style>
            sup {{
                font-size: smaller;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 5px;
            }}
        </style>
    </head>
    <body>
        <h2>Authors</h2>
        <p>{authors_list}</p>
        <h2>Affiliations</h2>
        <ul>
        {affiliations_list}
        </ul>
    </body>
    </html>
    """
    authors_list = ', '.join([author for author in authors])
    # authors_list = ', '.join([f"{author[:-1]}<sup>{author[-1]}</sup>" for author in authors])
    affiliations_list = ''.join([f"<li><sup>{i.split('.', 1)[0]}</sup> {i.split('.', 1)[1]}</li>" for i in affiliations])
    html_content = html_content.format(authors_list=authors_list, affiliations_list=affiliations_list)
    return html_content

st.title("Authors and Affiliations Formatter")
st.write('The TSV should contain the following headers. Add as much affiliations as you need, numbering them sequentially.')
st.write('Version: 2026.04.24')

example_df = pd.read_csv("sample_input.tsv", sep='\t')
st.table(example_df)

uploaded_file = st.file_uploader("Choose a TSV file with author details", type="tsv")

active_file = uploaded_file if uploaded_file is not None else "sample_input.tsv"
df = pd.read_csv(active_file, sep='\t')

st.markdown("### Preview & Edit")
df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

authors_list, affiliations_list = format_authors_affiliations(df)

if st.button('Generate HTML'):
    html_content = create_html_authors_file(authors_list, affiliations_list)
    st.markdown("### Output:")
    st.markdown(html_content, unsafe_allow_html=True)
