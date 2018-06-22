# irk

---
> A package manager for package managers
---

`irk` is a tool which installs packages. It accomplishes this primarily by using other package managers, although it ~does~ will
include its own packaging systems.

## Usage

Using irk is as simple as installing it and running `sudo irk update` to get started. The `/etc/irk/sources.list.d` directory
will be created.

To use irk, you must create files in this directory corresponding to different sources for packages. These files simply contain lists of urls, as
well as comments starting with `#`.

These URLs point to files called "source descriptors", explained below.

## Source Descriptors

Source descriptors consist of three parts, the type, config and data. They are layed out like this:

```
<type>
<config>
CONFIGLINE
<data>
```

The meanings of these sections depends on the `<type>`, explained below (section title = `<type>`).

### `APT`
The `<config>` section for an `APT` entry contains two lines like this:
```
<name>
<executable>
```

The `<name>` is a name given to this source.
The `<executable>` is the path to `apt-get` on the system.

The `<data>` section is empty.

### `PIP`
The `<config>` section for an `PIP` entry contains one line. This line is simply the name of the source. As with the `APT` source 
type the `data` section is empty.

### `CREGX`
The `CREGX` type (stands for "custom with regular expressions) allows you to define a custom script to interface with another package management
system.

The `<config>` section looks like this:

```
<name>
<regex>
```

The `<regex>` refers to a regular expression that defines what packages this script _may_ match. The script can reject packages afterwards if it wants.
The `<data>` section contains the entire script. It should return 0 if the install was successful, return 101 if the package does not exist or any other code for failure.

An example can be seen in `sources/rosk.source`, useful if you have a ros kinetic source installation at "~/ros_kinetic" and want to install packages to it.

