#
# Conditional build:
%bcond_without	doc	# HTML (sphinx-based) documentation
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform tests

Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Name:		python-testtools
# keep 2.4.x here for python2 support
Version:	2.4.0
Release:	3
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.org/simple/testtools/
Source0:	https://files.pythonhosted.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# Source0-md5:	e8fc7185b47cfb908c641f8c4b2a6add
Patch0:		%{name}-tests-nosource.patch
Patch1:		%{name}-deps.patch
URL:		https://github.com/testing-cabal/testtools
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pbr >= 0.11
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-devel-tools >= 1:2.7
BuildRequires:	python-extras >= 1.0.0
BuildRequires:	python-fixtures >= 1.3.0
BuildRequires:	python-mimeparse
BuildRequires:	python-modules
BuildRequires:	python-six >= 1.4.0
BuildRequires:	python-testresources
BuildRequires:	python-testscenarios
BuildRequires:	python-traceback2
BuildRequires:	python-unittest2 >= 1.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pbr >= 0.11
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-devel-tools >= 1:3.3
BuildRequires:	python3-extras >= 1.0.0
BuildRequires:	python3-fixtures >= 1.3.0
BuildRequires:	python3-mimeparse
BuildRequires:	python3-six >= 1.4.0
BuildRequires:	python3-testresources
BuildRequires:	python3-testscenarios
%if "%{py3_ver}" < "3.5"
BuildRequires:	python3-traceback2
BuildRequires:	python3-unittest2 >= 1.0.0
%endif
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%{?with_doc:BuildRequires:	sphinx-pdg}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -l pl.UTF-8
testtools to zestaw rozszerzeń szkieletu testów jednostkowych z
biblioteki standardowej Pythona.

%package -n python3-testtools
Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Group:		Development/Tools

%description -n python3-testtools
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -n python3-testtools -l pl.UTF-8
testtools to zestaw rozszerzeń szkieletu testów jednostkowych z
biblioteki standardowej Pythona.

%package doc
Summary:	Documentation for Python testttools module
Summary(pl.UTF-8):	Dokumentacja do pakietu Pythona testttools
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains HTML documentation for Python testttools module.

%description doc -l pl.UTF-8
Dokumentacja HTML do pakietu Pythona testttools.

%prep
%setup -q -n testtools-%{version}
%patch0 -p1
%patch1 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} -m testtools.run testtools.tests.test_suite
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m testtools.run testtools.tests.test_suite
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests/{matchers,twistedsupport}
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests/{__init__,samplecases,test_*}.py*

# replace selftests __init__ by empty stub
touch $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/{matchers,twistedsupport}
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/{__init__,samplecases,test_*}.py* \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/__pycache__/{__init__,samplecases,test_*}.*.py*

# replace selftests __init__ by empty stub
touch $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/__init__.py
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README.rst
%dir %{py_sitescriptdir}/testtools
%{py_sitescriptdir}/testtools/*.py[co]
%{py_sitescriptdir}/testtools/matchers
%{py_sitescriptdir}/testtools/testresult
%{py_sitescriptdir}/testtools/tests
%{py_sitescriptdir}/testtools/twistedsupport
%{py_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-testtools
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README.rst
%dir %{py3_sitescriptdir}/testtools
%{py3_sitescriptdir}/testtools/*.py
%{py3_sitescriptdir}/testtools/__pycache__
%{py3_sitescriptdir}/testtools/matchers
%{py3_sitescriptdir}/testtools/testresult
%{py3_sitescriptdir}/testtools/tests
%{py3_sitescriptdir}/testtools/twistedsupport
%{py3_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
