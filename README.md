# `a2s-cli`

This tool is only available for the following operating systems:
- Linux: **Ubuntu 22.04** (recommended).
- Windows: Through WLS 2 with Ubuntu 22.04 (experimental).
- MacOS: technically possible but not yet implemented.

> [!IMPORTANT]
> Installation is restricted to linux systems only.

## Install

The following command takes care of installing the necessary dependencies and installs `a2s` cli tool for you:

```sh
wget --show-progress --tries=1 -qO- https://raw.githubusercontent.com/harleylara/a2s-cli/refs/heads/main/install.sh | bash
```

## How to use

Depending on the robot to be used, initialize the robot container, for example to start `foxy`:

```
a2s init foxy
```

If you want to see a list of supported robots:

```
a2s ls
```

To start the container of the robot:

```
a2s run foxy
```

## How to update

To update the `a2s0-cli` tool (just the tool no the containers):

```
a2s update
```

to update a specific robot container:

```
a2s ????? (not yet implemented)
```
