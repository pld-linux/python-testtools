#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Name:		python-testtools
Version:	0.9.34
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://pypi.python.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# Source0-md5:	51d37e7376a70cee40cf17b44889fc88
URL:		https://launchpad.net/testtools
BuildRequires:	python-Sphinx
BuildRequires:	python-devel >= 1:2.6
%if %{with tests}
BuildRequires:	python-extras
BuildRequires:	python-mimeparse
%endif
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sphinx-pdg
Requires:	python-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -l pl.UTF-8
testtools to zestaw rozszerzeń szkieletu testów jednostkowych z
biblioteki standardowej Pythona.

%package doc
Summary:	Documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja do pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains HTML documentation for %{name}.

%description doc -l pl.UTF-8
Dokumentacja HTML do pakietu %{name}.

%prep
%setup -q -n testtools-%{version}

%build
%{__python} setup.py build
%{__make} -C doc html

%if %{with tests}
%{__python} setup.py test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	-O2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py_sitescriptdir}/testtools
%{py_sitescriptdir}/testtools/*.py[co]
%dir %{py_sitescriptdir}/testtools/matchers
%{py_sitescriptdir}/testtools/matchers/*.py[co]
%dir %{py_sitescriptdir}/testtools/testresult
%{py_sitescriptdir}/testtools/testresult/*.py[co]
%{py_sitescriptdir}/testtools-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/*
