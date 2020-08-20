import scipy.stats
import statsmodels.stats.multitest

import pandas as pd
import numpy as np


###############################################################################
# Set Pandas options
###############################################################################

#pd.set_option("display.max_rows", None, "display.max_columns", None)


###############################################################################
# Constants
###############################################################################
PHYLUM_CO_LIST = [
    "phylum_Actinobacteria",
    "phylum_Bacteroidetes",
    "phylum_Firmicutes",
    "phylum_Proteobacteria",
    "phylum_Verrucomicrobia",
    "phylum_unclassified_Bacteria",
]
CLASS_CO_LIST = [
    "class_Actinobacteria",
    "class_Bacilli",
    "class_Bacteroidia",
    "class_Betaproteobacteria",
    "class_Clostridia",
    "class_Deltaproteobacteria",
    "class_Erysipelotrichia",
    "class_Gammaproteobacteria",
    "class_Negativicutes",
    "class_Verrucomicrobiae",
    "class_unclassified_Bacteria",
    "class_unclassified_Firmicutes",
]
ORDER_CO_LIST = [
    "order_Bacteroidales",
    "order_Burkholderiales",
    "order_Clostridiales",
    "order_Coriobacteriales",
    "order_Desulfovibrionales",
    "order_Enterobacteriales",
    "order_Erysipelotrichales",
    "order_Lactobacillales",
    "order_Selenomonadales",
    "order_Verrucomicrobiales",
    "order_unclassified_Bacteria",
    "order_unclassified_Firmicutes",
]
FAMILY_CO_LIST = [
    "family_Acidaminococcaceae",
    "family_Bacteroidaceae",
    "family_Clostridiaceae.1",
    "family_Clostridiales_Incertae.Sedis.XIII",
    "family_Coriobacteriaceae",
    "family_Desulfovibrionaceae",
    "family_Enterobacteriaceae",
    "family_Erysipelotrichaceae",
    "family_Lachnospiraceae",
    "family_Peptostreptococcaceae",
    "family_Porphyromonadaceae",
    "family_Prevotellaceae",
    "family_Rikenellaceae",
    "family_Ruminococcaceae",
    "family_Streptococcaceae",
    "family_Sutterellaceae",
    "family_Veillonellaceae",
    "family_Verrucomicrobiaceae",
    "family_unclassified_Bacteria",
    "family_unclassified_Clostridiales",
    "family_unclassified_Firmicutes",
]
GENUS_CO_LIST = [
    "genus_Akkermansia",
    "genus_Alistipes",
    "genus_Anaerotruncus",
    "genus_Anaerovorax",
    "genus_Bacteroides",
    "genus_Barnesiella",
    "genus_Bilophila",
    "genus_Blautia",
    "genus_Butyricicoccus",
    "genus_Butyricimonas",
    "genus_Clostridium.IV",
    "genus_Clostridium.XI",
    "genus_Clostridium.XVIII",
    "genus_Clostridium.XlVa",
    "genus_Clostridium.XlVb",
    "genus_Clostridium.sensu.stricto",
    "genus_Collinsella",
    "genus_Coprococcus",
    "genus_Dorea",
    "genus_Eggerthella",
    "genus_Erysipelotrichaceae_incertae_sedis",
    "genus_Faecalibacterium",
    "genus_Flavonifractor",
    "genus_Holdemania",
    "genus_Lachnospiracea_incertae_sedis",
    "genus_Odoribacter",
    "genus_Oscillibacter",
    "genus_Parabacteroides",
    "genus_Parasutterella",
    "genus_Phascolarctobacterium",
    "genus_Prevotella",
    "genus_Pseudoflavonifractor",
    "genus_Roseburia",
    "genus_Ruminococcus",
    "genus_Streptococcus",
    "genus_Veillonella",
    "genus_unclassified_Bacteria",
    "genus_unclassified_Clostridiales",
    "genus_unclassified_Clostridiales_Incertae.Sedis.XIII",
    "genus_unclassified_Coriobacteriaceae",
    "genus_unclassified_Erysipelotrichaceae",
    "genus_unclassified_Firmicutes",
    "genus_unclassified_Lachnospiraceae",
    "genus_unclassified_Porphyromonadaceae",
    "genus_unclassified_Ruminococcaceae",
]
CORR_COLUMS=["X1","X2","Correlation"]
CORR_METHOD = "pearson"
INPUT = "/app/data/gut_16s_abundance.csv"
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
    csv_names = ['phylum.csv', 'class.csv', 'order.csv', 'family.csv', 'genus.csv']

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
    for df in df_list:
        index = 0
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

        df_corr_true.to_csv(csv_names[index])
        index = index + 1

if __name__ == "__main__":
    main()