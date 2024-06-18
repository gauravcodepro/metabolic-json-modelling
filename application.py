#! usr/bin/env python3
# Author Gaurav
# Universitat Potsdam
# Date 2024-6-18
# application coded in 1 hour. I do time specific code writing. 
import streamlit as st
import pandas as pd
import json
import streamlit.components.v1 as components
st.set_page_config(
                 page_title="Metabolic Loader",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width = 100)
st.header("Analyzing metabolic models json")
st.subheader("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam, Germany")
help = st.button("Please show the helpfile")
if help:
    st.write("This is a quick application for the searching of the metabolic models json schema")
    st.write("You can search the json either through the metabolite id, compartment, reactions, genes")
    st.write("This will also give you the upperbound and the lower bound")

uploadjson = st.text_input("please choose a json file:")
inputid = st.text_input("Please enter the id of the metabolic pathway:")
inputbigg = st.text_input("Please enter the bigg ID:")
inputgenes = st.text_input("Please enter the genes:")
inputcompartments = st.text_input("Please enter the compartments:")
fecthreactionpathway = st.text_input("Please enter the reaction pathway")
fetchreactions = st.button("fetch all the biochemical reactions")
fetchreactionids = st.button("fetch all the biochemical reactions ids")
fetchidsgene_reaction_rule = st.button("fetch all the gpr rules")
if uploadjson is not None and inputid:
    readjson = json.load(open(uploadjson))
    jsonkeys = readjson.keys()
    jsonvalues = readjson.values()
    metabolites = readjson["metabolites"]
    reactions = readjson["reactions"]
    genes = readjson["genes"]
    ids = readjson["id"]
    compartments = readjson["compartments"]
    searchid = [i for i in readjson["metabolites"] if i["id"] == inputid]
    st.write("The observed id and the associated metabolites and the compartment are:")
    st.write(searchid)
if uploadjson is not None and inputcompartments:
    readjson = json.load(open(uploadjson))
    jsonkeys = readjson.keys()
    jsonvalues = readjson.values()
    metabolites = readjson["metabolites"]
    reactions = readjson["reactions"]
    genes = readjson["genes"]
    ids = readjson["id"]
    compartments = readjson["compartments"]
    searchcompartment = pd.DataFrame([i for i in readjson["metabolites"] if i["compartment"] == inputcompartments])
    st.write("The observed id and the associated metabolites and the compartment are:")
    st.write(searchcompartment)
if uploadjson is not None and inputgenes:
    readjson = json.load(open(uploadjson))
    jsonkeys = readjson.keys()
    jsonvalues = readjson.values()
    metabolites = readjson["metabolites"]
    reactions = readjson["reactions"]
    genes = readjson["genes"]
    ids = readjson["id"]
    compartments = readjson["compartments"]
    searchgenes = pd.DataFrame([i for i in readjson["metabolites"] if inputgenes in i["annotation"]["chebi"]])
    st.write("The observed id and the associated metabolites and the compartment are:")
    st.write(searchcompartment)
if uploadjson is not None and inputbigg:
    readjson = json.load(open(uploadjson))
    jsonkeys = readjson.keys()
    jsonvalues = readjson.values()
    metabolites = readjson["metabolites"]
    reactions = readjson["reactions"]
    genes = readjson["genes"]
    ids = readjson["id"]
    compartments = readjson["compartments"]
    searchbigg = pd.DataFrame([i["annotation"] for i in readjson["metabolites"] if inputbigg in i["annotation"]["bigg.metabolite"]])
    st.write("The observed id and the associated metabolites and the compartment are:")
    st.write(searchbigg)
if uploadjson and fetchreactions:
    st.write("These are the reactions present in the embedded JSON")
    readjson = json.load(open(uploadjson))
    reactions = pd.DataFrame([i["name"] for i in readjson["reactions"]])
    st.write(reactions)
if uploadjson and fetchreactionids:
    readjson = json.load(open(uploadjson))
    selectids = pd.DataFrame([i["id"] for i in readjson["reactions"]])
    st.write(selectids)
if uploadjson and fetchidsgene_reaction_rule:
    readjson = json.load(open(uploadjson))
    gprdata = pd.DataFrame([[i["id"],i["gene_reaction_rule"]] for i in readjson["reactions"]])
    st.write(gprdata)
if uploadjson and fecthreactionpathway:
    readjson = json.load(open(uploadjson))
    getreactions = pd.DataFrame([i for i in readjson["reactions"]if i["name"] == fecthreactionpathway])
    st.write(getreactions)
