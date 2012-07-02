#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Extensions to the Python unit testing framework
Name:		python-testtools
Version:	0.9.15
Release:	3
License:	MIT
Group:		Development/Tools
URL:		https://launchpad.net/testtools
Source0:	http://pypi.python.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# Source0-md5:	01a30afb126de49de4998c255259d312
BuildRequires:	python-Sphinx
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sphinx-pdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testtools is a set of extensions to the Python standard library's unit
testing framework.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains HTML documentation for %{name}.

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
%doc LICENSE NEWS README
%dir %{py_sitescriptdir}/testtools
%{py_sitescriptdir}/testtools/*.py[co]
%{py_sitescriptdir}/testtools-*.egg-info
%dir %{py_sitescriptdir}/testtools/testresult
%{py_sitescriptdir}/testtools/testresult/*.py[co]

%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/*
