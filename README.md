# Mailman (POEM ver.) rpm spec files for Fedora Copr build
This repository maintains the packaging files to build packages on the Fedora Copr.

https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/

## Installation Instructions of Fedora Copr build packages
Currently, Copr repository is provided only for EL8 x86_64 packages.
```
$ sudo dnf install epel-release
$ sudo dnf copr enable orrisroot/mailman-jp
$ sudo dnf install mailman
```

## Providing Packages
* mailman : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/mailman/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/mailman/)
  * mailman-2.1.35+j1-1.el8.ors.src.rpm
  * mailman-2.1.35+j1-1.el8.ors.x86_64.rpm
  * mailman-debuginfo-2.1.35+j1-1.el8.ors.x86_64.rpm
  * mailman-debugsource-2.1.35+j1-1.el8.ors.x86_64.rpm
* python-cchardet : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/python-cchardet/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/python-cchardet/)
  * python-cchardet-2.1.7-4.1.el8.ors.src.rpm
  * python-cchardet-debugsource-2.1.7-4.1.el8.ors.x86_64.rpm
  * python2-cchardet-2.1.7-4.1.el8.ors.x86_64.rpm
  * python2-cchardet-debuginfo-2.1.7-4.1.el8.ors.x86_64.rpm
* python-pykf : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/python-pykf/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/mailman-jp/package/python-pykf/)
  * python-pykf-0.4-1.el8.ors.src.rpm
  * python-pykf-debugsource-0.4-1.el8.ors.x86_64.rpm
  * python2-pykf-0.4-1.el8.ors.x86_64.rpm
  * python2-pykf-debuginfo-0.4-1.el8.ors.x86_64.rpm
