import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_compose_file(host):
    f = host.file('/opt/drone/docker-compose.yml')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_systemd_service_file(host):
    f = host.file('/etc/systemd/system/drone-runner.service')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_drone_runner_container_is_running(host):
    container = host.docker("drone_runner_1")
    assert container.is_running
    assert host.socket("tcp://0.0.0.0:3000").is_listening
