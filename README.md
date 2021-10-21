[![github-issues](https://img.shields.io/github/issues/shollingsworth/pyquanda?style=plastic "github-issues")](https://github.com/shollingsworth/pyquanda/issues) [![github-languages-code-size](https://img.shields.io/github/languages/code-size/shollingsworth/pyquanda?style=plastic "github-languages-code-size")](https://github.com/shollingsworth/pyquanda) [![github-stars](https://img.shields.io/github/stars/shollingsworth/pyquanda?style=plastic "github-stars")](https://github.com/shollingsworth/pyquanda/stargazers) [![github-forks](https://img.shields.io/github/forks/shollingsworth/pyquanda?style=plastic "github-forks")](https://github.com/shollingsworth/pyquanda/network/members) 

[![pypi-v](https://img.shields.io/pypi/v/pyquanda?style=plastic "pypi-v")](https://pypi.org/project/pyquanda) [![pypi-status](https://img.shields.io/pypi/status/pyquanda?style=plastic "pypi-status")](https://pypi.org/project/pyquanda) [![pypi-l](https://img.shields.io/pypi/l/pyquanda?style=plastic "pypi-l")](https://pypi.org/project/pyquanda) [![pypi-dm](https://img.shields.io/pypi/dm/pyquanda?style=plastic "pypi-dm")](https://pypi.org/project/pyquanda) [![pypi-pyversions](https://img.shields.io/pypi/pyversions/pyquanda?style=plastic "pypi-pyversions")](https://pypi.org/project/pyquanda) [![pypi-implementation](https://img.shields.io/pypi/implementation/pyquanda?style=plastic "pypi-implementation")](https://pypi.org/project/pyquanda) 

# TOC
* [PyQ[u]AndA](#pyq-u-anda-)
   * [Installation / Quickstart](#installation---quickstart-)
   * [License](#license-)
   * [Other Docs](#other-docs-)
   * [Command Help](#command-help-)


# PyQ[u]AndA [&#8593;](#toc)
    This is an interview environment based around xonsh, meant to be used via
    SSH and wrapped around custom hooks you define

Pull requests welcome!
## Installation / Quickstart [&#8593;](#toc)
To install this package from [pypy](https://pypi.org/project/pyquanda/) run the following command.


```

pip3 install pyquanda

```



```

pyquandacmd demo

```

## License [&#8593;](#toc)
See: [LICENSE](./LICENSE)
## Other Docs [&#8593;](#toc)
* [Api Docs](./docs/documentation.md)
* [Changelog](./CHANGELOG.md)
## Command Help [&#8593;](#toc)
# Main
## new
```
usage: gendoc.py new [-h] [--no_overwrite] --destination_directory DESTINATION_DIRECTORY {system,intro,problem} name description

create a new module from templates

positional arguments:
  {system,intro,problem}
                        module type
  name                  module name
  description           module name

optional arguments:
  -h, --help            show this help message and exit
  --no_overwrite        automatically overwrite destination directory
  --destination_directory DESTINATION_DIRECTORY, -d DESTINATION_DIRECTORY
                        src_module_dir help

```
## a_single
```
usage: gendoc.py a_single [-h] -s SRC_MODULE_DIR

run ansible on a single module based on path

optional arguments:
  -h, --help            show this help message and exit
  -s SRC_MODULE_DIR, --src_module_dir SRC_MODULE_DIR
                        source module directory

```
## a_all
```
usage: gendoc.py a_all [-h] -s SRC_MODULE_DIR

run all ansible modules in path

optional arguments:
  -h, --help            show this help message and exit
  -s SRC_MODULE_DIR, --src_module_dir SRC_MODULE_DIR
                        source module directory

```
## qsave
```
usage: gendoc.py qsave [-h] -s SRC_MODULE_DIR [--destination_directory DESTINATION_DIRECTORY]

convert questions to pyquanda questions config file

optional arguments:
  -h, --help            show this help message and exit
  -s SRC_MODULE_DIR, --src_module_dir SRC_MODULE_DIR
                        source module directory
  --destination_directory DESTINATION_DIRECTORY, -d DESTINATION_DIRECTORY
                        src_module_dir help

```
## qtest
```
usage: gendoc.py qtest [-h] -s SRC_MODULE_DIR [--keep_state]

test question set

optional arguments:
  -h, --help            show this help message and exit
  -s SRC_MODULE_DIR, --src_module_dir SRC_MODULE_DIR
                        source module directory
  --keep_state, -k      keep state (defaults to False)

```
## userdata
```
usage: gendoc.py userdata [-h] -s SRC_MODULE_DIR --destination_directory DESTINATION_DIRECTORY

save userdata zip file in directory (filename: userdata.zip)

optional arguments:
  -h, --help            show this help message and exit
  -s SRC_MODULE_DIR, --src_module_dir SRC_MODULE_DIR
                        source module directory
  --destination_directory DESTINATION_DIRECTORY, -d DESTINATION_DIRECTORY
                        src_module_dir help

```
## bootstrap
```
usage: gendoc.py bootstrap [-h] userdata_file

bootstrap host given userdata.zip file

positional arguments:
  userdata_file

optional arguments:
  -h, --help     show this help message and exit

```
## demo
```
usage: gendoc.py demo [-h]

demonstrate the xonsh question environment

optional arguments:
  -h, --help  show this help message and exit

```
