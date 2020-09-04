import scipy.stats
import statsmodels.stats.multitest

import pandas as pd
import numpy as np

from igraph import *

###############################################################################
# Set Pandas options
###############################################################################

#pd.set_option("display.max_rows", None, "display.max_columns", None)


###############################################################################
# Constants
###############################################################################

PHYLUM_CO_LIST = [
    "phylum_Euryarchaeota",
    "phylum_Bacteroidetes",
    "phylum_Proteobacteria",
    "phylum_Planctomycetes",
    "phylum_Verrucomicrobia",
    "phylum_Spirochaetes",
    "phylum_Actinobacteria",
    "phylum_Firmicutes",
]
CLASS_CO_LIST = [
    "class_Methanobacteria",
    "class_Thermoplasmata",
    "class_Bacteroidia",
    "class_Flavobacteriia",
    "class_Sphingobacteriia",
    "class_Betaproteobacteria",
    "class_Epsilonproteobacteria",
    "class_Gammaproteobacteria",
    "class_Planctomycetia",
    "class_Verrucomicrobiae",
    "class_Spirochaetia",
    "class_Actinobacteria",
    "class_Coriobacteriia",
    "class_Bacilli",
    "class_Clostridia",
    "class_Erysipelotrichia",
    "class_Negativicutes",
    "class_Tissierellia",
]
ORDER_CO_LIST = [
    "order_Methanobacteriales",
    "order_Methanomassiliicoccales",
    "order_Bacteroidales",
    "order_Flavobacteriales",
    "order_Sphingobacteriales",
    "order_Burkholderiales",
    "order_Campylobacterales",
    "order_Enterobacterales",
    "order_Pasteurellales",
    "order_Planctomycetales",
    "order_Verrucomicrobiales",
    "order_Spirochaetales",
    "order_Bifidobacteriales",
    "order_Propionibacteriales",
    "order_Eggerthellales",
    "order_Bacillales",
    "order_Lactobacillales",
    "order_Clostridiales",
    "order_Erysipelotrichales",
    "order_Acidaminococcales",
    "order_Selenomonadales",
    "order_Veillonellales",
    "order_Tissierellales",
]
FAMILY_CO_LIST = [
    "family_Methanobacteriaceae",
    "family_Methanomassiliicoccaceae",
    "family_Bacteroidaceae",
    "family_Barnesiellaceae",
    "family_Odoribacteraceae",
    "family_Porphyromonadaceae",
    "family_Prevotellaceae",
    "family_Rikenellaceae",
    "family_Tannerellaceae",
    "family_Flavobacteriaceae",
    "family_Sphingobacteriaceae",
    "family_Comamonadaceae",
    "family_Campylobacteraceae",
    "family_Enterobacteriaceae",
    "family_Pasteurellaceae",
    "family_Planctomycetaceae",
    "family_Akkermansiaceae",
    "family_Spirochaetaceae",
    "family_Bifidobacteriaceae",
    "family_Propionibacteriaceae",
    "family_Eggerthellaceae",
    "family_Bacillaceae",
    "family_Paenibacillaceae",
    "family_Enterococcaceae",
    "family_Lactobacillaceae",
    "family_Leuconostocaceae",
    "family_Streptococcaceae",
    "family_Eubacteriaceae",
    "family_Lachnospiraceae",
    "family_Oscillospiraceae",
    "family_Peptostreptococcaceae",
    "family_Ruminococcaceae",
    "family_unclassified_Clostridiales",
    "family_Erysipelotrichaceae",
    "family_Acidaminococcaceae",
    "family_Selenomonadaceae",
    "family_Veillonellaceae",
    "family_Peptoniphilaceae",
]
GENUS_CO_LIST = [
    "genus_Methanobrevibacter",
    "genus_Methanomassiliicoccus",
    "genus_Bacteroides",
    "genus_Barnesiella",
    "genus_Odoribacter",
    "genus_Fermentimonas",
    "genus_Porphyromonas",
    "genus_Prevotella",
    "genus_Alistipes",
    "genus_Parabacteroides",
    "genus_Tannerella",
    "genus_Ornithobacterium",
    "genus_Sphingobacterium",
    "genus_Acidovorax",
    "genus_Campylobacter",
    "genus_Citrobacter",
    "genus_Escherichia",
    "genus_Klebsiella",
    "genus_Raoultella",
    "genus_Haemophilus",
    "genus_Rubinisphaera",
    "genus_Akkermansia",
    "genus_Treponema",
    "genus_Bifidobacterium",
    "genus_Gardnerella",
    "genus_Cutibacterium",
    "genus_Adlercreutzia",
    "genus_Eggerthella",
    "genus_Gordonibacter",
    "genus_Bacillus",
    "genus_Paenibacillus",
    "genus_Enterococcus",
    "genus_Lactobacillus",
    "genus_Leuconostoc",
    "genus_Lactococcus",
    "genus_Streptococcus",
    "genus_Eubacterium",
    "genus_Anaerostipes",
    "genus_Blautia",
    "genus_Coprococcus",
    "genus_Lachnoclostridium",
    "genus_Roseburia",
    "genus_unclassified_Lachnospiraceae",
    "genus_Oscillibacter",
    "genus_Clostridioides",
    "genus_Paeniclostridium",
    "genus_Ethanoligenens",
    "genus_Faecalibacterium",
    "genus_Mageeibacillus",
    "genus_Ruminiclostridium",
    "genus_Ruminococcus",
    "genus_Intestinimonas",
    "genus_unclassified_Clostridiales_(miscellaneous)",
    "genus_Faecalitalea",
    "genus_Acidaminococcus",
    "genus_Megamonas",
    "genus_Veillonella",
    "genus_Anaerococcus",
    "genus_Parvimonas",
]
CORR_COLUMS=["X1","X2","Correlation"]
CORR_METHOD = "pearson"
INPUT = "/app/data/healthy_human_abundance.csv"
###############################################################################
# Functions
###############################################################################


def main():

    # Create Dataframes
    phylum_df = pd.read_csv(INPUT, usecols=PHYLUM_CO_LIST)
    class_df = pd.read_csv(INPUT, usecols=CLASS_CO_LIST)
    order_df = pd.read_csv(INPUT, usecols=ORDER_CO_LIST)
    family_df = pd.read_csv(INPUT, usecols=FAMILY_CO_LIST)
    genus_df = pd.read_csv(INPUT, usecols=GENUS_CO_LIST)

    df_list = [phylum_df, class_df, order_df, family_df, genus_df]

    csv_fileNames = ["healthy_phylum.csv", "healthy_class.csv", "healthy_order.csv", "healthy_family.csv", "healthy_genus.csv"]
    csv_headerNames = ["X1", "X2", "Correlation"]

    image_names = ["healthy_phylum.png", "healthy_class.png", "healthy_order.png", "healthy_family.png", "healthy_genus.png"]

    for df in df_list:
        print(df.shape)

    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html 

    # Length of the dataframe, since the source is the same for each dataframe the number of rows is the same
    n = phylum_df.shape[0]

    dist = scipy.stats.beta(n/2 - 1, n/2 - 1, loc=-1, scale=2)

    # Test value to verify
    # print(scipy.stats.pearsonr(phylum_df['phylum_Actinobacteria'].tolist(),phylum_df['phylum_Bacteroidetes'].tolist()))

    print(n)

    # Correlation test for each data frame
    index = 0
    for df in df_list:
        df_corr = df.corr(method=CORR_METHOD).stack().reset_index()

        # Use to name columns in new dataframe
        df_corr.columns = CORR_COLUMS

        # P value formula from documentation in scipy
        df_corr['P_Value'] = 2*dist.cdf(-abs(df_corr['Correlation']))

        # Adjusted P value and Rejection (true for hypothesis that can be rejected for given alpha)
        adjusted_pvalue = []
        adjusted_pvalue = statsmodels.stats.multitest.multipletests(df_corr['P_Value'], alpha=0.05, method='bonferroni', is_sorted=False, returnsorted=False)

        df_corr['Adjusted_P_Value'] = adjusted_pvalue[1]
        df_corr['Rejection'] = adjusted_pvalue[0]

        reject_true = df_corr['Rejection'] == True
        df_corr_true = df_corr[reject_true]

        df_corr_true.to_csv(str(csv_fileNames[index]), columns=csv_headerNames, index=False, sep='\t', header=None)
    
        g = Graph.Read_Ncol(str(csv_fileNames[index]), directed=False)
        print(g)
        print("\nSummary\n")
        print(g.summary())
        print("\nVertex Betweenness\n")
        betw = g.betweenness()
        for v in g.vs:
            print(v["name"], betw[v.index])
        print("\nEdge Betweenness\n")
        print(g.edge_betweenness())
        print("\nOmega\n")
        print(g.omega())
        print("\nClusters\n")
        print(g.clusters())
        print("\nDiameter\n")
        print(g.diameter())
        print("\nTransitivity Undirected\n")
        print(g.transitivity_undirected())

        # This section is commented out due to issues that I am trying to resolve. Images for the networks have
        # provided in the GitHub repo.
        """
        layout = g.layout("kk")
        g.vs["label"] = g.vs["name"]
        plot(g, image_names[index], layout = layout, bbox = (2560, 1440), margin = 20)

        index = index + 1
        """
        
if __name__ == "__main__":
    main()