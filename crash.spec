Name: crash
Version: 7.3.0
Release: 8
Summary: Linux kernel crash utility.
License: GPLv3
URL: https://crash-utility.github.io
Source0: https://github.com/crash-utility/crash/archive/%{version}.tar.gz
Source1: http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz

Patch1: lzo_snappy.patch
Patch2: 0001-arm64-rename-ARM64_PAGE_OFFSET_ACTUAL-to-ARM64_FLIP_.patch
Patch3: 0002-arm64-assign-page_offset-with-VA_BITS-kernel-configu.patch
Patch4: 0003-arm64-use-dedicated-bits-to-record-the-VA-space-layo.patch
Patch5: 0004-arm64-implement-switchable-PTOV-VTOP-for-kernels-5.1.patch
Patch6:	add-SDEI-stack-resolution.patch
Patch7: Handle-task_struct-cpu-member-changes-for-kernels-5..patch
Patch8: 0001-CVE-2019-1010180-Add-bfd_get_file_size-to-get-archive-element-size.patch
Patch9: 0002-CVE-2019-1010180-DWARF-reader-Reject-sections-with-invalid-sizes.patch
%ifarch sw_64
Patch10: crash-7.3.0-sw.patch
%endif
Patch11: Fix-live-debugging-with-lockdown-integrity.patch

BuildRequires: ncurses-devel zlib-devel lzo-devel snappy-devel
BuildRequires: gcc gcc-c++ bison m4
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
* Mon Nov 21 2022 chenhaixiang <chenhaixiang3@huawei.com> - 7.3.0-8
- fix live debugging with error "cannot determine VA_BITS_ACTUAL:
  please use /proc/kcore"

* Wed Oct 19 2022 wuzx<wuzx1226@qq.com> - 7.3.0-7
- add sw64 patch

* Sun Oct 9 2022 chenhaixiang <chenhaixiang3@huawei.com> - 7.3.0-6
- fix gdb CVE-2019-1010180

* Wed Feb 23 2022 wangbin <wangbin224@huawei.com> - 7.3.0-5
- Handle task_struct cpu member changes for kernels >= 5.16-rc1
  and delete use_system_readline_v3.patch

* Tue Feb 8 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 7.3.0-4
- fix null pointer reference when CONFIG_KASAN is open

* Fri Dec 31 2021 zhouwenpei <zhouwenpei1@huawei.com> - 7.3.0-3
- add SDEI stack resolution

* Thu Dec 30 2021 zhouwenpei <zhouwenpei1@huawei.com> - 7.3.0-2
- fix seek error "IRQ stack pointer"

* Fri Dec 24 2021 zhouwenpei <zhouwenpei1@huawei.com> - 7.3.0-1
- Upgrade version to 7.3.0

* Fri Sep 03 2021 wangbin <wangbin224@huawei.com> - 7.2.9-5
- fix null pointer reference when CONFIG_KASAN is open

* Tue Jun 29 2021 zhouwenpei <zhouwenpei1@huawei.com> - 7.2.9-4
- add buildrequires m4

* Mon May 10 2021 shixuantong <shixuantong@huawei.com> - 7.2.9-3
- add -j option for building efficiency optimization

* Thu Apr 08 2021 shixuantong <shixuantong@huawei.com> - 7.2.9-2
- fix patch issue in upgrade version commit

* Mon Feb 1 2021 liudabo <liudabo1@huawei.com> - 7.2.9-1
- Upgrade version to 7.2.9

* Sat Dec 12 2020 shixuantong <shixuantong@huawei.com> - 7.2.8-4
- Update Source0, URL, add Source1 and update tarball from upstream release

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
