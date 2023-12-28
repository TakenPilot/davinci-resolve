# Davinci Resolve

Scripts and tools for Davinci Resolve.

## Requirements

- Python 3.6+, latest tested is 3.6.15, see [.tool-versions](./.tool-versions)
- Davinci Resolve 18+

## Installation

```bash
pip install -r requirements.txt
```

### Python 3.6 Installation

Install Rosetta to run Intel binaries on Apple Silicon.

```zsh
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

Does this work? If so, you can run Intel binaries and you can skip the error sections below.

```zsh
arch -x86_64 /bin/bash -c "echo hello"
```

#### Package reference com.apple.pkg.RosettaUpdateAuto is missing installKBytes attribute

If you get this error, you might need to reinstall Rosetta. Try this:

```zsh
pkgutil --files com.apple.pkg.RosettaUpdateAuto
```

Remember the path to Rosetta and libexec, such as `/Library/Apple/usr/share/rosetta` and `/Library/Apple/usr/libexec`.
Open the M1 in recovery mode.
Run `csrutil disable` and confirm, and reboot.
Delete the Rosetta files and libexec directories.
Reboot into recovery mode again.
Run `csrutil enable` and confirm, and reboot.

#### Rosetta still doesn't work

If Rosetta still doesn't work, try this:

```zsh
open /System/Library/CoreServices/
```

Find "Rosetta 2 Updater" in the list and open it. Can you run `arch -x86_64 bash` now?

#### Final solution if Rosetta still doesn't work

```
sudo uninstall /System/Library/CoreServices/Rosetta\ 2\ Updater.app
```

Restart, reinstall. Does `arch -x86_64 bash` work now? If not, I dunno.

### Python 3.6 Installation on Apple Silicon

```zsh
brew install pyenv
pyenv install 3.6.15
pyenv global 3.6.15
```
