**********************************************
SSHing into Stanford Farmshare (Cardinal/Corn)
**********************************************

So that non-journalism/non-Mac-using students aren't at a disadvantage, our early exercises can be done using the Stanford shared computing environment. In later weeks, we'll use machines on Amazon Cloud Computing.

Here's the homepage for `Stanford's Shared Computing Environment <https://uit.stanford.edu/service/sharedcomputing>`, though it contains way more details than we need.


Having a command-line
=====================

So the main obstacle is going to be whether you have a program, like **Terminal** with OS X, that can give you command-line access to a system, whether it is your own computer, or a remote computer like ``cardinal.stanford.edu``.


If you don't have a Mac
-----------------------

If you're on Windows, you won't have a **Terminal**, so you have two options:

1. Go to one of the campus computer labs, such as `Lathrop's Tech Lounge <https://library.stanford.edu/libraries/lathrop/tech-lounge>`_, and use their Macs.

2. Or, using the Chrome browser, install the `Secure Shell plugin <https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=en>`_ (we'll go over this in class)




Connecting to cardinal.stanford.edu via Terminal
================================================

``SSH`` is a protocol, just like ``HTTP`` for the web, for connecting to a remote computer. Except ``SSH`` gives us command-line access to system programs, just as if we were doing things on our own computers.

From your Terminal, type the following (using your Stanford ID):

.. code-block:: shell

    $ ssh your_stanford_name@cardinal.stanford.edu


If the connection is successful, you'll be asked for your password. And when you're authenticated, you'll be logged onto one of the Stanford "cardinal" machines.

It will look exactly like, well, your own system's command line, but that's because all shells basically look alike. But the commands you run logged in are on the "cardinal" computer.



.. _installing_compciv_2017_software_on_farmshare:



Installing software specific for Compciv 2017
=============================================

These instructions pertain only to students in Compciv 2017.

To summarize, these instructions cover how to install the following tools onto your Stanford shared computing space:

- miniconda
- csvkit
- youtube-dl
- ack


Installing miniconda
--------------------

For the majority of this class, you will be running Python through the Anaconda distribution


However, we don't want to install the full Anaconda on our Stanford Farmshare accounts, mostly because our Farmshare accounts are limited to 5GB, and Anaconda and all of its Python packages is multiple GBs. So we install "miniconda" which gives us the bare necessities for setting up a useful environment for some essential data tools for early assignments (i.e. work that we do before we go full Python on our own computers).

The official miniconda installation instructions are `here <http://conda.pydata.org/docs/install/quick.html>`_. But follow my instructions below:


Open up a Terminal and SSH into one of the Stanford Farmshare servers (I recommend ``corn.stanford.edu`` instead of ``cardinal.stanford.edu``):

.. code-block:: shell

    $ ssh your_id@corn.stanford.edu


After you've logged in, run this command to download the Miniconda installation script and save it as a file named ``miniconda-installer.sh``. Doesn't really matter where you do it, you might as well do it in your default home directory:


.. code-block:: shell

    $ curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh > miniconda-installer.sh

After the download has finished, run the script with this command:


.. code-block:: shell

    $ bash miniconda-installer.sh


You'll get these instructions:

.. code-block:: text

    Welcome to Miniconda3 4.2.12 (by Continuum Analytics, Inc.)

    In order to continue the installation process, please review the license
    agreement.
    Please, press ENTER to continue
    >>>


Hit your Enter key.

Then enter ``yes`` to the prompt ``Do you approve the license terms? [yes|no]``

Then the installer will ask where you want to install miniconda:

.. code-block:: text

    Miniconda3 will now be installed into this location:
    /afs/.ir/users/y/o/your_id/miniconda3

      - Press ENTER to confirm the location
      - Press CTRL-C to abort the installation
      - Or specify a different location below

    [/afs/.ir/users/y/o/your_id/miniconda3] >>>

Just hit **Enter** for the default, i.e. "to confirm the location".

Then wait for about 5 to 10 minutes for everything to install...



Finishing the miniconda install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the end of the installation process, you should see messages like:

.. code-block:: text

    creating default environment...
    installation finished.
    Do you wish the installer to prepend the Miniconda3 install location
    to PATH in your /afs/.ir/users/y/o/your_id/.bashrc ? [yes|no]
    [no] >>>

The default answer to this promopt is ``no`` but **please manually enter in** ``yes``.

You'll see a few more dense technical messages, and then you should be returned to your prompt.


To see if everything work, run this commmand:

.. code-block:: shell

    $ which python

The response should look like this (with your Stanford ID instead of ``your_id`` of course):


.. code-block:: text

    /afs/.ir/users/y/o/your_id/miniconda3/bin/python



Installing csvkit and youtube-dl via pip
----------------------------------------

csvkit and youtube-dl are command-line utilities that happen to be written in Python, not that that matters to us, except when it comes to installing them. With Anaconda (or miniconda) installed, the command to install both programs is simply:


.. code-block:: text

    $ pip install csvkit youtube-dl


To test if they work, use the ``which`` command and verify that you see output similar to this:


.. code-block:: shell

    $ which csvcut
    /afs/.ir/users/y/o/your_id/miniconda3/bin/csvcut

    $ which youtube-dl
    /afs/.ir/users/y/o/your_id/miniconda3/bin/youtube-dl


Installing ack
--------------

In general, it's a very bad idea to just copy-paste code into the shell, especially code that literally just downloads a file and does something to make it magically run, which is what the following line will seem like if you don't know Bash...but these are commands which come from the `ack homepage  <http://beyondgrep.com/install/>`_, which I've modified to fit our needs.

I guess you can type it out by hand but you'd probably make a typo:


.. code-block:: shell

    $ curl http://beyondgrep.com/ack-2.14-single-file > ~/miniconda3/bin/ack && chmod 0755 ~/miniconda3/bin/ack


When it's done downloading/installing, run ``which`` to see where ``ack`` is installed. You should get something like this:


.. code-block:: shell


    $ which ack
    /afs/.ir/users/y/o/your_id/miniconda3/bin/ack


Congrats, you have all the software needed to do what we need to do from the Stanford machines.



Navigating your Stanford Farmsshare user profile/data directory
===============================================================

Right when you log into one of the Stanford Farmshare servers (corn or cardinal), you should be "in" your **user home directory**.

Use the ``pwd`` command -- i.e. "print working directory" -- to see what that is:




Exposing your AFS files to the web
==================================

Once you've logged in, run the ``ls`` command to get a list of files:

.. code-block:: shell

    $ ls


You should see something similar to this (I have different files than you):

.. code-block:: shell

    $ dun@cardinal3:~$ ls
    Apps       Downloads  News  archive     sent
    Desktop    Mail       Pictures  cgi-bin    private
    Documents  Music      WWW   downloads  public


Anything in that ``WWW`` directory is exposed to the web. For example, if you have a file named ``cat.jpg`` in `WWW`, then the following URL will show ``cat.jpg`` to any web visitor:

`https://stanford.edu/~dun/cat.jpg <https://stanford.edu/~dun/cat.jpg>`_

(change ``dun`` to your own Stanford ID)



All Stanford students have 5GB on `Stanford's AFS (Andrew File System) <https://uit.stanford.edu/service/afs>`

.. note:: note

    Sorry, leaving this blank because I don't know if you all already know what AFS is. Can elaborate more in class.





Using corn.stanford.edu
-----------------------

Just a bit of minutiae; Stanford Farmshare also has servers named ``corn.stanford.edu``, which are actually more powerful and generally run faster than ``cardinal.stanford.edu``. Any files saved in your AFS user profile -- e.g. your ``~/WWW`` directory -- is the same on ``cardinal`` or ``corn``. This also includes any user-specific software that you've installed manually

So why do I often recommend using ``cardinal.stanford.edu``? Because you have to go through the two-factor authentication on the ``corn.stanford.edu`` servers:


.. code-block:: text

    $ ssh dun@corn.stanford.edu
    dun@corn.stanford.edu's password:
    Authenticated with partial success.
    Duo two-factor login for dun

    Enter a passcode or select one of the following options:

     1. Duo Push to XXX-XXX-2750
     2. Phone call to XXX-XXX-2750
     3. SMS passcodes to XXX-XXX-2750 (next code starts with: 1)









