import base64
from github import Github
import streamlit as st

token = "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"
repository = "1masa0ka/CR"
fileName = "CR_date.csv"

g = Github(token)
repo = g.get_repo(repository)
contents = repo.get_contents(fileName)
content = base64.b64decode(contents.content)

st.write('git')
with open("copy_" + fileName, mode="wb") as f:
    f.write(content)
