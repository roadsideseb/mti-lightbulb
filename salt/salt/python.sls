python-pkgs:
  pkg.installed:
    - names:
      - python-setuptools
      - python-dev
      - build-essential

pip-install:
  cmd.run:
    - name: easy_install pip
    - unless: which pip
    - require:
      - pkg: python-pkgs
