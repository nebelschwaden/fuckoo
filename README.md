# Fuckoo

![GitHub license](https://img.shields.io/github/license/nebelschwaden/fuckoo?color=brightgreen)
![GitHub contributors](https://img.shields.io/badge/contributors-1-yellowgreen)
![GitHub stars](https://img.shields.io/github/stars/nebelschwaden/fuckoo)
![GitHub forks](https://img.shields.io/github/forks/nebelschwaden/fuckoo?color=orange)

Fuckoo is a python script which can be used to obtain certain features from any JSON report generated with [Cuckoo Sandbox](https://cuckoosandbox.org/).  
Cuckoo Sandbox is a malware analysis tool that lets you analyze malicious files or websites under different  virtualized environments such as Windows, Linux, Android and so forth.
Cuckoo Sanbox generates a JSON report for each file it analyzes.  Fuckoo allows you to process multiple JSON files to create a dataset with some of the most important features which can be used for machine learning.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python >= 3.8.5
* Pandas >= 1.1.1

## Using Fuckoo

To use fuckoo, follow these steps:

Clone the repository.
```
git clone https://github.com/nebelschwaden/fuckoo
```
Set your current directory to where you cloned the repository, it may depend on your OS.
```
cd /some/directory/fuckoo
```
To run the script, you need to specify two things:  
* The directory in which your JSON files are located.
* The name you want to give to the dataset.
```
python3 fuckoo.py "/my/directory/with/json/files" "name_of_dataset"
```
Both arguments must be enclosed in quotation marks.

## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).
