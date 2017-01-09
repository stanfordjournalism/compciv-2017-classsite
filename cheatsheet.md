# aws


```sh
# push to s3
cd  _build/html \
  && aws s3 --profile dun sync . s3://compciv2017.s3.databa.es \
  && cd ../..
```

# wgets


```sh
# save a page
wget \
  --recursive --level=0 \
  --page-requisites \
  --convert-links \
  --no-directories \
  --adjust-extension \
  --html-extension \
  -e robots=off \
  --span-hosts true\
  domains=https://web.archive.org,http://abcnews.com.co \
  https://web.archive.org/web/20160320215817/http://abcnews.com.co/drug-kingpin-el-chapo-escapes-mexican-prison-once-again/ 
```



# rst

http://www.sphinx-doc.org/en/1.5.1/markup/inline.html

## documents

    :doc:`/readings/fake-news`
