FROM jupyter/datascience-notebook

USER root

RUN apt update && \
    apt install -y --no-install-recommends \
    libmysqlclient-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install \
    pandas==0.25.3 \
    geopandas \
    folium \
    descartes \
    mysql-connector-python \
    python-igraph \
    modin[ray]==0.6.3 \
    git+https://github.com/sevamoo/SOMPY.git


# R packages including IRKernel which gets installed globally.
RUN conda install --quiet --yes \
    'r-islr' \
    'r-plot3d' \
    'r-rgl' \
    'r-car' \
    'r-mass' \
    'r-class' \
    'r-fnn' \
    'r-tree' \
    'r-randomforest' \
    'r-gbm' \
    'r-e1071' \
    'r-cluster' \
    'r-som' \
    && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER