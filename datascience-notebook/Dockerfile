FROM jupyter/datascience-notebook

USER root

RUN apt update && \
    apt install -y --no-install-recommends \
    libmysqlclient-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


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

RUN pip install \
    geopandas \
    folium \
    descartes \
    mysql-connector-python \
    python-igraph \
    modin[all] \
    git+https://github.com/sevamoo/SOMPY.git
