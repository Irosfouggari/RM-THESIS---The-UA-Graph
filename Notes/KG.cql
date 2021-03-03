{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>MED:7 </h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tools for extracting & displaying data\n",
    "import spacy\n",
    "from spacy import displacy\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span class=\"tex2jax_ignore\"><div class=\"entities\" style=\"line-height: 2.5; direction: ltr\">A patient was prescribed \n",
       "<mark class=\"entity\" style=\"background: #3cb44b; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    Magnesium hydroxide\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">DRUG</span>\n",
       "</mark>\n",
       " \n",
       "<mark class=\"entity\" style=\"background: #e6194B; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    400mg/5ml\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">DOSAGE</span>\n",
       "</mark>\n",
       " \n",
       "<mark class=\"entity\" style=\"background: #ffd8b1; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    suspension\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">FORM</span>\n",
       "</mark>\n",
       " \n",
       "<mark class=\"entity\" style=\"background: #f032e6; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    PO\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">ROUTE</span>\n",
       "</mark>\n",
       " of total \n",
       "<mark class=\"entity\" style=\"background: #e6194B; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    30ml\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">DOSAGE</span>\n",
       "</mark>\n",
       " \n",
       "<mark class=\"entity\" style=\"background: #f58231; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    bid\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">FREQUENCY</span>\n",
       "</mark>\n",
       " \n",
       "<mark class=\"entity\" style=\"background: #ffe119; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;\">\n",
       "    for the next 5 days\n",
       "    <span style=\"font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem\">DURATION</span>\n",
       "</mark>\n",
       ".</div></span>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[('Magnesium hydroxide', 'DRUG'),\n",
       " ('400mg/5ml', 'DOSAGE'),\n",
       " ('suspension', 'FORM'),\n",
       " ('PO', 'ROUTE'),\n",
       " ('30ml', 'DOSAGE'),\n",
       " ('bid', 'FREQUENCY'),\n",
       " ('for the next 5 days', 'DURATION')]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "med7 = spacy.load(\"en_core_med7_lg\")\n",
    "\n",
    "# create distinct colours for labels\n",
    "col_dict = {}\n",
    "seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']\n",
    "for label, colour in zip(med7.pipe_labels['ner'], seven_colours):\n",
    "    col_dict[label] = colour\n",
    "\n",
    "options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}\n",
    "\n",
    "text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'\n",
    "doc = med7(text)\n",
    "\n",
    "spacy.displacy.render(doc, style='ent', jupyter=True, options=options)\n",
    "\n",
    "[(ent.text, ent.label_) for ent in doc.ents]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cord_uid</th>\n",
       "      <th>sha</th>\n",
       "      <th>source_x</th>\n",
       "      <th>title</th>\n",
       "      <th>doi</th>\n",
       "      <th>pmcid</th>\n",
       "      <th>pubmed_id</th>\n",
       "      <th>license</th>\n",
       "      <th>abstract</th>\n",
       "      <th>publish_time</th>\n",
       "      <th>authors</th>\n",
       "      <th>journal</th>\n",
       "      <th>mag_id</th>\n",
       "      <th>who_covidence_id</th>\n",
       "      <th>arxiv_id</th>\n",
       "      <th>pdf_json_files</th>\n",
       "      <th>pmc_json_files</th>\n",
       "      <th>url</th>\n",
       "      <th>s2_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ug7v899j</td>\n",
       "      <td>d1aafb70c066a2068b02786f8929fd9c900897fb</td>\n",
       "      <td>PMC</td>\n",
       "      <td>Clinical features of culture-proven Mycoplasma...</td>\n",
       "      <td>10.1186/1471-2334-1-6</td>\n",
       "      <td>PMC35282</td>\n",
       "      <td>11472636</td>\n",
       "      <td>no-cc</td>\n",
       "      <td>OBJECTIVE: This retrospective chart review des...</td>\n",
       "      <td>04-07-01</td>\n",
       "      <td>Madani, Tariq A; Al-Ghamdi, Aisha A</td>\n",
       "      <td>BMC Infect Dis</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>document_parses/pdf_json/d1aafb70c066a2068b027...</td>\n",
       "      <td>document_parses/pmc_json/PMC35282.xml.json</td>\n",
       "      <td>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>02tnwd4m</td>\n",
       "      <td>6b0567729c2143a66d737eb0a2f63f2dce2e5a7d</td>\n",
       "      <td>PMC</td>\n",
       "      <td>Nitric oxide: a pro-inflammatory mediator in l...</td>\n",
       "      <td>10.1186/rr14</td>\n",
       "      <td>PMC59543</td>\n",
       "      <td>11667967</td>\n",
       "      <td>no-cc</td>\n",
       "      <td>Inflammatory diseases of the respiratory tract...</td>\n",
       "      <td>15-08-00</td>\n",
       "      <td>Vliet, Albert van der; Eiserich, Jason P; Cros...</td>\n",
       "      <td>Respir Res</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>document_parses/pdf_json/6b0567729c2143a66d737...</td>\n",
       "      <td>document_parses/pmc_json/PMC59543.xml.json</td>\n",
       "      <td>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   cord_uid                                       sha source_x  \\\n",
       "0  ug7v899j  d1aafb70c066a2068b02786f8929fd9c900897fb      PMC   \n",
       "1  02tnwd4m  6b0567729c2143a66d737eb0a2f63f2dce2e5a7d      PMC   \n",
       "\n",
       "                                               title                    doi  \\\n",
       "0  Clinical features of culture-proven Mycoplasma...  10.1186/1471-2334-1-6   \n",
       "1  Nitric oxide: a pro-inflammatory mediator in l...           10.1186/rr14   \n",
       "\n",
       "      pmcid  pubmed_id license  \\\n",
       "0  PMC35282   11472636   no-cc   \n",
       "1  PMC59543   11667967   no-cc   \n",
       "\n",
       "                                            abstract publish_time  \\\n",
       "0  OBJECTIVE: This retrospective chart review des...     04-07-01   \n",
       "1  Inflammatory diseases of the respiratory tract...     15-08-00   \n",
       "\n",
       "                                             authors         journal  mag_id  \\\n",
       "0                Madani, Tariq A; Al-Ghamdi, Aisha A  BMC Infect Dis     NaN   \n",
       "1  Vliet, Albert van der; Eiserich, Jason P; Cros...      Respir Res     NaN   \n",
       "\n",
       "   who_covidence_id  arxiv_id  \\\n",
       "0               NaN       NaN   \n",
       "1               NaN       NaN   \n",
       "\n",
       "                                      pdf_json_files  \\\n",
       "0  document_parses/pdf_json/d1aafb70c066a2068b027...   \n",
       "1  document_parses/pdf_json/6b0567729c2143a66d737...   \n",
       "\n",
       "                               pmc_json_files  \\\n",
       "0  document_parses/pmc_json/PMC35282.xml.json   \n",
       "1  document_parses/pmc_json/PMC59543.xml.json   \n",
       "\n",
       "                                                 url  s2_id  \n",
       "0  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3...    NaN  \n",
       "1  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5...    NaN  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Loading data\n",
    "data = pd.read_csv(\"C:/Users/Iro Sfoungari/Desktop/THESIS DATA/CORD-19/1000_metadata.csv\")\n",
    "data = data.loc[:, ~data.columns.str.contains('^Unnamed')]\n",
    "data.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "text1=data[\"abstract\"][265]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Iro Sfoungari\\anacondaDisaster\\lib\\site-packages\\spacy\\displacy\\__init__.py:189: UserWarning: [W006] No entities to visualize found in Doc object. If this is surprising to you, make sure the Doc was processed using a model that supports named entity recognition, and check the `doc.ents` property manually if necessary.\n",
      "  warnings.warn(Warnings.W006)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<span class=\"tex2jax_ignore\"><div class=\"entities\" style=\"line-height: 2.5; direction: ltr\">BACKGROUND: The Picornaviridae family contains a number of important pathogenic viruses, among which the recently reclassified human parechoviruses (HPeVs). These viruses are widespread and can be grouped in several types. Understanding the evolutionary history of HPeV could answer questions such as how long the circulating lineages last shared a common ancestor and how the evolution of this viral species is shaped by its population dynamics. Using both strict and relaxed clock Bayesian phylogenetics we investigated 1) the substitutions rates of the structural P1 and capsid VP1 regions and 2) evolutionary timescale of currently circulating HPeV lineages. RESULTS: Our estimates reveal that human parechoviruses exhibit high substitution rates for both structural P1 and capsid VP1 regions, respectively 2.21 × 10(-3 )(0.48 – 4.21 × 10(-3)) and 2.79 × 10(-3 )(2.05 – 3.66 × 10(-3)) substitutions per site per year. These are within the range estimated for other picornaviruses. By employing a constant population size coalescent prior, the date of the most recent common ancestor was estimated to be at around 1600 (1427–1733). In addition, by looking at the frequency of synonymous and non-synonymous substitutions within the VP1 gene we show that purifying selection constitutes the dominating evolutionary force leading to strong amino acid conservation. CONCLUSION: In conclusion, our estimates provide a timescale for the evolution of HPeVs and suggest that genetic diversity of current circulating HPeV types has arisen about 400 years ago.</div></span>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "doc = med7(text1)\n",
    "\n",
    "spacy.displacy.render(doc, style='ent', jupyter=True, options=options)\n",
    "\n",
    "[(ent.text, ent.label_) for ent in doc.ents]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_cr(abstractList, doiList):\n",
    "    i = 0\n",
    "    table= {\"cord_uid\":[], \"Entity\":[], \"Class\":[]}\n",
    "    for doc in med7.pipe(abstractList):\n",
    "        doi = doiList[i]\n",
    "        for x in doc.ents:\n",
    "          table[\"cord_uid\"].append(doi)\n",
    "          table[\"Entity\"].append(x.text)\n",
    "          table[\"Class\"].append(x.label_)\n",
    "        i +=1\n",
    "    return table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Read in file\n",
    "meta_df = pd. read_csv(\"C:/Users/Iro Sfoungari/Desktop/THESIS DATA/CORD-19/1000_metadata.csv\")\n",
    "#Sort out blank abstracts\n",
    "df = meta_df.dropna(subset=['abstract'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create lists\n",
    "doiList = df['cord_uid'].tolist()\n",
    "abstractList = df['abstract'].tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add all entity value pairs to table (run one at a time, each ones takes ~20 min)\n",
    "table = add_cr(abstractList, doiList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "trans_df = pd.DataFrame(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cord_uid</th>\n",
       "      <th>Entity</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>02tnwd4m</td>\n",
       "      <td>nitric oxide</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5yhe786e</td>\n",
       "      <td>red blood cells</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8qnrcgnk</td>\n",
       "      <td>ferrous iron</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8qnrcgnk</td>\n",
       "      <td>monoxide</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8qnrcgnk</td>\n",
       "      <td>anti-inflammatory and</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>jg13scgo</td>\n",
       "      <td>daily</td>\n",
       "      <td>FREQUENCY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>eiqypt0m</td>\n",
       "      <td>acyclovir</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>di0fcy0j</td>\n",
       "      <td>Oxygen</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>di0fcy0j</td>\n",
       "      <td>oxygen</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>gdsfkw1b</td>\n",
       "      <td>propeptide</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>l3z27806</td>\n",
       "      <td>anti-infective drugs</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>kvhoa2se</td>\n",
       "      <td>serine</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>kvhoa2se</td>\n",
       "      <td>leucine</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>kvhoa2se</td>\n",
       "      <td>leucine</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>ajlctjeb</td>\n",
       "      <td>cysteine-protease inhibitor E64 [trans-epoxysu...</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>ajlctjeb</td>\n",
       "      <td>phorbol</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>m71xkuo9</td>\n",
       "      <td>fluorescent dyes</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>s64v656n</td>\n",
       "      <td>methadone</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>mq6bterc</td>\n",
       "      <td>antibiotic</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>5eqdrd52</td>\n",
       "      <td>polyethylenimine</td>\n",
       "      <td>DRUG</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cord_uid                                             Entity      Class\n",
       "0   02tnwd4m                                       nitric oxide       DRUG\n",
       "1   5yhe786e                                    red blood cells       DRUG\n",
       "2   8qnrcgnk                                       ferrous iron       DRUG\n",
       "3   8qnrcgnk                                           monoxide       DRUG\n",
       "4   8qnrcgnk                              anti-inflammatory and       DRUG\n",
       "5   jg13scgo                                              daily  FREQUENCY\n",
       "6   eiqypt0m                                          acyclovir       DRUG\n",
       "7   di0fcy0j                                             Oxygen       DRUG\n",
       "8   di0fcy0j                                             oxygen       DRUG\n",
       "9   gdsfkw1b                                         propeptide       DRUG\n",
       "10  l3z27806                               anti-infective drugs       DRUG\n",
       "11  kvhoa2se                                             serine       DRUG\n",
       "12  kvhoa2se                                            leucine       DRUG\n",
       "13  kvhoa2se                                            leucine       DRUG\n",
       "14  ajlctjeb  cysteine-protease inhibitor E64 [trans-epoxysu...       DRUG\n",
       "15  ajlctjeb                                            phorbol       DRUG\n",
       "16  m71xkuo9                                   fluorescent dyes       DRUG\n",
       "17  s64v656n                                          methadone       DRUG\n",
       "18  mq6bterc                                         antibiotic       DRUG\n",
       "19  5eqdrd52                                   polyethylenimine       DRUG"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trans_df.head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
