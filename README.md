# Authors and Affiliations Formatter

This Streamlit app (https://aut-formatter.streamlit.app/) allows you to upload a TSV file containing author details, processes the data, and generates an HTML-formatted list of authors with their corresponding affiliations. The output is displayed directly on the app page with proper superscripted affiliation numbers.

## Features
- Loads a built-in example on startup so you can see the expected format immediately.
- Upload a `.tsv` file to replace the example with your own data.
- Preview and edit the data in an interactive table before generating output — rows can be added or deleted.
- Automatically deduplicates affiliations and assigns sequential superscript numbers.
- Generates an HTML snippet ready to paste into a manuscript.

## Prerequisites
- Python 3.x
- Streamlit
- Pandas

## TSV format

The file must be tab-separated with these columns (add more `Affiliation` columns as needed, numbered sequentially):

| Order | First Name | Middle Name | Surname | Affiliation1 | Affiliation2 |
|-------|------------|-------------|---------|--------------|--------------|

A `sample_input.tsv` is included in the repository as a reference.

## Installation (if you want to run locally)

1. Clone the repository:

```bash
git clone https://github.com/wilhan-nunes/authors-affiliations-formatter.git
cd authors-affiliations-formatter
```

2. Install dependencies:

```bash
pip install streamlit pandas
```

3. Run the app:

```bash
streamlit run app.py
```
