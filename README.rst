===============================
correctr
===============================

.. code-block:: bash

    $ # Clone repository
    $ git clone https://github.com/EnTeQuAk/correctr

    $ # create a new virtualenv (Note: Python 3.4 if possible, py2 is not supported)
    $ mkvirtualenv correctr

    $ # install
    $ python setup.py develop

    $ # run spellcorrecter shell
    $ correctr

    $ # run tests (note: those are randomized - some failures may be expected for now)
    $ py.test
