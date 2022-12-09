Name: crash
Version: 7.2.8
Release: 5
Summary: Linux kernel crash utility.
License: GPLv3
URL: https://crash-utility.github.io
Source0: https://github.com/crash-utility/crash/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz

Patch0: lzo_snappy.patch
Patch1: use_system_readline_v3.patch
Patch2: add-SDEI-stack-resolution.patch
Patch3: fix-bitmap_len-calculation-overflow-problem-in-large.patch
Patch4: 0001-CVE-2019-1010180-Add-bfd_get_file_size-to-get-archive-element-size.patch
Patch5: 0002-CVE-2019-1010180-DWARF-reader-Reject-sections-with-invalid-sizes.patch
Patch6: arm64-fix-backtraces-of-KASAN-kernel-dumpfile-truncated.patch

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
cp %{SOURCE1} .
make -j RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

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
* Thu Dec 1 2022 Ding Hui <dinghui@sangfor.com.cn> - 7.2.8-5
- fix backtraces of arm64 KASAN kernel dumpfile truncated

* Fri Oct 14 2022 chenhaixiang <chenhaixiang3@huawei.com> - 7.2.8-4
- fix gdb CVE-2019-1010180

* Mon May 10 2021 shixuantong <shixuantong@huawei.com> - 7.2.8-3
- add -j option for building efficiency optimization

* Sat Dec 12 2020 shixuantong <shixuantong@huawei.com> - 7.2.8-2
- Update Source0, URL, add Source1 and update tarball from upstream release

* Mon Aug 3 2020 chengquan <chengquan3@huawei.com> - 7.2.8-1
- Update software to v7.2.8

* Sun Jan 19 2020 Yeqing Peng <pengyeqing@huawei.com> - 7.2.6-3
- fix parse vmcore fail.

* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.2.6-2
- Package rebuild.

* Fri Aug 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.2.6-1
- Package init.
