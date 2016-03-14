#
# Conditional build:
%bcond_without	doc	# HTML (sphinx-based) documentation
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform tests

Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Name:		python-testtools
Version:	1.1.0
Release:	2
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.python.org/pypi/testtools
Source0:	https://pypi.python.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# Source0-md5:	47e330e90034919d51fae6dc66f2ab9b
URL:		https://github.com/testing-cabal/testtools
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-devel-tools
BuildRequires:	python-extras
BuildRequires:	python-mimeparse
BuildRequires:	python-testtools
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-devel-tools
BuildRequires:	python3-extras
BuildRequires:	python3-mimeparse
BuildRequires:	python3-testtools
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-extras
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
Requires:	python3-extras

%description -n python3-testtools
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -n python3-testtools -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests/matchers
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests/{__init__,test_*}.py*
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/matchers
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/{__init__,test_*}.py* \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests/__pycache__/{__init__,test_*}.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py_sitescriptdir}/testtools
%{py_sitescriptdir}/testtools/*.py[co]
%dir %{py_sitescriptdir}/testtools/matchers
%{py_sitescriptdir}/testtools/matchers/*.py[co]
%dir %{py_sitescriptdir}/testtools/testresult
%{py_sitescriptdir}/testtools/testresult/*.py[co]
%dir %{py_sitescriptdir}/testtools/tests
%{py_sitescriptdir}/testtools/tests/helpers.py[co]
%{py_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-testtools
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py3_sitescriptdir}/testtools
%{py3_sitescriptdir}/testtools/*.py
%{py3_sitescriptdir}/testtools/__pycache__
%dir %{py3_sitescriptdir}/testtools/matchers
%{py3_sitescriptdir}/testtools/matchers/*.py
%{py3_sitescriptdir}/testtools/matchers/__pycache__
%dir %{py3_sitescriptdir}/testtools/testresult
%{py3_sitescriptdir}/testtools/testresult/*.py
%{py3_sitescriptdir}/testtools/testresult/__pycache__
%dir %{py3_sitescriptdir}/testtools/tests
%{py3_sitescriptdir}/testtools/tests/helpers.py
%{py3_sitescriptdir}/testtools/tests/__pycache__
%{py3_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
