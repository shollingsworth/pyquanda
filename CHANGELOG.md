# v1.0.27
#### Added Error handling to answer if no input given
> 2021-11-04 20:07 UTC [HEAD](https://github.com/shollingsworth/pyquanda/commit/HEAD)

---
# v1.0.26
#### Addded HOOK_TYPE_ENVIRONMENT_EXIT event
> 2021-11-04 19:43 UTC [8fdf00e](https://github.com/shollingsworth/pyquanda/commit/8fdf00ea1f21259ce550aabf59bdd4c4c82d09ad)

```
Fixed strip bug introduced in yanked 1.0.21
```
---
# v1.0.25
#### Another bugfix
> 2021-11-04 05:45 UTC [9686ca0](https://github.com/shollingsworth/pyquanda/commit/9686ca042d53ff7d96d71906e4aeacae760b7aa9)

---
# v1.0.24
#### Bugfix with ansible ok events sent
> 2021-11-04 05:07 UTC [a24029f](https://github.com/shollingsworth/pyquanda/commit/a24029f745505e7829d7e70194eecedcd15cfa0a)

---
# v1.0.23
#### Updated ansible webhook to fire on run ok and not only errors
> 2021-11-04 04:25 UTC [d9b7712](https://github.com/shollingsworth/pyquanda/commit/d9b771221557667f58c346419ffcdedd89e7a3f5)

```
* Fixed bug with local generation of userdata when INTERVIEW_CONFIG_REMOTE_FILE isn't set
```
#### Updated makefile, added back docs
> 2021-10-31 21:03 UTC [90b5c29](https://github.com/shollingsworth/pyquanda/commit/90b5c298295bad41cf3c68cd64f7231429c5f3fc)

---
# v1.0.22
#### Adjusted trimming on current questions
> 2021-10-31 21:02 UTC [19265ef](https://github.com/shollingsworth/pyquanda/commit/19265eff9ef3c770ee79b437a5e1e2a8380534ab)

---
# v1.0.21
#### Adjusted boto3 version to be less than 2
> 2021-10-30 21:24 UTC [b006313](https://github.com/shollingsworth/pyquanda/commit/b00631344c4944d27b7c43318f6409af9c571e36)

#### Straggler doc
> 2021-10-30 21:02 UTC [9fffbcb](https://github.com/shollingsworth/pyquanda/commit/9fffbcbff7420edf6024487fee5f57fa1d25ea34)

---
# v1.0.20
#### Updated requirements to include boto3
> 2021-10-30 21:01 UTC [f6bf50a](https://github.com/shollingsworth/pyquanda/commit/f6bf50a074ff15cee7d48877810708c552aced24)

```
* changed some text in the question prompt
```
---
# v1.0.19
#### Added AWS Api Gateway type webhook
> 2021-10-30 17:56 UTC [d81ee7d](https://github.com/shollingsworth/pyquanda/commit/d81ee7d00895338f875cf62733d8b5e9fe01f2a5)

---
# v1.0.18
#### Bugfix on yaml generation
> 2021-10-26 15:20 UTC [41fdfa2](https://github.com/shollingsworth/pyquanda/commit/41fdfa210b85f9e3594e304d54fd3d4ffdcd2f0e)

---
# v1.0.17
#### Fixed a typo in setup.py for extras
> 2021-10-25 07:47 UTC [b7c8d00](https://github.com/shollingsworth/pyquanda/commit/b7c8d00395a4996ab4f8696a30e40ee28ecf1f22)

---
# v1.0.16
#### Made ansible an extra dependency
> 2021-10-25 07:09 UTC [bde8ee6](https://github.com/shollingsworth/pyquanda/commit/bde8ee6bfb062342757272b253a3496dfd29ce1f)

---
# v1.0.15
#### Made start of python3 version verification via docker images
> 2021-10-24 19:37 UTC [80746c8](https://github.com/shollingsworth/pyquanda/commit/80746c87f9584e9ffe64d60f2718026b74ab4128)

```
* switched from ruamel.yaml to pyyaml due to issues with python3.9
```
---
# v1.0.14
#### Demo subcommand bugfix
> 2021-10-23 21:26 UTC [d8ae3f0](https://github.com/shollingsworth/pyquanda/commit/d8ae3f02c6a4b41e5bb58da0bec7f7eb83ff59f2)

```
* Added dev_requirements
* added trace to cli error
```
---
# v1.0.13
#### Updated network ports iterator
> 2021-10-23 02:28 UTC [55ecc6d](https://github.com/shollingsworth/pyquanda/commit/55ecc6dec71c5d6493c72eb659a9499fdba5b467)

---
# v1.0.12
#### Fixed bug in network port iteration
> 2021-10-23 00:57 UTC [2dad232](https://github.com/shollingsworth/pyquanda/commit/2dad232f817c91716075be493303eb7f6d32b5fc)

#### Added "a" as an alias to answer
> 2021-10-22 23:33 UTC [5c7e102](https://github.com/shollingsworth/pyquanda/commit/5c7e102aa45101e498d7028b382c04ede81cad71)

---
# v1.0.11
#### Changed the way hooks are called / configured
> 2021-10-22 23:21 UTC [bbd1179](https://github.com/shollingsworth/pyquanda/commit/bbd1179284d704686dedf420872b3eb832ef67c3)

```
* rolled hooks into userdata.zip and the source repo
* adjusted some jinja2 slack filters
* merged runbook complete and all complete
* fixed question background process issue
* added nav forward / previous hooks
```
#### Changed the way hooks are called / configured
> 2021-10-22 23:21 UTC [88e7be3](https://github.com/shollingsworth/pyquanda/commit/88e7be34fbed7c0bda184b6751a528a8001a2b3c)

```
* rolled hooks into userdata.zip and the source repo
* adjusted some jinja2 slack filters
* merged runbook complete and all complete
* fixed question background process issue
* added nav forward / previous hooks
```
---
# v1.0.10
#### Changed the way hooks are called / configured
> 2021-10-22 23:21 UTC [88e7be3](https://github.com/shollingsworth/pyquanda/commit/88e7be34fbed7c0bda184b6751a528a8001a2b3c)

```
* rolled hooks into userdata.zip and the source repo
* adjusted some jinja2 slack filters
* merged runbook complete and all complete
* fixed question background process issue
* added nav forward / previous hooks
```
#### Moved shell restrictions to a configurable parameter
> 2021-10-22 20:00 UTC [2fe0b01](https://github.com/shollingsworth/pyquanda/commit/2fe0b014bddd93aeb9299eaee53106220a20a40f)

---
# v1.0.9
#### Bugfixes and  re-writes
> 2021-10-22 19:19 UTC [3fa235a](https://github.com/shollingsworth/pyquanda/commit/3fa235a8ab70b84f3672c7adae006d405059c5ad)

```
* Removed the host config.py section
* added better error output for pyquanda-cmd cli tool
* replaced pymitter with pyee
* multiple edits to ansible base class
* added hook and slack template samples
* added ansible test sample
* added slack_webhook type for hooks configuration
```
---
# v1.0.8
#### turned off suppress output so the ansible run boot process can be watched
> 2021-10-21 06:41 UTC [3661604](https://github.com/shollingsworth/pyquanda/commit/366160400365197223e574e5a79ac88c6dde8b24)

---
# v1.0.7
#### Various bugfixes after testing
> 2021-10-21 06:30 UTC [737716e](https://github.com/shollingsworth/pyquanda/commit/737716e8b9ad1a8524dcbf3ee2b78aec7c998870)

#### forgot a dunder
> 2021-10-21 05:32 UTC [01316b6](https://github.com/shollingsworth/pyquanda/commit/01316b66e870a24d38f5cce13055828c2e110325)

---
# v1.0.6
#### fixed fstring issue on python 3.7
> 2021-10-21 05:28 UTC [abc32ca](https://github.com/shollingsworth/pyquanda/commit/abc32ca5d86e2d94bf110940bbba06fb650247fc)

---
# v1.0.5
#### Fixed setup
> 2021-10-21 05:24 UTC [0008962](https://github.com/shollingsworth/pyquanda/commit/0008962a58e8cc6bb01ac69c99d4a2c702271df7)

#### updated documentation
> 2021-10-21 05:09 UTC [378c81e](https://github.com/shollingsworth/pyquanda/commit/378c81e3a8fbb815a3f5674016c484fe5fb06665)

---