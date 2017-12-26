ls-colours
==========
Shell utility to colourize ls based on file extension


Installation
------------

* Clone the repository to `/opt/`:
```shell
git clone git@github.com:ndrein/ls-colors.git /opt/
```

* Use the script `bin/ls` as an alias for `ls`.  This command uses `.bashrc` as your shell startup file, but you can put this alias wherever you need to:
```shell
echo "alias ls=`readlink -f /opt/ls-colors/bin/ls`" >> ~/.bashrc
```

Note that `bin/ls` must not be moved outside of the `ls-colors` repository.


Dependencies
------------

* `python3` in your `$PATH`


Usage
-----

Identical to `ls`.


Implementation
--------------

Hashes each file extension in the requested directories to produce a deterministic colour for each extension.  
Hidden files and files without extensions (eg. `.hidden`, `no-extension`) will not be coloured.
