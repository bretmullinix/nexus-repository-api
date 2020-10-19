#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import re
import swagger_client
from swagger_client.rest import ApiException
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
            ---
            module: nexus_docker_repo
            
            short_description: Creates a Nexus Docker repository
            
            version_added: "2.9"
            
            description:
                - "The module can create a private docker registry."
            
            author:
                - Bret Mullinix
            '''

EXAMPLES = '''
            # List all the markdown problems for test.md
            
            - name: List all the mark down problems for test.md in the roles folder.
              custom_markdown_lint:
                name: {{role_path }}/test.md
                action: problems
            '''

RETURN = '''
            markdown_lint_problems:
                description: All the markdown lint problems
                type: str
                returned: always
            '''


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        action=dict(type='str', required=True)
    )


    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        markdown_lint_problems='No problems'
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    action_to_perform = module.params["action"]
    files_or_directories = module.params["name"]
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)



    command_to_run = ['mdl',files_or_directories]

    result['markdown_lint_problems'] = raw_output

    # output
    no_failure = True
    if no_failure is False:
        failure_message = 'Failed.'
        module.fail_json(msg=failure_message, **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()