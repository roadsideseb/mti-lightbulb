client: acorn
project: agathachristie

builds:
  - dev
  - test

postgres:
  listen_addresses: "'*'"
  connections:
    - host    all             all             0.0.0.0/0            md5
    - host    all             all             ::/0                 md5
  dev:
    database: dev_db
    user: dev_app
    password: devpassword
  test:
    database: test_db
    user: test_app
    password: testpassword
