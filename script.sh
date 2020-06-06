wget http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip

unzip gzip.zip
shopt -s extglob
cd gzip
rm -- !(+(emnist-letters)*)
gunzip *.gz
