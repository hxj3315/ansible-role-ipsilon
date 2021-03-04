## Ansible Role: ipsilon
This role is used in the Circle Linux Infrastructure. It is used to install and configure ipsilon with optional openidc support.

### Package Information
If you are using this role, it designed to work with Enterprise Linux 8. It expects that the ipsilon packages are available. The packages not in base or in epel. Your system will need to use a copr repo in your playbook. See the example below.

```
- name: Install arrfab ipsilon repo
  yum_repository:
    name: copr:copr.fedorainfracloud.org:arrfab:noggin
    description: Copr repo for noggin owned by arrfab
    file: copr_repos
    baseurl: https://download.copr.fedorainfracloud.org/results/arrfab/noggin/epel-8-$basearch/
    gpgcheck: true
    gpgkey: https://download.copr.fedorainfracloud.org/results/arrfab/noggin/pubkey.gpg
    enabled: true
```

### Variables
See [defaults variables and explanations](defaults/main.yml)

### Dependencies
This role may depend on some other roles, either statically defined, or dynamically included/imported:
  * See [meta/main.yml](meta/main.yml)
  * Or each <task>.yml under tasks folder for included/imported roles

These roles are declared in our [requirements.yml](https://github.com/circle-linux/infrastructure/blob/main/ansible/playbooks/requirements.yml)

### License
MIT (see [LICENSE](LICENSE) file)

