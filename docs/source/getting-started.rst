Getting Started
===============

The development environment is meant to run on any platform where Linux
containers are supported, but has been actively tested on MacOS (with Docker
Desktop), and Ubuntu Linux hosts.

Requirements
------------

- **Vagrant** to control the development environment, please follow install
  `instructions for your platform here <https://www.vagrantup.com/downloads.html>`_.
- **Docker** to provide a lightweight container based environment for vagrant.
  Please follow the `install instructions for your platform <https://docs.docker.com/install/>`_.
- **Git** client to be able to clone the repository

Cloning and Starting
--------------------

Clone the repository from GitHub, then start the vagrant environment

.. code-block:: bash

   git clone https://github.com/ddompe/open-hw-dev
   cd open-hw-dev
   vagrant up

.. tip::

   This process may take some time the first time, as Docker will start downloading
   the container image from the public docker registry hub.

Once the Vagrant machine is up and running, you can establish a secure remote
connection via ssh by running `vagrant ssh` and the output should look like:

.. code-block:: bash

  $ vagrant ssh
  Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.9.184-linuxkit x86_64)

   $$$$$$\                                      $$\   $$\ $$\      $$\
  $$  __$$\                                     $$ |  $$ |$$ | $\  $$ |
  $$ /  $$ | $$$$$$\   $$$$$$\  $$$$$$$\        $$ |  $$ |$$ |$$$\ $$ |
  $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$$$$$$$ |$$ $$ $$\$$ |
  $$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |      $$  __$$ |$$$$  _$$$$ |
  $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |      $$ |  $$ |$$$  / \$$$ |
   $$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |  $$ |      $$ |  $$ |$$  /   \$$ |
   \______/ $$  ____/  \_______|\__|  \__|      \__|  \__|\__/     \__|
        $$ |
        $$ |
        \__|


              Open Hardware development environment 20.02.0

  Last login: Mon Feb 24 15:11:40 2020 from 172.17.0.1
  dev@hw-devel:~/ws$


.. note::

   The vagrant is configure to sync some folders from your host machine into
   your development machine, in special the folder with the git repo is available
   at `~/ws` and that is your default folder when doing ssh.

.. tip::

   You can open as many SSH sessions as you want. Some code editors like Visual
   Studio Code support `ssh remote edition <https://code.visualstudio.com/docs/remote/ssh>`_, which is very convenient.

Life cycle of the development machine
-------------------------------------

Once you are done with your development, you may want to "turn off" the container
with `vagrant halt`.

You may also need to destroy the environment altogether (for example to upgrade
to a new version of the environment), and you can do that with `vagrant destroy`.
