FROM ubuntu:16.10

MAINTAINER Denis Torre <denis.torre@mssm.com>

RUN echo deb http://cran.rstudio.com/bin/linux/ubuntu yakkety/ >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y python
RUN apt-get update && apt-get install -y python-pip
RUN apt-get update && apt-get install -y python-dev
RUN apt-get update && apt-get install -y libxml2-dev
RUN apt-get update && apt-get install -y libxslt1-dev
RUN apt-get update && apt-get install -y --allow-unauthenticated r-base

RUN pip install --upgrade pip
RUN pip install numpy==1.13.1
RUN pip install pandas==0.20.3
RUN pip install jupyter==1.0.0
RUN pip install rpy2==2.8.6
RUN pip install plotly==2.0.12
RUN pip install scipy==0.19.1
RUN pip install sklearn
RUN pip install clustergrammer-widget==1.12.1
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension
RUN jupyter nbextension enable --py --sys-prefix clustergrammer_widget

RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("limma");'
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("edgeR");'

RUN mkdir /lecture
RUN mkdir /lecture/scripts
COPY *.ipynb /lecture/
COPY scripts /lecture/scripts

EXPOSE 8888

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser --notebook-dir='/lecture' --NotebookApp.iopub_data_rate_limit=10000000000 --NotebookApp.token=