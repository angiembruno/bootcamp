

import numpy as np

def make_pca_plot(traces):
    # traces: Individual experiment loaded from the brain observatory
    #traces #columns are neuron IDs, rows are time points (e.g. 1000 x 60 for 1000 sec sampled at 1 Hz and 60 neurons)
    PCmat = traces - traces.mean(axis=1)[:, np.newaxis] #mean subtract the matrix
    from sklearn.decomposition import PCA
    pca = PCA(n_components = 10) #any number you want here
    pca.fit(PCmat)
    np.sum(pca.explained_variance_ratio_) #sanity check: should be around 0.6 for 10 components
    plt.plot(pca[0,:],pca[1,:])
