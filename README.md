Role Name
=========

This role installs droneio-runner service as docker-conpose service

Requirements
------------

Docker 

Role Variables
--------------

```
drone_rpc_proto: http
drone_rpc_host: localhost
drone_rpc_secret: so_secret
drone_runner_capacity: 2
drone_runner_config_file: /etc/sysconfig/drone-runner
drone_work_dir: /opt/drone
drone_runner_image: drone/drone-runner-docker:1
drone_service_name: drone-runner
drone_service_state: started
drone_restart_handler_state: restarted
drone_service_enabled: true
```

Dependencies
------------

Centos 7

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```
- name: install runner
  hosts: all
  become: true
  roles:
    - ansible-role-docker
    - ansible-role-droneio-runner
```

License
-------

BSD

Author Information
------------------

This role was created in by [hukuruIO](https://www.hukuru.io/)
