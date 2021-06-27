# credo-template
Template for students

## Requirements

Installed:
* python 3.6 or never with `venv` package
* git

Tested on Linux. On Windows should be work but preparing and
activate virtual environment will be different.

PyCharm IDE is recommended.

Please download and unpack set of data from:
https://download.nkg-mn.com/credo/credo-hits/

## Initial

Clone template from GitHub, init virtual environment and install libraries:

```
git clone https://github.com/dzwiedziu-nkg/credo-template.git
cd credo-template
python3 -v venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt
```

## Download data

How to download and unpack exampled part of parts:

```
wget https://download.nkg-mn.com/credo/new_hits/part_15.json.xz
xzcat part_15.json.xz > part_15.json 
```

Please visit for another parts: https://download.nkg-mn.com/credo/credo-hits/

## The template

Please analyse `template.py` code line by line and read comments.
The `template.py` contains 3 parts: loading data, analysing and save result.

We expected result in CSV file with 3 columns:
```
[Classifier], [ID of hit], [Class]
```

* `Classifier` - is the classifier name what you use
* `ID of hit` - ID of classified hit
* `Class` - the result of classification
