# Ansible integration with Visual TOM
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE.md)&nbsp;
[![fr](https://img.shields.io/badge/lang-fr-yellow.svg)](README-fr.md)

This project provides an integration between Visual TOM and Ansible to execute Playbook with options or not.

# Disclaimer
No Support and No Warranty are provided by Absyss SAS for this project and related material. The use of this project's files is at your own risk.

Absyss SAS assumes no liability for damage caused by the usage of any of the files offered here via this Github repository.

Consultings days can be requested to help for the implementation.

# Prerequisites

  * Visual TOM 7.1.2 or greater
  * python3
  * ansible
  * ansible-runner

# Instructions

You need the Python add-on module ansible-runner. To install it, run the following commands using the provided requirement.txt file:
  ```Execute following PIP command with requirement.txt file
pip install -U update
pip install -U -r requirement.txt
  ```

The ansible.xml template must be imported into VTOM. It contains 5 parameters to be filled in (mandatory or optional):
 * The working directory containing the playbook(s) (mandatory)
 * The name of the playbook to execute (.yml) (mandatory)
 * The inventory file (full path) (optional)
 * Extra variables (optional)
 * Tags (optional)

The Python script ansible.py is executed from the queue batch tom_submit.ansible.
Provide the full path to the ansible.py script in the queue batch. If the script is located in $TOM_SCRIPT, no changes are required.
  ```To be modified if necessary
Line 31 : python3 ${TOM_SCRIPT}/ansible.py
  ``` 

# License
This project is licensed under the Apache 2.0 License - see the [LICENSE](license) file for details


# Code of Conduct
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)  
Absyss SAS has adopted the [Contributor Covenant](CODE_OF_CONDUCT.md) as its Code of Conduct, and we expect project participants to adhere to it. Please read the [full text](CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.
