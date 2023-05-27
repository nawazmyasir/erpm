# erpm
To write your own plugin (or to test this example plugin):

Fork this repository and edit its source code to interface with your credential management system of choice.
Define any necessary Python dependencies (e.g., client SDKs) necessary to integrate with your credential system by setting the requirements variable in setup.py.
From all AWX/Red Hat Ansible Tower nodes, install the plugin into the AWX virtualenv:

awx-python -m pip install git+https://github.com/nawazmyasir/erpm.git


From any AWX/Red Hat Ansible Tower node, run this command to register the plugin:

awx-manage setup_managed_credential_ty
