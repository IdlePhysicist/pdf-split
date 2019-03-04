# PDF Split
#### IdlePhysicist, 2019

## Installation

Run the install script

```shell
chmod +x install.sh
./install.sh
```

The program is essentially a middleman between you and [GhostScript](https://www.ghostscript.com/). All it does is take your command arguments and pass them into a long string of args to GhostScript.

## Usage

- Range of pages:

Args: `<filename> -r <start page>-<end page>`

```shell
$ pdfsplit aipy.pdf -r 10-18
```

- Individual pages:

Args: `<filename> -i <number of pages>`

```shell
$ pdfsplit aipy.pdf -i 10
```
