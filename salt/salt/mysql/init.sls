mysql-pkgs:
  pkg.installed:
    - names:
      - mysql-client
      - mysql-server
      - python-mysqldb

mysql:
  service.running:
    - watch:
      - file: /etc/mysql/my.cnf
    - require:
      - pkg: mysql-pkgs

/etc/mysql/my.cnf:
  file.managed:
    - source: salt://mysql/my.cnf
    - user: root
    - group: root
    - require:
      - pkg: mysql-pkgs

mysql-dev_app:
  mysql_user.present:
    - name: dev_app
    - host: '%'
    - password_hash: '*3FB4FB951367E478F1065E9F0B1DF24CC91ED7B2'
    - require:
      - service: mysql
      - pkg: mysql-pkgs

mysql-dev_db:
  mysql_database.present:
    - name: dev_db
    - require:
      - service: mysql
      - pkg: mysql-pkgs

mysql-dev_app_grants:
  mysql_grants.present:
    - grant: all privileges
    - database: dev_db.*
    - user: dev_app
    - host: '%'
    - require:
      - service: mysql
      - pkg: mysql-pkgs
