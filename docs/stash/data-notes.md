
# baby names

~~~
curl https://www.ssa.gov/oact/babynames/names.zip \
  -o /tmp/names.zip
unzip names.zip -d /tmp
~~~



# FEC sample

~~~sh
curl ftp://ftp.fec.gov/FEC/2016/indiv16.zip -o indiv16.zip

curl http://www.fec.gov/finance/disclosure/metadata/indiv_header_file.csv \
  > indiv_data_2016.csv

csvformat -d '|' itcont.txt >> indiv_data_2016.csv

sed -n '1p;0~3p' input.txt

~~~
