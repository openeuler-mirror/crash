Name: crash
Version: 7.2.8
Release: 4
Summary: Linux kernel crash utility.
License: GPLv3
URL: http://people.redhat.com/anderson
Source0: http://people.redhat.com/anderson/%{name}-%{version}.tar.gz

Patch0: lzo_snappy.patch
Patch1: use_system_readline_v3.patch

Patch9000: add-SDEI-stack-resolution.patch
Patch9001: fix-bitmap_len-calculation-overflow-problem-in-large.patch
Patch9002: 4d2e607af5d758f9ae42864cb6b26af49e9f5b1d.patch

BuildRequires: ncurses-devel zlib-devel lzo-devel snappy-devel
BuildRequires: gcc gcc-c++ bison readline-devel
Requires: binutils

Provides: bundled(libiberty) bundled(gdb) = 7.6

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump
creation facilities such as kdump, kvmdump, xendump, the netdump and
diskdump packages offered by Red Hat, the LKCD kernel patch, the mcore
kernel patch created by Mission Critical Linux, as well as other formats
created by manufacturer-specific firmware.

%package devel
Summary: the development kit of crash.
Requires: %{name} = %{version}, zlib-devel

%description devel
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump
creation facilities such as kdump, kvmdump, xendump, the netdump and
diskdump packages offered by Red Hat, the LKCD kernel patch, the mcore
kernel patch created by Mission Critical Linux, as well as other formats
created by manufacturer-specific firmware.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
make RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%make_install
install -D -m 0644 crash.8 %{buildroot}%{_mandir}/man8/crash.8
install -D -m 0644 defs.h %{buildroot}%{_includedir}/%{name}/defs.h

%check

%pre

%preun

%post

%postun

%files
%{_bindir}/%{name}
%doc README
%license COPYING3

%files devel
%{_includedir}/*

%files help
%{_mandir}/man8/crash.8*

%changelog
* 20201026123007621517 patch-tracking 7.2.8-4
- append patch file of upstream repository from <4d2e607af5d758f9ae42864cb6b26af49e9f5b1d> to <4d2e607af5d758f9ae42864cb6b26af49e9f5b1d>

* Tue Sep 8 2020 shixuantong <shixuantong@huawei.com> - 7.2.8-3
- Restore Source0 and URL

* Tue Jul 28 2020 xinghe <xinghe1@huawei.com> - 7.2.8-2
- repair the source0

* Mon Jul 27 2020 xinghe <xinghe1@huawei.com> - 7.2.8-1
- update version to 7.2.8

* Sun Jan 19 2020 Yeqing Peng <pengyeqing@huawei.com> - 7.2.6-3
- fix parse vmcore fail.

* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.2.6-2
- Package rebuild.

* Fri Aug 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.2.6-1
- Package init.