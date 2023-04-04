---
layout: ../../layouts/MarkdownPostLayout.astro
title: "Know the Size of an Ubuntu Package Prior to Downloading It"
date: 2016-11-23
tags: ["Linux"]
summary: "Have you ever wanted to know the amount of data which will be downloaded when you install a package with `apt-get`?"
---

Have you ever wanted to know the amount of data which will be downloaded when you install a package with `apt-get`?  
Or the amount of data the installation will take?  
Or you install a list of packages so that the total install size gets quite huge and you want to know which package is to be blamed?  
You are lucky, `apt` has got you covered!

```bash
> apt-cache show --no-all-versions <pkg name>
```

This is the only command you have to run. The output looks like the following:

```bash
Package: git
Priority: optional
Section: vcs
Installed-Size: 23484
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Gerrit Pape <pape@smarden.org>
Architecture: amd64
Version: 1:2.7.4-0ubuntu1
Replaces: git-core (<< 1:1.7.0.4-1.), gitweb (<< 1:1.7.4~rc1)
Provides: git-completion, git-core
Depends: libc6 (>= 2.16), libcurl3-gnutls (>= 7.16.2), libexpat1 (>= 2.0.1), libpcre3, zlib1g (>= 1:1.2.0), perl-modules, liberror-perl, git-man (>> 1:2.7.4), git-man (<< 1:2.7.4-.)
Recommends: patch, less, rsync, ssh-client
Suggests: gettext-base, git-daemon-run | git-daemon-sysvinit, git-doc, git-el, git-email, git-gui, gitk, gitweb, git-arch, git-cvs, git-mediawiki, git-svn
Breaks: bash-completion (<< 1:1.90-1), cogito (<= 0.18.2+), git-buildpackage (<< 0.6.5), git-core (<< 1:1.7.0.4-1.), gitosis (<< 0.2+20090917-7), gitpkg (<< 0.15), gitweb (<< 1:1.7.4~rc1), guilt (<< 0.33), stgit (<< 0.15), stgit-contrib (<< 0.15)
Filename: pool/main/g/git/git_2.7.4-0ubuntu1_amd64.deb
Size: 3006120
MD5sum: 0412535c34d3f900629e9409ad73aead
SHA1: 87888d183e279e53035587cc2c42d16c6a06612f
SHA256: 8189c2dfe9ae6f3dc00c4cf858acbc53ba99a11d62646b2b7c62af9acb5076cd
Description: fast, scalable, distributed revision control system
Description-md5: c1f968556452a190fe359bffd151c012
Multi-Arch: foreign
Homepage: https://git-scm.com/
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Origin: Ubuntu
Supported: 5y
Task: cloud-image, server
```

There are two interesting lines for us in this output :

- `Installed-Size: 23484`
- `Size: 3006120`

`Size` corresponds to the download size while `Installed-Size` corresponds to the space the package will take after being installed. Both are in bytes.

If you want to see the size in human format and that you are on Ubuntu 14.04 or greater, you can use the `apt` command instead of `apt-cache`.

The main problem with this command however is that it does not take into account the dependencies of the package we want to install.

That's where `awk` can help us. We can run the following command to get the list of new packages to be installed when running `apt-get install <pkg name>`:

```bash
> apt-get install --dry-run git | awk 'BEGIN { ORS=" " }; $1 == "Inst" {print $2}'
libatm1 libmnl0 libpopt0 libgdbm3 libxau6 libxdmcp6 libxcb1 libx11-data libx11-6 libxext6 perl-modules-5.22 libperl5.22 perl iproute2 ifupdown libisc-export160 libdns-export162 isc-dhcp-client isc-dhcp-common less libbsd0 libexpat1 libffi6 libgmp10 libnettle6 libhogweed4 libidn11 libp11-kit0 libtasn1-6 libgnutls30 libsqlite3-0 libssl1.0.0 libxtables11 netbase openssl ca-certificates krb5-locales libroken18-heimdal libasn1-8-heimdal libkrb5support0 libk5crypto3 libkeyutils1 libkrb5-3 libgssapi-krb5-2 libhcrypto4-heimdal libheimbase1-heimdal libwind0-heimdal libhx509-5-heimdal libkrb5-26-heimdal libheimntlm0-heimdal libgssapi3-heimdal libsasl2-modules-db libsasl2-2 libldap-2.4-2 librtmp1 libcurl3-gnutls libedit2 libsasl2-modules libxmuu1 openssh-client rsync xauth liberror-perl git-man git patch rename
```

If we pass the output of this command to `apt-cache` and filter the output with `awk` again, we get the total download size:

```bash
> apt-cache --no-all-versions show $(apt-get install --dry-run git | awk 'BEGIN { ORS=" " }; $1 == "Inst" {print $2}') | awk '$1 == "Size:" {total += $2}; END {printf("%.2f MB\n", total / (1024^2)) }'
18.30 MB
```

Et voilà! That's it for this small trick (other answers to this question can be found [there](http://askubuntu.com/questions/35956/how-to-determine-the-size-of-a-package-while-using-apt-prior-to-downloading)). Unfortunately it seems that it is impossible to do the same with Brew yet but let's wait and see.
