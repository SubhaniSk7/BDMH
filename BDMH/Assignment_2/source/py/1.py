#!/usr/bin/env python
# coding: utf-8

# ### importing

# In[2]:


import sys
import numpy as np


# ### methods

# In[3]:


def get_all_seq(dot_plot, p1, p2):
    all_seq , considered= [],[]
    for i in range(len(dot_plot)):
        for j in range(len(dot_plot[i])):
            if dot_plot[i][j] == 1 and [i,j] not in considered:
                seq, ith, jth = [], i, j
                while ith < len(p1) and jth < len(p2) and dot_plot[ith][jth] == 1:
                    seq.append([ith,jth])
                    ith,jth = ith + 1, jth + 1
                if len(seq) >= 4:
                    all_seq.append(seq)
                    considered += seq
    return all_seq


# In[4]:


def get_all_seq_reverse(dot_plot, p1, p2):
    considered , all_seq_reverse= [], []
    for i in range(len(dot_plot)):
        for j in range(len(dot_plot[i])):
            if dot_plot[i][j] == 1 and [i,j] not in considered:
                #print(considered)
                #print(i,j)
                seq, ith, jth = [], i, j
                while ith < len(p1) and jth > -1 and dot_plot[ith][jth] == 1:
                    seq.append([ith,jth])
                    ith, jth = ith + 1, jth - 1
                if len(seq) >= 4:
                    seq.reverse()
                    all_seq_reverse.append(seq)
                    considered += seq
    return all_seq_reverse


# In[5]:


def get_sequences(all_seq, p):
    sequences = []
    for i in range(len(all_seq)):
        single = ''
        for j in range(len(all_seq[i])):
            single += p[all_seq[i][j][0]]
        sequences.append(single)
    return list(sequences)


# In[6]:


def get_dot_plot(protien1, protien2):
    dot_plot = np.zeros((len(protien1), len(protien2)))

    for i in range(len(dot_plot)):
        for j in range(len(dot_plot[i])):
            if protien1[i] == protien2[j]:
                dot_plot[i][j] = 1

    all_seq = get_all_seq(dot_plot, protien1, protien2)
    act_seq = get_sequences(all_seq, protien1)
    return list(act_seq)


# In[7]:


def get_dot_plot_reverse(protien1, protien2):
    dot_plot = np.zeros((len(protien1), len(protien2)))
    for i in range(len(dot_plot)):
        for j in range(len(dot_plot[i])):
            if protien1[i] == protien2[j]:
                dot_plot[i][j] = 1
    all_seq = get_all_seq_reverse(dot_plot, protien1, protien2)
    act_seq = get_sequences(all_seq, protien1)
    return list(act_seq)


# In[8]:


np.set_printoptions(threshold = sys.maxsize)


# In[9]:


if len(sys.argv) < 5 or sys.argv[1] != '-i' or sys.argv[3] != '-o':
    print('Enter CLI arguments in format:  python3 Answer_1.py -i input_file -o output_file')
else:
    inp_file = sys.argv[2]
    data = open(inp_file, 'r').read().split('\n')
    proteins = []
    for x in data:
        if len(x) > 0 and '>' not in x:
            proteins.append(x)
    if len(proteins) == 0:
        print('Protein seq. not found')
    else:
        text_file = open(sys.argv[4], "a")
        i = 0
        for protein in proteins:
            i += 1
            g = get_dot_plot(protein, protein)
            s = get_dot_plot_reverse(protein, protein)
            text_file.write('For sequence number ' + str(i) + '\n')
            text_file.write("Count: " + str(len(g)) + "\nReverse Count: " + str(len(s)) + '\n')
            text_file.write('--------------------------------------------\n\n')
        text_file.close()


# In[ ]: