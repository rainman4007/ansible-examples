#!/bin/python
from ansible.module_utils.basic import *

def another_function():
   # define available arguments/parameters a user can pass to the module
  module_args = dict( test_var=dict(type='str', required=True), new=dict(type='bool', required=False, default=False) )
  # defining module to allow two parameters
  module = AnsibleModule( argument_spec=module_args, supports_check_mode=True )
  #module = AnsibleModule(argument_spec={})
  response = {"test_var": module.params['test_var']}
  #print("this is test var %s" % module.params['test_var'])
  module.exit_json(changed=False, meta=response)

def custom_function():
  print("this is custom module")
  another_function()

def main():
  custom_function()

if __name__ == '__main__' :
  main()

