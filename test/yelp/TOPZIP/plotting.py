# Script for generating plots

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import seaborn as sns

#sns.set_style("whitegrid")
sns.set_style("ticks")
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc("lines", linewidth=3.5)
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

# VARIABLES TO BE CHANGED
precisions = [1, 5, 20]
ALPHA=0.0
TIME=50
THRESHOLD=1
N_ITEMS_FOR_USER_U=0
N_USERS_FOR_ITEM_I=0
MAX_LENGTH_PREFIX=8

TITLE=r'\textbf{Yelp tag}'
FILENAME='yelp-test'


# OTHER STUFF
parameters = ['t', 'l', 'alpha', 'theta', 'nItemsForUserU', 'nUsersForItemI']
columns = parameters + ['ranking']

palette = sns.color_palette()
palette[-1], palette[-2] = palette[-2], palette[-1]
sns.palplot(palette)

# PLOT TIME LIMIT EFFECTS
#def plot_t(f, A, matrix, times, lengths):
#    for k in precisions:
#        P = matrix[k]
#        # TIME EVOLUTIONS
#        alpha = ALPHA
#        theta = THRESHOLD
#        fig = plt.figure()
#        for t in times:
#            res = []
#            for l in lengths:
#                res.append(P[(t,l,alpha,theta,N_ITEMS_FOR_USER_U,N_USERS_FOR_ITEM_I)])
#            plt.plot(lengths, res, label=r'$%d$' % t)
#        plt.xlabel(r'Prefix length $l$')
#        plt.ylabel(r'Precision $%d$' % k)
#        plt.legend(title=r'Time $t$ ($ms$)').draw_frame(True)
#        plt.savefig('./plots/'+f.rstrip('.txt')+'-time-precision-'+str(k)+'.pdf')
#        plt.close(fig)

# PLOTS ALPHA EFFECTS
def plot_alpha(f, A, matrix, alphas, lengths):
    for k in precisions:
        P = matrix[k]
        # TIME EVOLUTIONS
        t = TIME
        theta = THRESHOLD
        fig = plt.figure(figsize=(7, 6))
        for alpha in alphas:
            res = []
            for l in lengths:
                res.append(P[(t,l,alpha,theta,N_ITEMS_FOR_USER_U,N_USERS_FOR_ITEM_I)])
            plt.plot(lengths, res, label=r'$\boldsymbol{%g}$' % (alpha))
        plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
        plt.ylabel(r'\textbf{P@%d}' % k, fontsize=18)
        legend = plt.legend(title=r'$\boldsymbol{\alpha}$', fontsize=18)
        plt.setp(legend.get_title(),fontsize=22)
        legend.draw_frame(True)
        plt.title(TITLE, fontsize=19, y=1.03)
        plt.savefig('./plots/'+FILENAME+'-alpha-p'+str(k)+'.pdf', bbox_inches='tight')
        plt.close(fig)

# PLOTS ALPHA EFFECTS MRR
def plot_alpha_mrr(f, A, matrix, alphas, lengths):
    P = matrix
    # TIME EVOLUTIONS
    t = TIME
    theta = THRESHOLD
    fig = plt.figure(figsize=(7, 6))
    for alpha in alphas:
        res = []
        for l in lengths:
            res.append(P[(t,l,alpha,theta,N_ITEMS_FOR_USER_U,N_USERS_FOR_ITEM_I)])
        plt.plot(lengths, res, label=r'$\boldsymbol{%g}$' % (alpha))
    plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
    plt.ylabel(r'\textbf{MRR}' % k, fontsize=18)
    legend = plt.legend(title=r'$\boldsymbol{\alpha}$', fontsize=18)
    plt.setp(legend.get_title(),fontsize=22)
    legend.draw_frame(True)
    plt.title(TITLE, fontsize=19, y=1.03)
    plt.savefig('./plots/'+FILENAME+'-alpha-mrr.pdf', bbox_inches='tight')
    plt.close(fig)

# PLOT THETA EFFECTS
def plot_threshold(f, A, matrix, thresholds, lengths):
    for k in precisions:
        P = matrix[k]
        # TIME EVOLUTIONS
        t = TIME
        alpha = ALPHA
        fig = plt.figure(figsize=(7, 6))
        for theta in thresholds:
            res = []
            for l in lengths:
                res.append(P[(t,l,alpha,theta,N_ITEMS_FOR_USER_U,N_USERS_FOR_ITEM_I)])
            plt.plot(lengths, res, label=r"$\boldsymbol{%.3f}$" % theta)
        plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
        plt.ylabel(r'\textbf{P@%d}' % k, fontsize=18)
        legend = plt.legend(title=r'$\boldsymbol{\theta}$', fontsize=18)
        plt.setp(legend.get_title(),fontsize=22)
        legend.draw_frame(True)
        plt.title(TITLE, fontsize=19, y=1.03)
        plt.savefig('./plots/'+FILENAME+'-theta-p'+str(k)+'.pdf', bbox_inches='tight')
        plt.close(fig)

# PLOT THETA EFFECTS MRR
def plot_threshold_mrr(f, A, matrix, thresholds, lengths):
    P = matrix
    # TIME EVOLUTIONS
    t = TIME
    alpha = ALPHA
    fig = plt.figure(figsize=(7, 6))
    for theta in thresholds:
        res = []
        for l in lengths:
            res.append(P[(t,l,alpha,theta,N_ITEMS_FOR_USER_U,N_USERS_FOR_ITEM_I)])
        plt.plot(lengths, res, label=r"$\boldsymbol{%.3f}$" % theta)
    plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
    plt.ylabel(r'\textbf{MRR}' % k, fontsize=18)
    legend = plt.legend(title=r'$\boldsymbol{\theta}$', fontsize=18)
    plt.setp(legend.get_title(),fontsize=22)
    legend.draw_frame(True)
    plt.title(TITLE, fontsize=19, y=1.03)
    plt.savefig('./plots/'+FILENAME+'-theta-mrr.pdf', bbox_inches='tight')
    plt.close(fig)

# PLOT TEST DATASET FILTERING EFFECTSS
def plot_test_filtering(f, A, matrix, nItemsForUserU, nUsersForItemI):
    for k in precisions:
        P = matrix[k]
        # TIME EVOLUTIONS
        t = TIME
        alpha = ALPHA
        fig = plt.figure(figsize=(7, 6))
        for n1 in nItemsForUserU:
            for n2 in nUsersForItemI:
                res = []
                for l in lengths:
                    res.append(P[(t,l,alpha,THRESHOLD,n1,n2)])
                if n1 < 0:
                    if n2 >= 0:
                        plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \leq %d}$, $\boldsymbol{\eta_u \geq %d}$' % (abs(n1), n2))
                    else:
                        plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \leq %d}$, $\boldsymbol{\eta_u \leq %d}$' % (abs(n1), abs(n2)))
                else:
                    if n2 >= 0:
                        plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \geq %d}$, $\boldsymbol{\eta_u \geq %d}$' % (n1, n2))
                    else:
                        plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \geq %d}$, $\boldsymbol{\eta_u \leq %d}$' % (n1, abs(n2)))
        plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
        plt.ylabel(r'\textbf{P@%d}' % k, fontsize=18)
        legend = plt.legend(fontsize=18)
        plt.setp(legend.get_title(),fontsize=22)
        legend.draw_frame(True)
        plt.title(TITLE, fontsize=19, y=1.03)
        plt.savefig('./plots/'+FILENAME+'-filtering-p'+str(k)+'.pdf', bbox_inches='tight')
        plt.close(fig)

# PLOT TEST DATASET FILTERING EFFECTSS -- MRR
def plot_test_filtering_mrr(f, A, matrix, nItemsForUserU, nUsersForItemI):
    P = matrix
    # TIME EVOLUTIONS
    t = TIME
    alpha = ALPHA
    fig = plt.figure(figsize=(7, 6))
    for n1 in nItemsForUserU:
        for n2 in nUsersForItemI:
            res = []
            for l in lengths:
                res.append(P[(t,l,alpha,THRESHOLD,n1,n2)])
            if n1 < 0:
                if n2 >= 0:
                    plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \leq %d}$, $\boldsymbol{\eta_u \geq %d}$' % (abs(n1), n2))
                else:
                    plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \leq %d}$, $\boldsymbol{\eta_u \leq %d}$' % (abs(n1), abs(n2)))
            else:
                if n2 >= 0:
                    plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \geq %d}$, $\boldsymbol{\eta_u \geq %d}$' % (n1, n2))
                else:
                    plt.plot(lengths, res, label=r'$\boldsymbol{\eta_i \geq %d}$, $\boldsymbol{\eta_u \leq %d}$' % (n1, abs(n2)))
    plt.xlabel(r'$\boldsymbol{l}$', fontsize=20)
    plt.ylabel(r'\textbf{MRR}' % k, fontsize=18)
    legend = plt.legend(fontsize=18)
    plt.setp(legend.get_title(),fontsize=22)
    legend.draw_frame(True)
    plt.title(TITLE, fontsize=19, y=1.03)
    plt.savefig('./plots/'+FILENAME+'-filtering-mrr.pdf', bbox_inches='tight')
    plt.close(fig)

# Script to generate the test input file

def datafixed(f):
    oldf = f
    name = f.rstrip('.txt')+'-fixed'+'.txt'
    with open(oldf, 'r') as f:
        maximum = 0
        for line in f:
            line = line.rstrip('\n')
            res = line.split('\t')
            if len(res) != 12:
                print 'Problem, too many columns'
                continue
            if maximum < int(res[5]):
                maximum = int(res[5])
    print str(maximum)
    with open(name, 'w') as newFile:
        with open(oldf, 'r') as f:
            currU = -1
            currI = -1
            currTag = -1
            currFreq = -1
            currTime = -1
            currL = -1
            currAlpha = -1
            currThres = -1
            currRanking = -1
            nItemsForUserU = -1
            nUsersForItemsI = -1
            #currNbWords = -1
            for line in f:
                line = line.rstrip('\n')
                res = line.split('\t')
                if len(res) != 12:
                    print 'ok'
                    continue
                if ((currU!=res[0]) or currTime!=res[4] or currAlpha!=res[6]) and (currU!=-1):# and (currAlpha==str(ALPHA)):# and (currNbWords=='1'):
                    for i in range(int(currL)+1, maximum+1):
                        newFile.write(currU+'\t'+currI+'\t'+currTag+'\t'+currFreq+'\t'+currTime+'\t'+str(i)+'\t'+currAlpha+'\t'+currThres+'\t'+currRanking+'\t'+nItemsForUserU+'\t'+nUsersForItemI+'\n')#'\t'+currNbWords+'\n')
                currU = res[0]
                currI = res[1]
                currTag = res[2]
                currFreq = res[3]
                currTime = res[4]
                currL = res[5]
                currAlpha = res[6]
                currThres = res[7]
                currRanking = res[8]
                nItemsForUserU = res[10]
                nUsersForItemI = res[11]
                newFile.write(currU+'\t'+currI+'\t'+currTag+'\t'+currFreq+'\t'+currTime+'\t'+currL+'\t'+currAlpha+'\t'+currThres+'\t'+currRanking+'\t'+nItemsForUserU+'\t'+nUsersForItemI+'\n')
            for i in range(int(currL)+1, maximum+1):
                newFile.write(currU+'\t'+currI+'\t'+currTag+'\t'+currFreq+'\t'+currTime+'\t'+str(i)+'\t'+currAlpha+'\t'+currThres+'\t'+currRanking+'\t'+nItemsForUserU+'\t'+nUsersForItemI+'\n')
    return name

if __name__=='__main__':
    if len(sys.argv)<=1:
        sys.exit(0)
    files = [arg for arg in sys.argv[1:]]
    files_fixed = []
    for f in files:
        A = pd.read_csv(f, sep='\t', names=['user', 'item', 'tag', 'freq', 't', 'l', 'alpha', 'theta', 'ranking', 'nbWords', 'nItemsForUserU', 'nUsersForItemI'])
        A = A.loc[A['nbWords']==1]
        A.to_csv('results.txt',sep='\t',header=False,index=False)
        files_fixed.append(datafixed('results.txt'))
        os.remove('results.txt')
        A['theta'] = A['theta'].map(lambda x: round(x,4))
    for f in files_fixed:
        A = pd.read_csv(f, sep='\t', names=['user', 'item', 'tag', 'freq', 't', 'l', 'alpha', 'theta', 'ranking', 'nItemsForUserU', 'nUsersForItemI'])
        A = A.dropna()
        # Matrix generation
        g=A.groupby(parameters)
        matrixKeys = g.groups.viewkeys()
        #print matrixKeys

        matrix = {}
        for k in precisions:
            matrix[k] = {}
            for key in matrixKeys:
                DF = g.get_group(key)
                DF = DF[["ranking"]]
                DF = DF.replace(0, np.nan)
                val = float(len(DF[(DF.ranking<=k)]))/len(DF)
                matrix[k][key]=val

        matrix_mrr = {}
        for key in matrixKeys:
            DF = g.get_group(key)
            DF = DF[["ranking"]]
            DF = DF.replace(0, 1.e9)
            val = 0.
            for i in range(len(DF)):
                val += 1 / DF.iloc[i]['ranking']
            val /= len(DF)
            # val = float(len(DF[(DF.ranking<=k)]))/len(DF)
            matrix_mrr[key] = val

        # TIMES
        times = []
        g_times = A.groupby('t')
        keys = g_times.groups.viewkeys()
        for t in keys:
            times.append(int(t))
        times = sorted(times)
        print str(times)
        # ALPHAS
        alphas = []
        g_alphas = A.groupby('alpha')
        keys = g_alphas.groups.viewkeys()
        for alpha in keys:
            alphas.append(float(alpha))
        alphas = sorted(alphas)
        print str(alphas)
        # THRESHOLDS
        thresholds = []
        g_thresholds = A.groupby('theta')
        keys = g_thresholds.groups.viewkeys()
        for theta in keys:
            thresholds.append(float(theta))
        thresholds = sorted(thresholds)
        print str(thresholds)
        THRESHOLD = min(thresholds)
        # LENGTHS
        lengths = []
        g_l = A.groupby('l')
        keys = g_l.groups.viewkeys()
        for l in keys:
            if (int(l) > MAX_LENGTH_PREFIX):
                continue
            lengths.append(int(l))
        lengths = sorted(lengths)
        # N_ITEMS_FOR_USER_U
        nItemsForUserU = []
        g_nItemsForUserU = A.groupby('nItemsForUserU')
        keys = g_nItemsForUserU.groups.viewkeys()
        for k in keys:
            nItemsForUserU.append(int(k))
        nItemsForUserU = sorted(nItemsForUserU)
        N_ITEMS_FOR_USER_U = max(nItemsForUserU)
        # N_USERS_FOR_ITEM_I
        nUsersForItemI = []
        g_nusers = A.groupby('nUsersForItemI')
        keys = g_nusers.groups.viewkeys()
        for k in keys:
            nUsersForItemI.append(int(k))
        nUsersForItemI = sorted(nUsersForItemI)
        N_USERS_FOR_ITEM_I = min(nUsersForItemI)
        N_USERS_FOR_ITEM_I = -9

        # PLOTS HERE
        #plot_test_filtering(f, A, matrix, nItemsForUserU, nUsersForItemI)
        #plot_test_filtering_mrr(f, A, matrix_mrr, nItemsForUserU, nUsersForItemI)
        #plot_t(f, A, matrix, times, lengths)
        plot_alpha(f, A, matrix, alphas, lengths)
        #plot_alpha_mrr(f, A, matrix_mrr, alphas, lengths)
        #plot_threshold(f, A, matrix, thresholds, lengths)
        #plot_threshold_mrr(f, A, matrix_mrr, thresholds, lengths)
