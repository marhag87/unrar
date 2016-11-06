Name:     unrar
Version:  5.4.5
Release:  1%{?dist}
Summary:  Utility for extracting, testing and viewing RAR archives

Group:    Applications/Archiving
License:  Freeware with further limitations
URL:      http://www.rarlab.com/rar_add.htm
Source0:  http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz

BuildRequires: gcc-c++

# Don't build debug package
%define debug_package %{nil}

%description
The unrar utility is a freeware program for extracting, testing and
viewing the contents of archives created with the RAR archiver version
1.50 and above.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
%make_install

%files
/bin/unrar

%changelog
* Sun Nov 06 2016 Martin Hagstrom <marhag87@gmail.com> 5.4.5-1
- Update to version 5.4.5
* Wed Jun 22 2016 Martin Hagstrom <marhag87@gmail.com> 5.4.2-1
- Initial release
