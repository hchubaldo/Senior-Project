import pandas as pd
import numpy as np
import scipy.stats

#read_file = pd.read_csv (r'C:\Users\admin\Dropbox\Bioinformatics\Senior Project\gut_16s_abundance.txt')
#read_file.to_csv (r'C:\Users\admin\Dropbox\Bioinformatics\Senior Project\gut_16s_abundance.csv', index = None)

#temp = open("gut_16s_abundance.csv", "w")
#with open("gut_16s_abundance.txt") as x:
#    for line in x:
#        line = line.replace("\t", ",")
#        temp.write(line)
#temp.close()

phylum_coList = ['phylum_Actinobacteria', 'phylum_Bacteroidetes', 'phylum_Firmicutes', 'phylum_Proteobacteria',	'phylum_Verrucomicrobia', 'phylum_unclassified_Bacteria']
class_coList = ['class_Actinobacteria',	'class_Bacilli', 'class_Bacteroidia', 'class_Betaproteobacteria', 'class_Clostridia', 'class_Deltaproteobacteria', 'class_Erysipelotrichia', 'class_Gammaproteobacteria', 'class_Negativicutes', 'class_Verrucomicrobiae', 'class_unclassified_Bacteria', 'class_unclassified_Firmicutes']
order_coList = ['order_Bacteroidales', 'order_Burkholderiales',	'order_Clostridiales', 'order_Coriobacteriales', 'order_Desulfovibrionales', 'order_Enterobacteriales',	'order_Erysipelotrichales',	'order_Lactobacillales', 'order_Selenomonadales', 'order_Verrucomicrobiales', 'order_unclassified_Bacteria', 'order_unclassified_Firmicutes']
family_coList = ['family_Acidaminococcaceae', 'family_Bacteroidaceae', 'family_Clostridiaceae.1', 'family_Clostridiales_Incertae.Sedis.XIII', 'family_Coriobacteriaceae', 'family_Desulfovibrionaceae',	'family_Enterobacteriaceae', 'family_Erysipelotrichaceae', 'family_Lachnospiraceae', 'family_Peptostreptococcaceae', 'family_Porphyromonadaceae', 'family_Prevotellaceae', 'family_Rikenellaceae', 'family_Ruminococcaceae', 'family_Streptococcaceae', 'family_Sutterellaceae', 'family_Veillonellaceae', 'family_Verrucomicrobiaceae', 'family_unclassified_Bacteria', 'family_unclassified_Clostridiales', 'family_unclassified_Firmicutes']
genus_coList = ['genus_Akkermansia', 'genus_Alistipes', 'genus_Anaerotruncus', 'genus_Anaerovorax', 'genus_Bacteroides', 'genus_Barnesiella', 'genus_Bilophila', 'genus_Blautia', 'genus_Butyricicoccus', 'genus_Butyricimonas', 'genus_Clostridium.IV', 'genus_Clostridium.XI', 'genus_Clostridium.XVIII', 'genus_Clostridium.XlVa', 'genus_Clostridium.XlVb', 'genus_Clostridium.sensu.stricto', 'genus_Collinsella', 'genus_Coprococcus', 'genus_Dorea', 'genus_Eggerthella', 'genus_Erysipelotrichaceae_incertae_sedis', 'genus_Faecalibacterium', 'genus_Flavonifractor', 'genus_Holdemania', 'genus_Lachnospiracea_incertae_sedis', 'genus_Odoribacter', 'genus_Oscillibacter', 'genus_Parabacteroides', 'genus_Parasutterella', 'genus_Phascolarctobacterium', 'genus_Prevotella', 'genus_Pseudoflavonifractor', 'genus_Roseburia', 'genus_Ruminococcus', 'genus_Streptococcus', 'genus_Veillonella', 'genus_unclassified_Bacteria', 'genus_unclassified_Clostridiales', 'genus_unclassified_Clostridiales_Incertae.Sedis.XIII', 'genus_unclassified_Coriobacteriaceae', 'genus_unclassified_Erysipelotrichaceae', 'genus_unclassified_Firmicutes', 'genus_unclassified_Lachnospiraceae', 'genus_unclassified_Porphyromonadaceae', 'genus_unclassified_Ruminococcaceae']

phylum_df = pd.read_csv ("gut_16s_abundance.csv", usecols = phylum_coList)
class_df = pd.read_csv ("gut_16s_abundance.csv", usecols = class_coList)
order_df = pd.read_csv ("gut_16s_abundance.csv", usecols = order_coList)
family_df = pd.read_csv ("gut_16s_abundance.csv", usecols = family_coList)
genus_df = pd.read_csv ("gut_16s_abundance.csv", usecols = genus_coList)

#correlation test for each data frame
print(phylum_df.corr(method = 'pearson'))
print(class_df.corr(method = 'pearson'))
print(order_df.corr(method = 'pearson'))
print(family_df.corr(method = 'pearson'))
print(genus_df.corr(method = 'pearson'))