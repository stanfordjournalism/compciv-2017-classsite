# aws

```
aws s3  sync . s3://2017.compciv.org
```


```sh
# push to s3
cd  _build/html \
  && aws s3  sync . s3://2017.compciv.org \
  && cd ../..
da
make html SPHINXOPTS='-E'
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

## Toc

http://www.sphinx-doc.org/en/1.5.1/markup/toctree.html

.. toctree::
    :caption: Table of Contents
    :name: mastertoc
    :maxdepth: 2
    :numbered:
    :titlesonly:
    :glob:
    :hidden:

    intro.rst
    chapter1.rst
    chapter2.rst

## documents

    :doc:`/readings/fake-news`


## code examples

http://www.sphinx-doc.org/en/1.5.1/markup/code.html

#### Emphasize lines:

  :emphasize-lines: 3,5


#### Literal includes

.. literalinclude:: example.py
   :lines: 1-10




    .. epigraph::
      
        Hello world

        -- Brian



.. include:: syllabus/tech-stack.rst.inc



### Local toc

http://stackoverflow.com/questions/24129481/how-to-include-a-local-table-of-contents-into-sphinx-doc

.. contents:: :local:
