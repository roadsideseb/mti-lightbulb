git-pkgs:
  pkg.installed:
    - names:
      - git
      - python-git

/root/.ssh/id_dsa:
  file.managed:
    - makedirs: True
    - user: root
    - group: root
    - mode: 0600
    - contents: |
        {{ salt['pillar.get']('github:vagrant-salter:private_key') | join('\n') | indent(8) }}

/root/.ssh/id_dsa.pub:
  file.managed:
    - makedirs: True
    - user: root
    - group: root
    - contents: {{ salt['pillar.get']('github:vagrant-salter:public_key') }}
