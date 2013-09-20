include:
  - python

postgres-ppa:
  pkgrepo.managed:
    - humanname: Postgres PPA
    - name: deb http://apt.postgresql.org/pub/repos/apt/ {{ grains['oscodename'] }}-pgdg main
    - key_url: http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc

psycopg2:
  pip.installed:
    - require:
      - cmd: pip-install

{% with postgres_version = '9.3' %}
postgresql:
  pkg.installed:
    - names:
      - postgresql-{{ postgres_version }}
      - postgresql-server-dev-{{ postgres_version }}
  service.running:
    - require:
      - pkg: postgresql
    - watch:
      - file: /etc/postgresql/{{ postgres_version }}/main/pg_hba.conf
      - file: /etc/postgresql/{{ postgres_version }}/main/postgresql.conf


/etc/postgresql/{{ postgres_version }}/main/pg_hba.conf:
  file.managed:
    - source: salt://postgresql/pg_hba.conf
    - template: jinja
    - require:
      - pkg: postgresql


/etc/postgresql/{{ postgres_version }}/main/postgresql.conf:
  file.managed:
    - source: salt://postgresql/postgresql.conf
    - template: jinja
    - context:
      postgres_version: {{ postgres_version }}
    - require:
      - pkg: postgresql
{% endwith %}

{% for build in pillar['builds'] %}
{% with postgres = pillar['postgres'][build] %}
{{ postgres['user'] }}:
  postgres_user.present:
    - createdb: True
    - createuser: False
    - superuser: False
    - runas: postgres
    - password: {{ postgres['password'] }}
    - require:
      - service: postgresql

{{ postgres['database'] }}:
  postgres_database.present:
    - owner: {{ postgres['user'] }}
    - require:
      - postgres_user: {{ postgres['user'] }} 
      - service: postgresql
{% endwith %}
{% endfor %}
